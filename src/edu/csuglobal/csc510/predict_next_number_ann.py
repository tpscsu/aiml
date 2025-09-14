import numpy as np

# --- Sigmoid Activation Function ---
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# --- Derivative of Sigmoid Function ---
def sigmoid_derivative(x):
    return x * (1 - x)

# --- Mean Squared Error Loss Function ---
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# --- Load Training Data and Normalize ---
# Inputs are scaled between 0–1 by dividing by 20
# Outputs are scaled between 0–1 by dividing by 40
# (Assumes max input = 20, max sum = 40 for safety)
def load_training_data(filename):
    X = []
    y = []
    with open(filename, 'r') as f:
        for line in f:
            parts = list(map(float, line.strip().split(',')))
            X.append([parts[0] / 20, parts[1] / 20])   # normalize inputs
            y.append([parts[2] / 40])                  # normalize output
    return np.array(X), np.array(y)

# --- Train the Neural Network ---
def train_ann(X, y, hidden_layer_size=4, epochs=10000, learning_rate=0.1):
    input_size = X.shape[1]
    output_size = y.shape[1]

    np.random.seed(42)
    weights_input_to_hidden = np.random.randn(input_size, hidden_layer_size)
    bias_hidden_layer = np.zeros((1, hidden_layer_size))
    weights_hidden_to_output = np.random.randn(hidden_layer_size, output_size)
    bias_output_layer = np.zeros((1, output_size))

    for _ in range(epochs):
        # Feedforward
        hidden_layer_input = np.dot(X, weights_input_to_hidden) + bias_hidden_layer
        hidden_layer_output = sigmoid(hidden_layer_input)

        output_layer_input = np.dot(hidden_layer_output, weights_hidden_to_output) + bias_output_layer
        y_pred = output_layer_input  # linear output

        # Backpropagation
        error = y - y_pred
        gradient_output_weights = np.dot(hidden_layer_output.T, error)
        gradient_output_bias = np.sum(error, axis=0, keepdims=True)

        hidden_layer_error = np.dot(error, weights_hidden_to_output.T) * sigmoid_derivative(hidden_layer_output)
        gradient_hidden_weights = np.dot(X.T, hidden_layer_error)
        gradient_hidden_bias = np.sum(hidden_layer_error, axis=0, keepdims=True)

        # Update weights and biases
        weights_input_to_hidden += learning_rate * gradient_hidden_weights
        bias_hidden_layer += learning_rate * gradient_hidden_bias
        weights_hidden_to_output += learning_rate * gradient_output_weights
        bias_output_layer += learning_rate * gradient_output_bias

    return weights_input_to_hidden, bias_hidden_layer, weights_hidden_to_output, bias_output_layer

# --- Predict and De-normalize Output ---
def predict(inputs, weights_input_to_hidden, bias_hidden_layer, weights_hidden_to_output, bias_output_layer):
    # Normalize input to match training scale
    normalized_input = np.array([[inputs[0] / 20, inputs[1] / 20]])
    hidden_layer_output = sigmoid(np.dot(normalized_input, weights_input_to_hidden) + bias_hidden_layer)
    normalized_output = np.dot(hidden_layer_output, weights_hidden_to_output) + bias_output_layer
    return normalized_output[0][0] * 40  # De-normalize prediction

if __name__ == "__main__":
    # Load and normalize training data
    X, y = load_training_data("training_data.txt")

    print("Training ANN...")
    weights_input_to_hidden, bias_hidden_layer, weights_hidden_to_output, bias_output_layer = train_ann(X, y)
    print("Training complete.\n")

    # Interactive input loop
    while True:
        user_input = input("Enter two numbers separated by a comma (or type 'exit' to quit): ").strip().lower()
        if user_input == 'exit':
            print("Exiting...")
            break
        try:
            a, b = map(float, user_input.split(','))
            prediction = predict((a, b), weights_input_to_hidden, bias_hidden_layer, weights_hidden_to_output, bias_output_layer)
            print(f"Predicted output (sum): {prediction:.2f}\n")
        except Exception as e:
            print(f"Invalid input. Please enter two numbers like: 5,6  — Error: {e}\n")
