import numpy as np
from sklearn.linear_model import LinearRegression

# Define the training data
# Each row represents a meal containing chicken and lentils in grams
X_train = np.array([[600, 0], [400, 278], [300, 400], [450, 250], [500, 100]])
y_train = np.array([150, 140, 130, 120, 110])

# Define the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Define the target protein value
target_protein = 150
target_calories = 2000

# Calculate the quantities of chicken and lentils needed to achieve the target protein value
predict = model.predict(
    [[target_protein, target_calories]])


print("Chicken quantity: ", predict[0])

print("Lentils quantity: ", predict[1])

# import numpy as np
# from sklearn.linear_model import LinearRegression

# Define the data
# X = np.array([[31, 9]])  # chicken and lentils
# y = np.array([150])  # target protein

# Train the model
# model = LinearRegression().fit(X, y)

# Get the coefficients and intercept
# coefs = model.coef_.item()
# intercept = model.intercept_.item()

# Calculate the quantities
# chicken = (150 - intercept) / coefs[0]
# lentils = (150 - intercept) / coefs[1]

# Print the results
# print("Chicken quantity: ", chicken)
# print("Lentils quantity: ", lentils)
