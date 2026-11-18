"""
Day 1 — My First Decision Tree Regressor

Goal:
Train a simple Decision Tree to predict house prices
using the number of bedrooms.
"""

# importing the braing model from sklearn library
from sklearn.tree import DecisionTreeRegressor

# training data
X = [[2], [3], [4], [5]]
y = [1.0, 1.2, 2.0, 2.2]

# making the model with only one branch depth
model = DecisionTreeRegressor(max_depth=1)

# triaining the model
model.fit(X, y)

# prediction 
rooms = int(input("enter number of rooms of specific house: "))

prediction = model.predict([[rooms]])

""" print the prediction NOTE: why did I right "prediction[0]"  not prediction directly? 
cause predict returns the value in a form of array so if I wrote "print(prediction) without using index property the result will be in the form of array not a direct number appears in the terminal"""

print(f"the house price is {prediction[0]}")


# =====================================================
# DAY 1 - WHAT I LEARNED
# =====================================================

# 1. DecisionTreeRegressor:
# A machine learning model used to predict numbers,
# such as house prices.

# 2. X and y:
# X contains the input features (number of bedrooms).
# y contains the correct house prices.

# 3. max_depth:
# It controls the maximum depth of the tree.
# With max_depth=1, the tree can make one split.

# 4. fit(X, y):
# This method trains the model using the given data.
# The tree searches for a split that reduces errors.

# 5. predict():
# This method makes predictions using the trained model.
# It returns a NumPy array, even for one house.

# 6. prediction[0]:
# It gets the first predicted value from the array.

# 7. Important limitation:
# This model uses only four houses and one feature.
# It is a learning example, not a real house-price model.

# =====================================================
# NEXT EXPERIMENTS
# =====================================================

# TODO: Change max_depth from 1 to 2.
# TODO: Compare the predictions.
# TODO: Learn how to evaluate a model on unseen data.


                          




