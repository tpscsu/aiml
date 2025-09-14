import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define training data (scaled down)
sizes = np.array([600, 800, 1000, 1200, 1400], dtype=float)
prices = np.array([150, 200, 250, 300, 350], dtype=float)

# Normalize the data (helps training)
sizes /= 1000
prices /= 1000

# Step 2: Build the model (cleaner input)
model = tf.keras.Sequential([
    tf.keras.Input(shape=(1,)),
    tf.keras.layers.Dense(units=1)
])

# Step 3: Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Step 4: Train the model
model.fit(sizes, prices, epochs=500, verbose=0)

# Step 5: Print learned weight and bias
weights = model.layers[0].get_weights()
slope = weights[0][0][0]   # 💡 Extract scalar float
bias = weights[1][0]       # 💡 Extract scalar float
print(f"Learned weight (slope): {slope:.4f}")
print(f"Learned bias (intercept): {bias:.4f}")

# Step 6: Predict price for 1600 sq ft
new_size = 1.6
predicted_price = model.predict(np.array([new_size]))[0][0]
print(f"Predicted price for {new_size*1000:.0f} sq ft: ${predicted_price*1000:.2f}")

# Step 7: Plot the result
predicted_prices = model.predict(sizes)

plt.scatter(sizes * 1000, prices * 1000, label='Training Data')
plt.plot(sizes * 1000, predicted_prices * 1000, color='red', label='Model Prediction')
plt.axvline(new_size * 1000, linestyle='--', color='gray', label='Prediction Input')
plt.title("House Price Prediction")
plt.xlabel("House Size (sq ft)")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.show()
