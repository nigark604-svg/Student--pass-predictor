# Student Pass/Fail Predictor

This project predicts whether a student will PASS or FAIL based on how many hours they studied.

Built with Python using Logistic Regression from scratch - no libraries used for machine learning.

## How It Works

1. We give the model data: hours studied vs pass/fail
2. Model learns a pattern using Logistic Regression
3. It uses the Sigmoid function to give a probability between 0 and 1
4. If probability > 0.5, prediction = PASS, else FAIL

## How to Run

```bash
python main.py
Trained model: w = 1.42, b = -7.52
---
2 hours studied -> 5.8% chance -> FAIL
5 hours studied -> 38.5% chance -> FAIL
7 hours studied -> 77.2% chance -> PASS
9 hours studied -> 94.8% chance -> PASS
## What I Learned
‎
‎- How Logistic Regression works
‎- How Sigmoid function converts numbers to probability
‎- How Gradient Descent trains a model
‎- How to build AI from scratch
‎
## ‎ Project by
‎
‎Building AI - Final Project
