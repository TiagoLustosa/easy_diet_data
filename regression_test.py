import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_mock_CSV.csv')

dfResult = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_result.csv')

df_input = pd.concat([df, dfResult['totalCaloriesIdealValue']], axis=1)

X = df_input[['totalProteinIdealInAllMeals',
              'totalCaloriesIdealValue',
              'proteinSourceFirstMealFirstFoodProteinCoeficient',
              'proteinSourceFirstMealSecondFoodProteinCoeficient',
              'proteinSourceFirstMealThirdFoodProteinCoeficient',
              'proteinSourceFirstMealFirstFoodKcalCoeficient',
              'proteinSourceFirstMealSecondFoodKcalCoeficient',
              'proteinSourceFirstMealThirdFoodKcalCoeficient',

              'proteinSourceSecondMealFirstFoodProteinCoeficient',
              'proteinSourceSecondMealSecondFoodProteinCoeficient',
              'proteinSourceSecondMealThirdFoodProteinCoeficient',
              'proteinSourceSecondMealFirstFoodKcalCoeficient',
              'proteinSourceSecondMealSecondFoodKcalCoeficient',
              'proteinSourceSecondMealThirdFoodKcalCoeficient',

              'proteinSourceThirdMealFirstFoodProteinCoeficient',
              'proteinSourceThirdMealSecondFoodProteinCoeficient',
              'proteinSourceThirdMealThirdFoodProteinCoeficient',
              'proteinSourceThirdMealFirstFoodKcalCoeficient',
              'proteinSourceThirdMealSecondFoodKcalCoeficient',
              'proteinSourceThirdMealThirdFoodKcalCoeficient',

              'proteinSourceFourthMealFirstFoodProteinCoeficient',
              'proteinSourceFourthMealSecondFoodProteinCoeficient',
              'proteinSourceFourthMealThirdFoodProteinCoeficient',
              'proteinSourceFourthMealFirstFoodKcalCoeficient',
              'proteinSourceFourthMealSecondFoodKcalCoeficient',
              'proteinSourceFourthMealThirdFoodKcalCoeficient',
              ]]

y = dfResult[[
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

    'totalProteinCalculated',
    'totalCaloriesCalculated',
]]

model = LinearRegression().fit(X, y)

predict = model.predict(X)
concat_with_ideal = df_input[['totalProteinIdealInAllMeals', 'totalCaloriesIdealValue']]
dfFullResult = pd.DataFrame(columns=['totalProteinIdealInAllMeals',
                                     'totalProteinAllMeals',
                                     'totalCaloriesIdealValue',
                                     'totalCaloriesAllMeals',
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
                                     'fourthMealCarboFoodTotalGrams'])
for i in range(len(predict)):
    firstMealProteinFoodTotalGrams = predict[i][0]
    firstMealLipidFoodTotalGrams = predict[i][1]
    firstMealCarboFoodTotalGrams = predict[i][2]

    secondMealProteinFoodTotalGrams = predict[i][3]
    secondMealLipidFoodTotalGrams = predict[i][4]
    secondMealCarboFoodTotalGrams = predict[i][5]

    thirdMealProteinFoodTotalGrams = predict[i][6]
    thirdMealLipidFoodTotalGrams = predict[i][7]
    thirdMealCarboFoodTotalGrams = predict[i][8]

    fourthMealProteinFoodTotalGrams = predict[i][9]
    fourthMealLipidFoodTotalGrams = predict[i][10]
    fourthMealCarboFoodTotalGrams = predict[i][11]
    totalProteinAllMeals = predict[i][12]
    totalCaloriesAllMeals = predict[i][13]

    idealProtein = df_input[['totalProteinIdealInAllMeals']].to_numpy()
    idealCalories = df_input[['totalCaloriesIdealValue']].to_numpy()
    fullResult = {
        'totalProteinIdealInAllMeals': idealProtein[i],
        'totalProteinAllMeals': totalProteinAllMeals,
        'totalCaloriesIdealValue': idealCalories[i],
        'totalCaloriesAllMeals': totalCaloriesAllMeals,
        'firstMealProteinFoodTotalGrams': firstMealProteinFoodTotalGrams,
        'firstMealLipidFoodTotalGrams': firstMealLipidFoodTotalGrams,
        'firstMealCarboFoodTotalGrams': firstMealCarboFoodTotalGrams,
        'secondMealProteinFoodTotalGrams': secondMealProteinFoodTotalGrams,
        'secondMealLipidFoodTotalGrams': secondMealLipidFoodTotalGrams,
        'secondMealCarboFoodTotalGrams': secondMealCarboFoodTotalGrams,
        'thirdMealProteinFoodTotalGrams': thirdMealProteinFoodTotalGrams,
        'thirdMealLipidFoodTotalGrams': thirdMealLipidFoodTotalGrams,
        'thirdMealCarboFoodTotalGrams': thirdMealCarboFoodTotalGrams,
        'fourthMealProteinFoodTotalGrams': fourthMealProteinFoodTotalGrams,
        'fourthMealLipidFoodTotalGrams': fourthMealLipidFoodTotalGrams,
        'fourthMealCarboFoodTotalGrams': fourthMealCarboFoodTotalGrams,

    }
    new_df_result = pd.DataFrame(fullResult)
    dfFullResult = pd.concat([dfFullResult, new_df_result], ignore_index=True)
    dfFullResult.to_csv('full_result_predict.csv', index=False)
    print('Dados preditos = ', i)
