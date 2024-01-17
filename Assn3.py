#Write a python program using perceptron neural network to recognize even and odd numbers. Given numbers are in ASCII from 0 to 9

import numpy as np

# Training data (binary representation of numbers 0 to 9)
training_data = [
    (np.array([0, 0, 1, 1, 0, 0, 0, 0]), 0),  # 0 in binary, even   = 48
    (np.array([0, 0, 1, 1, 0, 0, 0, 1]), 1),  # 1 in binary, odd
    (np.array([0, 0, 1, 1, 0, 0, 1, 0]), 0),  # 2 in binary, even
    (np.array([0, 0, 1, 1, 0, 0, 1, 1]), 1),  # 3 in binary, odd
    (np.array([0, 0, 1, 1, 0, 1, 0, 0]), 0),  # 4 in binary, even
    (np.array([0, 0, 1, 1, 0, 1, 0, 1]), 1),  # 5 in binary, odd
    (np.array([0, 0, 1, 1, 0, 1, 1, 0]), 0),  # 6 in binary, even
    (np.array([0, 0, 1, 1, 0, 1, 1, 1]), 1),  # 7 in binary, odd
    (np.array([0, 0, 1, 1, 1, 0, 0, 0]), 0),  # 8 in binary, even
    (np.array([0, 0, 1, 1, 1, 0, 0, 1]), 1),  # 9 in binary, odd
]

# Perceptron class
class Perceptron:
    def __init__(self):      
        self.weights = np.random.randn(8, 1)  # Random initial weights
    
    #Activation Function
    def activate(self, x):
        z = x @ self.weights
        return np.where(z >=0, 1, 0) #Step act function
        
    def train(self, training_data, epochs):
        for epoch in range(epochs):
            for x, y in training_data:
                x = np.array([x])
                y = np.array([[y]])
                output = self.activate(x)
                error = y - output
                self.weights += x.T @ error

    def predict(self, x):
        x = np.array([x])
        output = self.activate(x)
        return output

# Create and train the perceptron
perceptron = Perceptron()
perceptron.train(training_data, epochs=25)

# Test the perceptron
test_numbers = [
    (np.array([0, 0, 1, 1, 0, 0, 0, 0])),  # 0 in binary, even   = 48
    (np.array([0, 0, 1, 1, 0, 0, 0, 1])),  # 1 in binary, odd
    (np.array([0, 0, 1, 1, 0, 0, 1, 0])),  # 2 in binary, even
    (np.array([0, 0, 1, 1, 0, 0, 1, 1])),  # 3 in binary, odd
    (np.array([0, 0, 1, 1, 0, 1, 0, 0])),  # 4 in binary, even
    (np.array([0, 0, 1, 1, 0, 1, 0, 1])),  # 5 in binary, odd
    (np.array([0, 0, 1, 1, 0, 1, 1, 0])),  # 6 in binary, even
    (np.array([0, 0, 1, 1, 0, 1, 1, 1])),  # 7 in binary, odd
    (np.array([0, 0, 1, 1, 1, 0, 0, 0])),  # 8 in binary, even
    (np.array([0, 0, 1, 1, 1, 0, 0, 1])),  # 9 in binary, odd
]

for i in test_numbers:
    prediction = perceptron.predict(i)
    if prediction == 0:
        print(f"{i}: Even")
    else:
        print(f"{i}: Odd")
