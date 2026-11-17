# ============================================================
# DAY 01 — HOW MACHINE LEARNING MODELS WORK
# Source: Kaggle — Introduction to Machine Learning
# https://www.kaggle.com/learn/intro-to-machine-learning/how-models-work
#
# STATUS:
# [x] Studied the general idea of ML and a simple Decision Tree.
# [x] Understood that predictions can use the mean in each leaf.
# [x] Discussed how the tree compares candidate splits.
# [ ] REVIEW NEXT: Thresholds (3 vs 3.5).
# [ ] REVIEW NEXT: Training error vs validation error.
# [ ] PRACTICE NEXT: Run and explain the Decision Tree code.
# ============================================================


# 1) WHAT IS MACHINE LEARNING?
# ------------------------------------------------------------
# A Machine Learning model learns patterns from past examples.
# Then it uses those patterns to make predictions on new data.
#
# Example: Learn from known house prices to estimate the price
# of another house.
#
# IMPORTANT: A prediction is not guaranteed to be correct.


# 2) FEATURES (X) AND TARGET (y)
# ------------------------------------------------------------
# X = the input features used by the model.
# y = the value we want the model to predict.
#
# In our house-price example:
#   X = number of bedrooms
#   y = house price (in millions)
#
#   Bedrooms (X)   Price (y)
#       2              1.0
#       3              1.2
#       4              2.0
#       5              2.2
#
# Real house prices depend on other features too, such as
# location, area, and condition. This is a teaching example.


# 3) WHAT IS A DECISION TREE?
# ------------------------------------------------------------
# A Decision Tree makes a prediction by asking questions.
# Each question splits the data into smaller groups.
#
# Example split:
#   Is the number of bedrooms greater than 3?
#
#   NO  -> houses with 2 or 3 bedrooms
#   YES -> houses with 4 or 5 bedrooms
#
# For this regression example, the leaf prediction is the
# average house price among training examples in that leaf.
#
#   Left leaf:  (1.0 + 1.2) / 2 = 1.1 million
#   Right leaf: (2.0 + 2.2) / 2 = 2.1 million
#
# Example: a house with 5 bedrooms goes to the right leaf,
# so this simple tree predicts 2.1 million.
#
# Leaf = the final point in a tree where a prediction is made.


# 4) HOW DOES A TREE SELECT A QUESTION (SPLIT)?
# ------------------------------------------------------------
# It compares candidate splits and checks how much error
# each split creates on the TRAINING data.
#
# For this regression example, smaller squared error is better.
#
# We tried splitting after the bedroom counts 2, 3, or 4:
#
#   Split                        SSE        MSE
#   Bedrooms > 2                0.56       0.14
#   Bedrooms > 3                0.04       0.01   <- best
#   Bedrooms > 4                0.56       0.14
#
# SSE (sum of squared errors) = total of squared mistakes.
# MSE (mean squared error) = SSE / number of examples.
# Here, there are 4 houses, so MSE = SSE / 4.
#
# The model did not pick the >3 split at random.
# It gave the smallest training error among these choices.


# 5) THRESHOLD — TO REVIEW NEXT SESSION
# ------------------------------------------------------------
# Libraries often test a split BETWEEN two sorted values.
# Between 3 bedrooms and 4 bedrooms is the threshold 3.5.
# On the integer bedroom values in this example:
#   Bedrooms > 3   and   Bedrooms > 3.5
# put exactly the SAME houses into the same groups.
#
# NOTE: We discussed this but still need to make it intuitive.


# 6) TRAINING, VALIDATION, AND OVERFITTING — TO REVIEW
# ------------------------------------------------------------
# Training / fitting: learning rules from training examples.
# Training error: error on the examples used for fitting.
# Validation error: error on held-out examples used to compare
# models / settings, such as the tree's maximum depth.
#
# A deeper tree may fit the training examples more closely,
# but this does not guarantee better results on new houses.
# This problem is called overfitting.
#
# NOTE: This topic is NOT yet fully understood; review tomorrow.


# 7) WHAT IS NEXT?
# ------------------------------------------------------------
# [ ] Explain thresholds with a clear example.
# [ ] Understand training vs. validation errors.
# [ ] Open practice/day_01_decision_tree.py in VS Code.
# [ ] Run it, change one input, and explain the prediction.
