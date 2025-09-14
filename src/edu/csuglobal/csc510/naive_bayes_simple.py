#!/usr/bin/env python3
# Features: frequency table, likelihoods with Laplace, posteriors per class, CLI

from collections import Counter, defaultdict
import math

# embedded categorical dataset (Weather Play)
DATA = [
    {"Outlook": "Sunny",    "Temperature": "Hot",  "Humidity": "High",   "Wind": "Weak",   "Play": "No"},
    {"Outlook": "Sunny",    "Temperature": "Hot",  "Humidity": "High",   "Wind": "Strong", "Play": "No"},
    {"Outlook": "Overcast", "Temperature": "Hot",  "Humidity": "High",   "Wind": "Weak",   "Play": "Yes"},
    {"Outlook": "Rain",     "Temperature": "Mild", "Humidity": "High",   "Wind": "Weak",   "Play": "Yes"},
    {"Outlook": "Rain",     "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak",   "Play": "Yes"},
    {"Outlook": "Rain",     "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "Play": "No"},
    {"Outlook": "Overcast", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "Play": "Yes"},
    {"Outlook": "Sunny",    "Temperature": "Mild", "Humidity": "High",   "Wind": "Weak",   "Play": "No"},
    {"Outlook": "Sunny",    "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak",   "Play": "Yes"},
    {"Outlook": "Rain",     "Temperature": "Mild", "Humidity": "Normal", "Wind": "Weak",   "Play": "Yes"},
    {"Outlook": "Sunny",    "Temperature": "Mild", "Humidity": "Normal", "Wind": "Strong", "Play": "Yes"},
    {"Outlook": "Overcast", "Temperature": "Mild", "Humidity": "High",   "Wind": "Strong", "Play": "Yes"},
    {"Outlook": "Overcast", "Temperature": "Hot",  "Humidity": "Normal", "Wind": "Weak",   "Play": "Yes"},
    {"Outlook": "Rain",     "Temperature": "Mild", "Humidity": "High",   "Wind": "Strong", "Play": "No"},
]
FEATURES = ["Outlook", "Temperature", "Humidity", "Wind"]
TARGET = "Play"
ALPHA = 1.0  # Laplace smoothing

def domains(data, features):
    return {f: sorted({row[f] for row in data}) for f in features}

def class_priors(data, target):
    counts = Counter(row[target] for row in data)
    total = sum(counts.values())
    return {c: counts[c] / total for c in counts}, counts

def frequency_tables(data, features, target):
    freq = {f: defaultdict(Counter) for f in features}
    for row in data:
        y = row[target]
        for f in features:
            freq[f][y][row[f]] += 1
    return freq

def likelihoods(freq, doms, class_counts, alpha=1.0):
    like = {f: {} for f in freq}
    for f in freq:
        V = len(doms[f])
        like[f] = {c: {} for c in class_counts}
        for c in class_counts:
            denom = class_counts[c] + alpha * V
            for v in doms[f]:
                like[f][c][v] = (freq[f][c][v] + alpha) / denom
    return like

def posterior(instance, priors, like, classes):
    scores = {}
    for c in classes:
        s = math.log(priors[c])
        for f, v in instance.items():
            s += math.log(like[f][c].get(v, 1e-12))  # tiny fallback if unseen
        scores[c] = s
    m = max(scores.values())
    exps = {c: math.exp(scores[c] - m) for c in classes}
    Z = sum(exps.values())
    return {c: exps[c] / Z for c in classes}

def print_tables(priors, freq, like):
    print("\n== Class Priors ==")
    for c, p in priors.items():
        print(f"P(Y={c}) = {p:.3f}")

    print("\n== Frequency Tables (counts) ==")
    for f in freq:
        print(f"\nFeature: {f}")
        vals = sorted({v for c in freq[f] for v in freq[f][c]})
        header = "value".ljust(12) + " | " + " | ".join(c.center(6) for c in sorted(freq[f].keys()))
        print(header)
        print("-" * len(header))
        for v in vals:
            row = v.ljust(12) + " | " + " | ".join(str(freq[f][c][v]).center(6) for c in sorted(freq[f].keys()))
            print(row)

    print("\n== Likelihoods P(X=v | Y=c) with Laplace ==")
    for f in like:
        print(f"\nFeature: {f}")
        vals = sorted(next(iter(like[f].values())).keys())
        header = "value".ljust(12) + " | " + " | ".join(f"Y={c}".center(10) for c in sorted(like[f].keys()))
        print(header)
        print("-" * len(header))
        for v in vals:
            row = v.ljust(12) + " | " + " | ".join(f"{like[f][c][v]:.3f}".center(10) for c in sorted(like[f].keys()))
            print(row)

def main():
    doms = domains(DATA, FEATURES)
    priors, class_counts = class_priors(DATA, TARGET)
    freq = frequency_tables(DATA, FEATURES, TARGET)
    like = likelihoods(freq, doms, class_counts, ALPHA)

    print_tables(priors, freq, like)

    print("\nEnter a test instance (press Enter to use the shown default in brackets):")
    def ask(f, default):
        val = input(f"{f} {doms[f]} [{default}]: ").strip()
        return val if val in doms[f] else default

    defaults = {f: doms[f][0] for f in FEATURES}
    inst = {f: ask(f, defaults[f]) for f in FEATURES}

    post = posterior(inst, priors, like, sorted(priors.keys()))
    print("\n== Posterior P(Y | x) ==")
    for c in sorted(post):
        print(f"P(Y={c} | x) = {post[c]:.3f}")
    pred = max(post, key=post.get)
    print(f"Predicted class: {pred}")

if __name__ == "__main__":
    main()
