# polynomial_regression.py
# Predict employee salary based on years of experience using Polynomial Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Step 1: Load dataset
# Salary_Data.csv is in the same folder as this script
data = pd.read_csv("Salary_Data.csv")
X = data[['YearsExperience']].values
y = data['Salary'].values

# Step 2: Transform input to polynomial features (degree 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Step 3: Train polynomial regression model
model = LinearRegression()
model.fit(X_poly, y)

# Step 4: Visualize the results
plt.scatter(X, y, color='blue', label="Actual Data")
X_grid = np.linspace(min(X), max(X), 100).reshape(-1, 1)
plt.plot(X_grid, model.predict(poly.transform(X_grid)), color='red', label="Polynomial Regression")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Polynomial Regression - Salary Prediction")
plt.legend()
plt.show()

# Step 5: Get user input and predict
try:
    years = float(input("Enter years of experience: "))
    predicted_salary = model.predict(poly.transform([[years]]))
    print(f"Predicted salary for {years} years of experience: ${predicted_salary[0]:.2f}")
except ValueError:
    print("Invalid input. Please enter a number for years of experience.")
