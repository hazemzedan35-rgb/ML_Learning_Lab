"""Day 1 practice starter — NOT marked as completed.

Goal: see a Decision Tree learn a split from simple house-price data.
Run this in the next learning session after reviewing the notes.
"""

from sklearn.tree import DecisionTreeRegressor


# Features: number of bedrooms (each row has one feature).
X = [[2], [3], [4], [5]]

# Targets: house prices, in millions.
y = [1.0, 1.2, 2.0, 2.2]

# Limit the tree to one split, so the result is easy to explain.
model = DecisionTreeRegressor(max_depth=1, random_state=42)

# Fit the model to the known examples.
model.fit(X, y)

# Ask for a prediction for a 5-bedroom house.
prediction = model.predict([[5]])[0]
print(f"Predicted price for 5 bedrooms: {prediction:.1f} million")

# NEXT SESSION CHALLENGES (do them yourself):
# TODO 1: Change [[5]] to [[2]]. What happens, and why?
# TODO 2: Change max_depth to 2. What changes for the 5-bedroom house?
# TODO 3: Explain the difference between training error and
#         validation error before adding a model evaluation step.
