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
]]

model = LinearRegression().fit(X, y)
X_row = X.iloc[0].values.reshape(1, -1)

# Calculate the quantities X[0] pega a entrada do primeiro grupo do X
predict = model.predict(X_row)

firstMealProteinSourceGrams = predict[0]
