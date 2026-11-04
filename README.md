
# Student Pass/Fail Predictor

## About the Project

The Student Pass/Fail Predictor is a simple AI project that predicts whether a student will PASS or FAIL based on the number of hours they study.

This project is built using Python and Logistic Regression from scratch without using any machine learning libraries.

## How It Works

1. The model is trained using student study hours and pass/fail data.
2. Logistic Regression learns the relationship between study hours and student results.
3. The Sigmoid function converts the model's output into a probability between 0 and 1.
4. If the probability is greater than 0.5, the student is predicted to PASS.
5. Otherwise, the student is predicted to FAIL.

## Technologies Used

- Python
- Logistic Regression
- Sigmoid Function
- Gradient Descent
- GitHub

## How to Run

Make sure Python is installed on your computer.

Run the following command in your terminal:

```bash
python main.py
```

## Example Output

```text
Trained model... w = 1.42, b = -7.52

2 hours studied -> 5.8% chance -> FAIL
5 hours studied -> 38.5% chance -> FAIL
7 hours studied -> 77.2% chance -> PASS
9 hours studied -> 94.8% chance -> PASS
```

## What I Learned

- How Logistic Regression works
- How the Sigmoid function converts numbers into probabilities
- How Gradient Descent trains a model
- How to build a simple AI model from scratch
- How to create and manage a project using GitHub

## Project Goal

This project was created as part of the Building AI course to understand the basic concepts of Artificial Intelligence and Machine Learning.

## Project By

Building AI - Final Project
