# Student Pass/Fail Predictor using Logistic Regression
# Building AI - Final Project

import math

# Data: [hours studied, passed? 1 = pass, 0 = fail]
data = [
    [1, 0], [2, 0], [3, 0], [4, 0],
    [5, 0], [6, 1], [7, 1], [8, 1],
    [9, 1], [10, 1]
]

w = 0.0
b = 0.0

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

for _ in range(1000):
    for hours, passed in data:
        pred = sigmoid(w * hours + b)
        error = pred - passed
        w -= 0.1 * error * hours
        b -= 0.1 * error

print(f"Trained model: w = {w:.2f}, b = {b:.2f}")
print("---")

for hours in [2, 5, 7, 9]:
    prob = sigmoid(w * hours + b)
    result = "PASS" if prob > 0.5 else "FAIL"
    print(f"{hours} hours studied -> {prob*100:.1f}% chance -> {result}")
