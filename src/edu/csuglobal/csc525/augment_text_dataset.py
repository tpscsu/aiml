#!/usr/bin/env python3

"""
Text Dataset Augmentation (TXT and CSV)

- TXT: treats each line as one training example
- CSV: specify --text_col (default: 'text'); all other columns are preserved
- Augmentations: synonym replacement (WordNet), random deletion, random swap,
  random insertion (synonym), and keyboard-typo noise

Outputs per source file:
  <name>_original.<ext>
  <name>_augmented.<ext>

Usage examples:
  python augment_text_dataset.py --input_dir ./datasets --output_dir ./aug_out --n_aug 3
  python augment_text_dataset.py --input_dir ./datasets --output_dir ./aug_out --text_col text --n_aug 2
  python augment_text_dataset.py --input_dir ./datasets --output_dir ./aug_out --ops synonym,swap,delete,insert,typo
"""

import argparse
import csv
import os
import random
import re
import shutil
from pathlib import Path
from typing import List, Tuple, Dict

import pandas as pd
from tqdm import tqdm

# NLTK (download at first run if missing)
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

# ---------- NLTK setup ----------
def ensure_nltk():
    try:
        _ = wn.synsets("dog")
    except:
        nltk.download("wordnet", quiet=True)
        nltk.download("omw-1.4", quiet=True)
    try:
        _ = stopwords.words("english")
    except:
        nltk.download("stopwords", quiet=True)

# ---------- Token utils ----------
WORD_RE = re.compile(r"\w+('\w+)?", re.UNICODE)

def simple_tokenize(text: str) -> List[str]:
    # Lightweight tokenizer
    tokens = []
    i = 0
    while i < len(text):
        m = WORD_RE.match(text, i)
        if m:
            tokens.append(m.group())
            i = m.end()
        else:
            tokens.append(text[i])
            i += 1
    return tokens

def detokenize(tokens: List[str]) -> str:
    # Join tokens with simple rule: don't add spaces before punctuation
    out = []
    for i, tok in enumerate(tokens):
        if i > 0 and re.match(r"[\w']", tok):
            if not re.match(r"\s", tok) and not re.match(r"[.,!?;:)\]}]", tok):
                out.append(" ")
        out.append(tok)
    return "".join(out)

# ---------- Synonyms ----------
def get_synonyms(word: str) -> List[str]:
    syns = set()
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            s = lemma.name().replace("_", " ")
            if s.lower() != word.lower():
                syns.add(s)
    # Prefer single-word synonyms to keep tokenization simple; fall back otherwise
    single = [s for s in syns if " " not in s]
    return single if single else list(syns)

# ---------- Keyboard neighbor map (US QWERTY, minimal) ----------
NEIGHBORS: Dict[str, str] = {
    "q":"w", "w":"qe", "e":"wr", "r":"et", "t":"ry", "y":"tu", "u":"yi", "i":"uo", "o":"ip", "p":"o",
    "a":"s", "s":"ad", "d":"sf", "f":"dg", "g":"fh", "h":"gj", "j":"hk", "k":"jl", "l":"k",
    "z":"x", "x":"zc", "c":"xv", "v":"cb", "b":"vn", "n":"bm", "m":"n"
}
def keyboard_typo(text: str, char_prob: float = 0.02) -> str:
    out = []
    for ch in text:
        if ch.lower() in NEIGHBORS and random.random() < char_prob:
            neigh = random.choice(list(NEIGHBORS[ch.lower()]))
            out.append(neigh.upper() if ch.isupper() else neigh)
        else:
            out.append(ch)
    return "".join(out)

# ---------- Augment ops ----------
EN_STOPS = set()

def op_synonym_replace(tokens: List[str], p: float = 0.1) -> Tuple[List[str], str]:
    new = tokens[:]
    changed = 0
    for idx, t in enumerate(tokens):
        if not re.match(r"^\w", t):  # skip punctuation & spaces
            continue
        if t.lower() in EN_STOPS:
            continue
        if random.random() < p:
            syns = get_synonyms(t)
            if syns:
                repl = random.choice(syns)
                # Keep capitalization style
                if t.istitle():
                    repl = repl.title()
                elif t.isupper():
                    repl = repl.upper()
                new[idx] = repl
                changed += 1
    return new, f"synonym(x{changed})"

def op_random_delete(tokens: List[str], p: float = 0.08) -> Tuple[List[str], str]:
    kept = []
    deleted = 0
    for t in tokens:
        if re.match(r"^\w", t) and random.random() < p:
            deleted += 1
            continue
        kept.append(t)
    if not kept:
        kept = tokens[:]  # avoid empty
        deleted = 0
    return kept, f"delete(x{deleted})"

def op_random_swap(tokens: List[str], n_swaps: int = 1) -> Tuple[List[str], str]:
    new = tokens[:]
    word_idxs = [i for i, t in enumerate(tokens) if re.match(r"^\w", t)]
    swaps = 0
    for _ in range(n_swaps):
        if len(word_idxs) < 2: break
        i, j = sorted(random.sample(word_idxs, 2))
        new[i], new[j] = new[j], new[i]
        swaps += 1
    return new, f"swap(x{swaps})"

def op_random_insert(tokens: List[str], n_inserts: int = 1) -> Tuple[List[str], str]:
    new = tokens[:]
    word_idxs = [i for i, t in enumerate(tokens) if re.match(r"^\w", t)]
    inserts = 0
    for _ in range(n_inserts):
        if not word_idxs: break
        i = random.choice(word_idxs)
        syns = get_synonyms(tokens[i])
        if syns:
            ins = random.choice(syns)
            new.insert(i, ins)
            inserts += 1
    return new, f"insert(x{inserts})"

def op_typo_text(text: str, char_prob: float = 0.02) -> Tuple[str, str]:
    return keyboard_typo(text, char_prob=char_prob), f"typo(p={char_prob})"

# ---------- Pipeline ----------
def augment_text_once(text: str, ops: List[str]) -> Tuple[str, List[str]]:
    # order: token ops -> detokenize -> char-level typo (if selected)
    tokens = simple_tokenize(text)
    applied = []
    if "synonym" in ops:
        tokens, tag = op_synonym_replace(tokens, p=0.12)
        applied.append(tag)
    if "delete" in ops:
        tokens, tag = op_random_delete(tokens, p=0.08)
        applied.append(tag)
    if "swap" in ops:
        tokens, tag = op_random_swap(tokens, n_swaps=1)
        applied.append(tag)
    if "insert" in ops:
        tokens, tag = op_random_insert(tokens, n_inserts=1)
        applied.append(tag)
    out = detokenize(tokens)
    if "typo" in ops:
        out, tag = op_typo_text(out, char_prob=0.015)
        applied.append(tag)
    return out, applied

def process_txt_file(src: Path, out_dir: Path, n_aug: int, ops: List[str], report) -> None:
    dst_orig = out_dir / f"{src.stem}_original.txt"
    dst_aug  = out_dir / f"{src.stem}_augmented.txt"

    # Save original copy
    shutil.copyfile(src, dst_orig)

    total = 0
    aug_total = 0
    with src.open("r", encoding="utf-8", errors="ignore") as fin, \
            dst_aug.open("w", encoding="utf-8") as fout:
        for line in tqdm(fin, desc=f"[TXT] {src.name}"):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            total += 1
            # write original
            fout.write(line + "\n")
            # write augmentations
            for _ in range(n_aug):
                aug, applied = augment_text_once(line, ops)
                fout.write(aug + "\n")
                aug_total += 1

    report.append(f"- {src.name}: {total} originals, {aug_total} augmented → {dst_aug.name}")

def process_csv_file(src: Path, out_dir: Path, text_col: str, n_aug: int, ops: List[str], report) -> None:
    dst_orig = out_dir / f"{src.stem}_original.csv"
    dst_aug  = out_dir / f"{src.stem}_augmented.csv"

    df = pd.read_csv(src)
    if text_col not in df.columns:
        raise ValueError(f"{src.name}: text column '{text_col}' not found. Columns: {list(df.columns)}")

    df.to_csv(dst_orig, index=False)

    rows = []
    total = 0
    aug_total = 0
    for _, row in tqdm(df.iterrows(), total=len(df), desc=f"[CSV] {src.name}"):
        text = str(row[text_col])
        base = row.copy()
        base["aug_source"] = "original"
        base["aug_ops"] = ""
        rows.append(base)
        total += 1

        for _ in range(n_aug):
            aug_text, applied = augment_text_once(text, ops)
            new_row = row.copy()
            new_row[text_col] = aug_text
            new_row["aug_source"] = "augmented"
            new_row["aug_ops"] = ",".join(applied)
            rows.append(new_row)
            aug_total += 1

    out = pd.DataFrame(rows)
    out.to_csv(dst_aug, index=False, quoting=csv.QUOTE_MINIMAL)
    report.append(f"- {src.name}: {total} originals, {aug_total} augmented → {dst_aug.name}")

def main():
    parser = argparse.ArgumentParser(description="Text dataset augmentation (TXT/CSV).")
    parser.add_argument("--input_dir", required=True, help="Folder with datasets")
    parser.add_argument("--output_dir", required=True, help="Where to write outputs")
    parser.add_argument("--text_col", default="text", help="CSV text column name (default: text)")
    parser.add_argument("--file_glob", default="**/*", help="Optional glob within input_dir")
    parser.add_argument("--n_aug", type=int, default=1, help="Augmentations per original example")
    parser.add_argument("--ops", default="synonym,delete,swap,insert,typo",
                        help="Comma-separated ops: synonym,delete,swap,insert,typo")
    args = parser.parse_args()

    random.seed(13)
    ensure_nltk()
    global EN_STOPS
    EN_STOPS = set(stopwords.words("english"))

    in_dir = Path(args.input_dir).resolve()
    out_dir = Path(args.output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    ops = [o.strip().lower() for o in args.ops.split(",") if o.strip()]
    report_lines = [
        "# AUGMENTATION REPORT",
        "",
        f"- Input directory: `{in_dir}`",
        f"- Output directory: `{out_dir}`",
        f"- Operations: {ops}",
        f"- Augmentations per example: {args.n_aug}",
        ""
    ]

    found = 0
    for p in in_dir.glob(args.file_glob):
        if p.is_file() and p.suffix.lower() == ".txt":
            found += 1
            process_txt_file(p, out_dir, n_aug=args.n_aug, ops=ops, report=report_lines)

    for p in in_dir.glob(args.file_glob):
        if p.is_file() and p.suffix.lower() == ".csv":
            found += 1
            process_csv_file(p, out_dir, text_col=args.text_col, n_aug=args.n_aug, ops=ops, report=report_lines)

    if found == 0:
        report_lines.append("_No .txt or .csv files found._")

    # Write a top-level report
    with (out_dir / "AUGMENTATION_REPORT.md").open("w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print("\n".join(report_lines))
    print("\nDone.")

if __name__ == "__main__":
    main()
