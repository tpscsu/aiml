#!/usr/bin/env python3
# knn_iris.py
# Minimal KNN classifier for the Iris dataset with interactive input.
# Usage:
#   python knn_iris.py
# Then enter the four values when prompted.

from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def main():
    # Ask user for inputs
    try:
        sl = float(input("Enter sepal length (cm): "))
        sw = float(input("Enter sepal width  (cm): "))
        pl = float(input("Enter petal length (cm): "))
        pw = float(input("Enter petal width  (cm): "))
    except ValueError:
        print("All inputs must be numbers.")
        return

    csv_path = Path(__file__).with_name("iris.csv")
    if not csv_path.exists():
        print(f"iris.csv not found in the same folder as this script.")
        return

    # Load dataset
    df = pd.read_csv(csv_path)
    X = df[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]].to_numpy()
    y = df["Name"].to_numpy()

    # Simple KNN with k=5
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X, y)

    # Predict
    sample = np.array([[sl, sw, pl, pw]])
    pred = model.predict(sample)[0]
    print(f"\nPredicted iris class: {pred}")

if __name__ == "__main__":
    main()
