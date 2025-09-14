import argparse
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf

def load_and_preprocess(path, invert_auto=True):
    """
    Load an image, convert to MNIST-style 28x28 grayscale, normalize to [0,1],
    and return both (1, 28, 28) and (1, 784) arrays.
    """
    # 1) open image and convert to grayscale
    img = Image.open(path).convert("L")

    # 2) center-crop/fit to 28x28 (keeps aspect, centers content)
    img = ImageOps.fit(img, (28, 28), method=Image.Resampling.LANCZOS)

    # 3) numpy array
    arr = np.array(img).astype("float32")

    # 4) Heuristic invert: MNIST is white digit on black bg
    # If your digit is black on white (common), the mean is high -> invert
    if invert_auto and arr.mean() > 127:
        arr = 255.0 - arr

    # 5) normalize 0..1
    arr /= 255.0

    # 6) batch shapes
    arr_28 = arr.reshape(1, 28, 28)   # for models expecting (batch, 28, 28)
    arr_784 = arr.reshape(1, 784)     # for models expecting flattened input
    return arr_28, arr_784

def call_model(loaded_model, x28, x784):
    """
    Try calling the SavedModel with different shapes/signatures.
    The notebook’s NeuralNet typically accepts flattened (1,784) and
    may require is_training=False.
    """
    # Try flattened with explicit flag (matches notebook’s call signature)
    try:
        y = loaded_model(x784, is_training=False)
        return y
    except TypeError:
        pass
    except Exception:
        pass

    # Try flattened without the flag
    try:
        y = loaded_model(x784)
        return y
    except Exception:
        pass

    # Try 2D image shape with the flag
    try:
        y = loaded_model(x28, is_training=False)
        return y
    except Exception:
        pass

    # Try 2D image shape without the flag
    y = loaded_model(x28)
    return y

def main():
    ap = argparse.ArgumentParser(description="Predict a handwritten digit (0-9) using a SavedModel from the MNIST simple NN notebook.")
    ap.add_argument("image_path", help="Path to input image (png/jpg)")
    ap.add_argument("--model", default="mnist_simple_nn", help="Path to SavedModel directory")
    ap.add_argument("--no-invert", action="store_true", help="Disable auto inversion if your image is already white digit on black")
    args = ap.parse_args()

    # Load SavedModel (exported via tf.saved_model.save(neural_net, 'mnist_simple_nn'))
    model = tf.saved_model.load(args.model)

    # Preprocess image
    x28, x784 = load_and_preprocess(args.image_path, invert_auto=not args.no_invert)

    # Predict
    out = call_model(model, x28, x784)

    # Convert to numpy
    if hasattr(out, "numpy"):
        logits_or_probs = out.numpy()
    else:
        # In some TF builds, returned tensor may be EagerTensor already or nested
        logits_or_probs = np.array(out)

    # Ensure we’re working with a 1D vector of length 10
    probs = logits_or_probs.squeeze()
    if probs.ndim > 1:
        probs = probs[0]

    # If output looks like logits, apply softmax; it’s safe even if they’re already probs
    probs = tf.nn.softmax(probs).numpy()
    pred = int(np.argmax(probs))
    conf = float(probs[pred])

    print(f"Prediction: {pred} (confidence: {conf:.3f})")
    print("Class probabilities:", np.array2string(probs, precision=3, suppress_small=True))

if __name__ == "__main__":
    main()
