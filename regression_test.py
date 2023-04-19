import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

dfTESTE = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_mock_CSV11.csv')

dfResultTESTE = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_result11.csv')

df = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_mock_CSV.csv')
df2 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_mock_CSV2.csv')
df3 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_mock_CSV3.csv')
df4 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_mock_CSV4.csv')
df5 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_mock_CSV5.csv')
df6 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_mock_CSV6.csv')
df7 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_mock_CSV7.csv')
df8 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_mock_CSV8.csv')
df9 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_mock_CSV9.csv')
df10 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_mock_CSV10.csv')


dfResult = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_result.csv')

dfResult2 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_result2.csv')

dfResult3 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_result3.csv')

dfResult4 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_result4.csv')

dfResult5 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_result5.csv')

dfResult6 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_result6.csv')

dfResult7 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_result7.csv')

dfResult8 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_result8.csv')

dfResult9 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_result9.csv')

dfResult10 = pd.read_csv(
    'C:/projects/easy_diet_data/data_files/user_data_result10.csv')


dfAllFiles = pd.concat([df, df2, df3, df4, df5, df6, df7, df8, df9, df10])

dfResultAllFiles = pd.concat([dfResult, dfResult2, dfResult3, dfResult4, dfResult5, dfResult6, dfResult7, dfResult8, dfResult9, dfResult10])

print(len(dfAllFiles), len(dfResultAllFiles))

# df_input = pd.concat([dfAllFiles, dfResultAllFiles[['totalCaloriesIdealValue', 'totalLipidIdealValue']]], axis=1)
df_input = pd.concat([dfTESTE, dfResultTESTE[['totalCaloriesIdealValue', 'totalLipidIdealValue']]], axis=1)

df_input[['proteinSourceFirstMealFirstFoodProteinCoeficient',
          'proteinSourceFirstMealSecondFoodProteinCoeficient',
          'proteinSourceFirstMealThirdFoodProteinCoeficient',
          'proteinSourceFirstMealFirstFoodLipidCoeficient',
          'proteinSourceFirstMealSecondFoodLipidCoeficient',
          'proteinSourceFirstMealThirdFoodLipidCoeficient',
          'proteinSourceFirstMealFirstFoodKcalCoeficient',
          'proteinSourceFirstMealSecondFoodKcalCoeficient',
          'proteinSourceFirstMealThirdFoodKcalCoeficient',

          'proteinSourceSecondMealFirstFoodProteinCoeficient',
          'proteinSourceSecondMealSecondFoodProteinCoeficient',
          'proteinSourceSecondMealThirdFoodProteinCoeficient',
          'proteinSourceSecondMealFirstFoodLipidCoeficient',
          'proteinSourceSecondMealSecondFoodLipidCoeficient',
          'proteinSourceSecondMealThirdFoodLipidCoeficient',
          'proteinSourceSecondMealFirstFoodKcalCoeficient',
          'proteinSourceSecondMealSecondFoodKcalCoeficient',
          'proteinSourceSecondMealThirdFoodKcalCoeficient',

          'proteinSourceThirdMealFirstFoodProteinCoeficient',
          'proteinSourceThirdMealSecondFoodProteinCoeficient',
          'proteinSourceThirdMealThirdFoodProteinCoeficient',
          'proteinSourceThirdMealFirstFoodLipidCoeficient',
          'proteinSourceThirdMealSecondFoodLipidCoeficient',
          'proteinSourceThirdMealThirdFoodLipidCoeficient',
          'proteinSourceThirdMealFirstFoodKcalCoeficient',
          'proteinSourceThirdMealSecondFoodKcalCoeficient',
          'proteinSourceThirdMealThirdFoodKcalCoeficient',

          'proteinSourceFourthMealFirstFoodProteinCoeficient',
          'proteinSourceFourthMealSecondFoodProteinCoeficient',
          'proteinSourceFourthMealThirdFoodProteinCoeficient',
          'proteinSourceFourthMealFirstFoodLipidCoeficient',
          'proteinSourceFourthMealSecondFoodLipidCoeficient',
          'proteinSourceFourthMealThirdFoodLipidCoeficient',
          'proteinSourceFourthMealFirstFoodKcalCoeficient',
          'proteinSourceFourthMealSecondFoodKcalCoeficient',
          'proteinSourceFourthMealThirdFoodKcalCoeficient']] = df_input[['proteinSourceFirstMealFirstFoodProteinCoeficient',
                                                                         'proteinSourceFirstMealSecondFoodProteinCoeficient',
                                                                         'proteinSourceFirstMealThirdFoodProteinCoeficient',
                                                                         'proteinSourceFirstMealFirstFoodLipidCoeficient',
                                                                         'proteinSourceFirstMealSecondFoodLipidCoeficient',
                                                                         'proteinSourceFirstMealThirdFoodLipidCoeficient',
                                                                         'proteinSourceFirstMealFirstFoodKcalCoeficient',
                                                                         'proteinSourceFirstMealSecondFoodKcalCoeficient',
                                                                         'proteinSourceFirstMealThirdFoodKcalCoeficient',

                                                                         'proteinSourceSecondMealFirstFoodProteinCoeficient',
                                                                         'proteinSourceSecondMealSecondFoodProteinCoeficient',
                                                                         'proteinSourceSecondMealThirdFoodProteinCoeficient',
                                                                         'proteinSourceSecondMealFirstFoodLipidCoeficient',
                                                                         'proteinSourceSecondMealSecondFoodLipidCoeficient',
                                                                         'proteinSourceSecondMealThirdFoodLipidCoeficient',
                                                                         'proteinSourceSecondMealFirstFoodKcalCoeficient',
                                                                         'proteinSourceSecondMealSecondFoodKcalCoeficient',
                                                                         'proteinSourceSecondMealThirdFoodKcalCoeficient',

                                                                         'proteinSourceThirdMealFirstFoodProteinCoeficient',
                                                                         'proteinSourceThirdMealSecondFoodProteinCoeficient',
                                                                         'proteinSourceThirdMealThirdFoodProteinCoeficient',
                                                                         'proteinSourceThirdMealFirstFoodLipidCoeficient',
                                                                         'proteinSourceThirdMealSecondFoodLipidCoeficient',
                                                                         'proteinSourceThirdMealThirdFoodLipidCoeficient',
                                                                         'proteinSourceThirdMealFirstFoodKcalCoeficient',
                                                                         'proteinSourceThirdMealSecondFoodKcalCoeficient',
                                                                         'proteinSourceThirdMealThirdFoodKcalCoeficient',

                                                                         'proteinSourceFourthMealFirstFoodProteinCoeficient',
                                                                         'proteinSourceFourthMealSecondFoodProteinCoeficient',
                                                                         'proteinSourceFourthMealThirdFoodProteinCoeficient',
                                                                         'proteinSourceFourthMealFirstFoodLipidCoeficient',
                                                                         'proteinSourceFourthMealSecondFoodLipidCoeficient',
                                                                         'proteinSourceFourthMealThirdFoodLipidCoeficient',
                                                                         'proteinSourceFourthMealFirstFoodKcalCoeficient',
                                                                         'proteinSourceFourthMealSecondFoodKcalCoeficient',
                                                                         'proteinSourceFourthMealThirdFoodKcalCoeficient']] / 100
X = df_input[['totalProteinIdealInAllMeals',
              'totalLipidIdealValue',
              'totalCaloriesIdealValue',
              'proteinSourceFirstMealFirstFoodProteinCoeficient',
              'proteinSourceFirstMealSecondFoodProteinCoeficient',
              'proteinSourceFirstMealThirdFoodProteinCoeficient',
              'proteinSourceFirstMealFirstFoodLipidCoeficient',
              'proteinSourceFirstMealSecondFoodLipidCoeficient',
              'proteinSourceFirstMealThirdFoodLipidCoeficient',
              'proteinSourceFirstMealFirstFoodKcalCoeficient',
              'proteinSourceFirstMealSecondFoodKcalCoeficient',
              'proteinSourceFirstMealThirdFoodKcalCoeficient',

              'proteinSourceSecondMealFirstFoodProteinCoeficient',
              'proteinSourceSecondMealSecondFoodProteinCoeficient',
              'proteinSourceSecondMealThirdFoodProteinCoeficient',
              'proteinSourceSecondMealFirstFoodLipidCoeficient',
              'proteinSourceSecondMealSecondFoodLipidCoeficient',
              'proteinSourceSecondMealThirdFoodLipidCoeficient',
              'proteinSourceSecondMealFirstFoodKcalCoeficient',
              'proteinSourceSecondMealSecondFoodKcalCoeficient',
              'proteinSourceSecondMealThirdFoodKcalCoeficient',

              'proteinSourceThirdMealFirstFoodProteinCoeficient',
              'proteinSourceThirdMealSecondFoodProteinCoeficient',
              'proteinSourceThirdMealThirdFoodProteinCoeficient',
              'proteinSourceThirdMealFirstFoodLipidCoeficient',
              'proteinSourceThirdMealSecondFoodLipidCoeficient',
              'proteinSourceThirdMealThirdFoodLipidCoeficient',
              'proteinSourceThirdMealFirstFoodKcalCoeficient',
              'proteinSourceThirdMealSecondFoodKcalCoeficient',
              'proteinSourceThirdMealThirdFoodKcalCoeficient',

              'proteinSourceFourthMealFirstFoodProteinCoeficient',
              'proteinSourceFourthMealSecondFoodProteinCoeficient',
              'proteinSourceFourthMealThirdFoodProteinCoeficient',
              'proteinSourceFourthMealFirstFoodLipidCoeficient',
              'proteinSourceFourthMealSecondFoodLipidCoeficient',
              'proteinSourceFourthMealThirdFoodLipidCoeficient',
              'proteinSourceFourthMealFirstFoodKcalCoeficient',
              'proteinSourceFourthMealSecondFoodKcalCoeficient',
              'proteinSourceFourthMealThirdFoodKcalCoeficient',
              ]]

y = dfResultTESTE[[
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
    'totalLipidCalculated',
    'totalCaloriesCalculated',
]]

model = LinearRegression().fit(X, y)

predict = model.predict(X)
concat_with_ideal = df_input[['totalProteinIdealInAllMeals', 'totalCaloriesIdealValue']]
dfFullResult = pd.DataFrame(columns=['totalProteinIdealInAllMeals',
                                     'totalProteinAllMeals',
                                     'totalLipidIdealInAllMeals',
                                     'totalLipidAllMeals',
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
    totalLipidAllMeals = predict[i][13]
    totalCaloriesAllMeals = predict[i][14]

    idealProtein = df_input[['totalProteinIdealInAllMeals']].to_numpy()
    idealLipid = df_input[['totalLipidIdealValue']].to_numpy()
    idealCalories = df_input[['totalCaloriesIdealValue']].to_numpy()
    fullResult = {
        'totalProteinIdealInAllMeals': idealProtein[i],
        'totalProteinAllMeals': totalProteinAllMeals,
        'totalLipidIdealInAllMeals': idealLipid[i],
        'totalLipidAllMeals': totalLipidAllMeals,
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
    dfFullResult.to_csv('full_result_predictTESTE.csv', index=False)
    print('Dados preditos = ', i)
