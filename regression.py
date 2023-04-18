import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# X = np.array([[totalproteina, totalcaloria, ptnPrimeiroAlimento, caloriaPrimeiroAlimento, ptnSegundoALimneto, caloriaSegundoAlimneto, ptnTerceiroAlimento, caloriaTerceiroAlimento][[totalproteina, totalcaloria, ptnPrimeiroAlimento,
#              caloriaPrimeiroAlimento, ptnSegundoALimneto, caloriaSegundoAlimneto, ptnTerceiroAlimento, caloriaTerceiroAlimento]]])  # datasetinteiro tem que ser esse array aqui foods, totalptn calorias vai ser um array gigante
# y = np.array([140])  # output quantidade gramas por alimento por refeicao
# Define the linear regression model

df = pd.read_csv('C:/projects/easy_diet_data/data_files/user_data_result.csv')
# 'totalProteinIdealValue'
# 'totalCaloriesIdealValue'
# 'firstMealProteinFoodTotalGrams'
# 'firstMealProteinFoodTotalKcal'
# 'firstMealLipidFoodTotalGrams'
# 'firstMealLipidFoodTotalKcal'
# 'firstMealCarboFoodTotalGrams'
# 'firstMealCarboFoodTotalKcal'
# 'secondMealProteinFoodTotalGrams'
# 'secondMealProteinFoodTotalKcal'
# 'secondMealLipidFoodTotalGrams'
# 'secondMealLipidFoodTotalKcal'
# 'secondMealCarboFoodTotalGrams'
# 'secondMealCarboFoodTotalKcal'
# 'thirdMealProteinFoodTotalGrams'
# 'thirdMealProteinFoodTotalKcal'
# 'thirdMealLipidFoodTotalGrams'
# 'thirdMealLipidFoodTotalKcal'
# 'thirdMealCarboFoodTotalGrams'
# 'thirdMealCarboFoodTotalKcal'
# 'fourthMealProteinFoodTotalGrams'
# 'fourthMealProteinFoodTotalKcal'
# 'fourthMealLipidFoodTotalGrams'
# 'fourthMealLipidFoodTotalKcal'
# 'fourthMealCarboFoodTotalGrams'
# 'fourthMealCarboFoodTotalKcal'
# 'totalProteinCalculated'
# 'totalCaloriesCalculated'
X = df[['totalProteinIdealValue',
        'totalCaloriesIdealValue',
        'firstMealProteinFoodTotalGrams',
        'firstMealProteinFoodTotalKcal',
        'firstMealLipidFoodTotalGrams',
        'firstMealLipidFoodTotalKcal',
        'firstMealCarboFoodTotalGrams',
        'firstMealCarboFoodTotalKcal',
        'secondMealProteinFoodTotalGrams',
        'secondMealProteinFoodTotalKcal',
        'secondMealLipidFoodTotalGrams',
        'secondMealLipidFoodTotalKcal',
        'secondMealCarboFoodTotalGrams',
        'secondMealCarboFoodTotalKcal',
        'thirdMealProteinFoodTotalGrams',
        'thirdMealProteinFoodTotalKcal',
        'thirdMealLipidFoodTotalGrams',
        'thirdMealLipidFoodTotalKcal',
        'thirdMealCarboFoodTotalGrams',
        'thirdMealCarboFoodTotalKcal',
        'fourthMealProteinFoodTotalGrams',
        'fourthMealProteinFoodTotalKcal',
        'fourthMealLipidFoodTotalGrams',
        'fourthMealLipidFoodTotalKcal',
        'fourthMealCarboFoodTotalGrams',
        'fourthMealCarboFoodTotalKcal',
        ]]

y = df[[
    'firstMealProteinFoodTotalGrams',
    'firstMealLipidFoodTotalGrams',
    'firstMealCarboFoodTotalGrams',
    'secondMealProteinFoodTotalGrams',
    'secondMealLipidFoodTotalGrams',
    'secondMealCarboFoodTotalGrams',
    'thirdMealProteinFoodTotalGrams',
    'thirdMealLipidFoodTotalGrams',
    'thirdMealCarboFoodTotalGrams',
    'fourthMealProteinFoodTotalGrams',
    'fourthMealLipidFoodTotalGrams',
    'fourthMealCarboFoodTotalGrams',
]]

model = LinearRegression().fit(X, y)
X_row = X.iloc[0].values.reshape(1, -1)

# Calculate the quantities X[0] pega a entrada do primeiro grupo do X
predict = model.predict(X)

predict = model.predict(X)

for i in range(len(predict)):
    firstMealProteinFoodTotalGrams = predict[i][0]
    firstMealLipidFoodTotalGrams = predict[i][1]
    firstMealCarboFoodTotalGrams = predict[i][2]

    # You can then use these predicted values as desired
    # For example, print them to the console
    print("Predicted values for row", i, ":")
    print("First Meal Protein Food Total Grams:",
          firstMealProteinFoodTotalGrams)
    print("First Meal Lipid Food Total Grams:", firstMealLipidFoodTotalGrams)
    print("First Meal Carbo Food Total Grams:", firstMealCarboFoodTotalGrams)


# for i in predict:
#     firstMealProteinFoodTotalGrams = predict[0]
#     firstMealLipidFoodTotalGrams = predict[1]
#     firstMealCarboFoodTotalGrams = predict[i, 2]
#     secondMealProteinFoodTotalGrams = predict[i, 4]
#     secondMealLipidFoodTotalGrams = predict[i, 5]
#     secondMealCarboFoodTotalGrams = predict[i, 6]
#     thirdMealProteinFoodTotalGrams = predict[i, 7]
#     thirdMealLipidFoodTotalGrams = predict[i, 8]
#     thirdMealCarboFoodTotalGrams = predict[i, 9]
#     fourthMealProteinFoodTotalGrams = predict[i, 10]
#     fourthMealLipidFoodTotalGrams = predict[i, 11]
#     fourthMealCarboFoodTotalGrams = predict[i, 12]

#     firstMeal = {
#         'firstMealProteinFoodTotalGrams': firstMealProteinFoodTotalGrams,
#         'firstMealLipidFoodTotalGrams': firstMealLipidFoodTotalGrams,
#         'firstMealCarboFoodTotalGrams': firstMealCarboFoodTotalGrams,
#     }

#     secondMeal = {
#         'secondMealProteinFoodTotalGrams': secondMealProteinFoodTotalGrams,
#         'secondMealLipidFoodTotalGrams': secondMealLipidFoodTotalGrams,
#         'secondMealCarboFoodTotalGrams': secondMealCarboFoodTotalGrams,
#     }

#     thirdMeal = {
#         'thirdMealProteinFoodTotalGrams': thirdMealProteinFoodTotalGrams,
#         'thirdMealLipidFoodTotalGrams': thirdMealLipidFoodTotalGrams,
#         'thirdMealCarboFoodTotalGrams': thirdMealCarboFoodTotalGrams,
#     }
#     fourthMeal = {
#         'fourthMealProteinFoodTotalGrams': fourthMealProteinFoodTotalGrams,
#         'fourthMealLipidFoodTotalGrams': fourthMealLipidFoodTotalGrams,
#         'fourthMealCarboFoodTotalGrams': fourthMealCarboFoodTotalGrams,
#     }
#     print(firstMeal)
