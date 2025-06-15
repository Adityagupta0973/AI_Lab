import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the dataset
url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240320114716/data_for_lr.csv'
data = pd.read_csv(url)
data = data.dropna()  # Remove missing values

# Prepare training data
X_train = np.array(data['x'][:500]).reshape(-1, 1)
y_train = np.array(data['y'][:500]).reshape(-1, 1)

# Define a simple Linear Regression class
class SimpleLinearRegression:
    def __init__(self):
        # Start with random values for slope (m) and intercept (c)
        self.m = np.random.uniform(-1, 1)
        self.c = np.random.uniform(-1, 1)
        self.losses = []

    def predict(self, X):
        return self.m * X + self.c

    def compute_loss(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)

    def update_weights(self, X, y_true, y_pred, learning_rate):
        error = y_pred - y_true
        dm = 2 * np.mean(X * error)
        dc = 2 * np.mean(error)
        self.m -= learning_rate * dm
        self.c -= learning_rate * dc

    def train(self, X, y, learning_rate=0.0001, epochs=20):
        fig, ax = plt.subplots()
        x_vals = np.linspace(X.min(), X.max(), 100)
        line, = ax.plot(x_vals, self.predict(x_vals), color='red', label='Regression Line')
        ax.scatter(X, y, color='green', label='Training Data')
        ax.set_ylim(0, y.max() + 1)

        def update(frame):
            y_pred = self.predict(X)
            loss = self.compute_loss(y, y_pred)
            self.update_weights(X, y, y_pred, learning_rate)
            self.losses.append(loss)

            # Update the line on the graph
            line.set_ydata(self.predict(x_vals))
            print(f"Epoch {frame+1}, Loss: {loss:.4f}")
            return line,

        ani = FuncAnimation(fig, update, frames=epochs, interval=500, blit=True)
        ani.save('simple_linear_regression.gif', writer='ffmpeg')

        plt.title("Simple Linear Regression")
        plt.xlabel("Input (x)")
        plt.ylabel("Output (y)")
        plt.legend()
        plt.show()

        return self.m, self.c, self.losses

# Run the training
model = SimpleLinearRegression()
m, c, losses = model.train(X_train, y_train, learning_rate=0.0001, epochs=20)


# LOGISTIC REGRESSION
# from sklearn.datasets import load_breast_cancer
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score

# # Load the breast cancer dataset
# X, y = load_breast_cancer(return_X_y=True)

# # Split data into training and testing sets (80% train, 20% test)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Create and train the Logistic Regression model
# model = LogisticRegression(max_iter=10000)
# model.fit(X_train, y_train)

# # Make predictions and calculate accuracy
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred) * 100

# # Print result
# print(f"Logistic Regression Accuracy: {accuracy:.2f}%")
