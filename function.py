import csv
import json


def calculateTotalMacros(userData):
    totalProtein = userData['weight'] * \
        userData['proteinPerKilogramOfBodyWeight']
    totalLipid = userData['weight'] * 1
    macros = {
        'totalProtein': totalProtein,
        'totalLipid': totalLipid
    }
    return macros


def calculateBasalMetabolicRate(userData):
    activityLevelFactor = 1.2
    dietObjective = 0
    if userData['dietObjective'] == 'maintainWeight':
        dietObjective = 0
    if userData['dietObjective'] == 'loseWeight':
        dietObjective = -500
    if userData['dietObjective'] == 'gainWeight':
        dietObjective = 500
    if userData['activityLevel'] == 'sedentary':
        activityLevelFactor = 1.2
    if userData['activityLevel'] == 'lightlyActive':
        activityLevelFactor = 1.375
    if userData['activityLevel'] == 'moderatelyActive':
        activityLevelFactor = 1.55
    if userData['activityLevel'] == 'veryActive':
        activityLevelFactor = 1.725
    if userData['activityLevel'] == 'superActive':
        activityLevelFactor = 1.9
    if userData['gender'] == 'male':
        return (66.47 + (13.75 * userData['weight'])
                + (5.003 * userData['height'])
                - (6.755 * userData['age'])) * activityLevelFactor + dietObjective
    else:
        return (655.1 + (9.563 * userData['weight'])
                + (1.85 * userData['height'])
                - (4.676 * userData['age'])) * activityLevelFactor + dietObjective


totalProteinInMeal = 160
totalLipidInMeal = 80
totalCaloriesInMeal = 2500

totalProteinFirstMeal = totalProteinInMeal * 0.2
totalLipidFirstMeal = totalLipidInMeal * 0.2
totalCaloriesFirstMeal = totalCaloriesInMeal * 0.2

totalProteinSecondMeal = totalProteinInMeal * 0.3
totalLipidSecondMeal = totalLipidInMeal * 0.3
totalCaloriesInSecondMeal = totalCaloriesInMeal * 0.3

totalProteinThirdMeal = totalProteinInMeal * 0.2
totalLipidThirdMeal = totalLipidInMeal * 0.2
totalCaloriesInThirdMeal = totalCaloriesInMeal * 0.2

totalProteinInFourthMeal = 0
totalLipidInFourthMeal = 0
totalCaloriesInFourthMeal = 0

meal_number = 1


def calculateMeal(foodList, totalProtein, totalLipid, totalCaloriesInMeal):
    totalProteinGrams = 0
    proteinResult = 0
    totalLipidGrams = 0
    lipidResult = 0
    totalCarboGrams = 0
    carboResult = 0
    totalKcal = 0.0

    protein = next(
        (e for e in foodList if 'highProtein' in e and e['highProtein']), None)
    lipid = next(
        (e for e in foodList if 'highLipid' in e and e['highLipid']), None)
    carbo = next(
        (e for e in foodList if 'highCarb' in e and e['highCarb']), None)

    proteinPerGram = protein['protein'] / 100
    proteinKcalPerGram = protein['energyInKcal'] / 100
    proteinLipidPerGram = protein['lipid'] / 100
    proteinCarboPerGram = protein['carbohydrate'] / 100

    lipidPerGram = lipid['lipid'] / 100
    lipidKcalPerGram = lipid['energyInKcal'] / 100
    lipidProteinPerGram = lipid['protein'] / 100
    lipidCarboPerGram = lipid['carbohydrate'] / 100

    carboPerGram = carbo['carbohydrate'] / 100
    carboKcalPerGram = carbo['energyInKcal'] / 100
    carboLipidPerGram = carbo['lipid'] / 100
    carboProteinPerGram = carbo['protein'] / 100

    mealNumber = 1
    while totalKcal < totalCaloriesInMeal:
        if mealNumber == 1 and (protein['protein'] / protein['lipid'] < 2.4 or lipid['protein'] / lipid['lipid'] < 2.4):
            highFatMeal = totalCaloriesFirstMeal * 0.17
            totalGramsFromLipidSource = highFatMeal / lipidKcalPerGram
            while totalLipidGrams < totalGramsFromLipidSource:
                proteinResult += lipidProteinPerGram
                totalKcal += lipidKcalPerGram
                carboResult += lipidCarboPerGram
                lipidResult += lipidPerGram
                totalLipidGrams += 1
        while proteinResult < totalProtein:
            proteinResult += proteinPerGram
            totalKcal += proteinKcalPerGram
            carboResult += proteinCarboPerGram
            lipidResult += proteinLipidPerGram
            totalProteinGrams += 1
        if lipidResult < totalLipid:
            proteinResult += lipidProteinPerGram
            totalKcal += lipidKcalPerGram
            carboResult += lipidCarboPerGram
            lipidResult += lipidPerGram
            totalLipidGrams += 1
        if totalKcal >= totalCaloriesInMeal:
            while proteinResult < totalProtein or lipidResult > totalLipid:
                proteinResult -= lipidProteinPerGram
                totalKcal -= lipidKcalPerGram
                carboResult -= lipidCarboPerGram
                lipidResult -= lipidPerGram
                totalLipidGrams -= 1

                proteinResult += proteinPerGram
                totalKcal += proteinKcalPerGram
                carboResult += proteinCarboPerGram
                lipidResult += proteinLipidPerGram
                totalProteinGrams += 1

        if proteinResult > (totalProtein + (totalProtein * 0.03)):
            while proteinResult > (totalProtein + (totalProtein * 0.03)):
                proteinResult -= proteinPerGram
                totalKcal -= proteinKcalPerGram
                carboResult -= proteinCarboPerGram
                lipidResult -= proteinLipidPerGram
                totalProteinGrams -= 1

        proteinResult += carboProteinPerGram
        totalKcal += carboKcalPerGram
        carboResult += carboPerGram
        lipidResult += carboLipidPerGram
        totalCarboGrams += 1

    mealResult = {
        'totalKcal': totalKcal,
        'proteinSource': totalProteinGrams,
        'proteinSourceKcal': totalProteinGrams * proteinKcalPerGram,
        'lipidSource': totalLipidGrams,
        'lipidSourceKcal': totalLipidGrams * lipidKcalPerGram,
        'carboSource': totalCarboGrams,
        'carboSourceKcal': totalCarboGrams * carboKcalPerGram,
        'foods': foodList,
        'totalProteinInMeal': proteinResult,
        'totalLipidInMeal': lipidResult,
        'totalCarboInMeal': carboResult
    }
    mealNumber += 1
    return mealResult


userData = []


def calculateDietFourMeals(userData):

    firstMealResult = calculateMeal(
        userData['firstMealFoodList'], totalProteinFirstMeal, totalLipidFirstMeal, totalCaloriesFirstMeal)
    secondMealResult = calculateMeal(
        userData['secondMealFoodList'], totalProteinSecondMeal, totalLipidSecondMeal, totalCaloriesInSecondMeal)
    thirdMealResult = calculateMeal(
        userData['thirdMealFoodList'], totalProteinThirdMeal, totalLipidThirdMeal, totalCaloriesInThirdMeal)
    totalProteinInFourthMeal = totalProteinInMeal - \
        (firstMealResult["totalProteinInMeal"] +
         secondMealResult["totalProteinInMeal"] + thirdMealResult["totalProteinInMeal"])
    totalLipidInFourthMeal = totalLipidInMeal - \
        (firstMealResult["totalLipidInMeal"] +
         secondMealResult["totalLipidInMeal"] + thirdMealResult["totalLipidInMeal"])
    totalCaloriesInFourthMeal = totalCaloriesInMeal - \
        (firstMealResult["totalKcal"] +
         secondMealResult["totalKcal"] + thirdMealResult["totalKcal"])
    fourthMealResult = calculateMeal(
        userData['fourthMealFoodList'], totalProteinInFourthMeal, totalLipidInFourthMeal, totalCaloriesInFourthMeal)
    totalMacrosInDiet = {
        "totalCaloriesInDiet": (firstMealResult["totalKcal"] + secondMealResult["totalKcal"] + thirdMealResult["totalKcal"] + fourthMealResult["totalKcal"]),
        "totalProteinInDiet": (firstMealResult["totalProteinInMeal"] + secondMealResult["totalProteinInMeal"] + thirdMealResult["totalProteinInMeal"] + fourthMealResult["totalProteinInMeal"]),
        "totalLipidInDiet": (firstMealResult["totalLipidInMeal"] + secondMealResult["totalLipidInMeal"] + thirdMealResult["totalLipidInMeal"] + fourthMealResult["totalLipidInMeal"]),
        "totalCarboInDiet": (firstMealResult["totalCarboInMeal"] + secondMealResult["totalCarboInMeal"] + thirdMealResult["totalCarboInMeal"] + fourthMealResult["totalCarboInMeal"])
    }
    fullDiet = {
        "firstMealResult": firstMealResult,
        "secondMealResult": secondMealResult,
        "thirdMealResult": thirdMealResult,
        "fourthMealResult": fourthMealResult,
        "totalMacrosInDiet": totalMacrosInDiet
    }

    return fullDiet


with open('C:/projects/easy_diet_data/data_files/new_data_mock_to_regression.json', 'r', encoding="utf8") as input_file:
    userDataJson = json.load(input_file)

with open('C:/projects/easy_diet_data/data_files/user_data_result.csv', mode='w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(
        ['totalProteinIdealValue',
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

         'totalProteinCalculated',
         'totalCaloriesCalculated'
         ])
    for i in userDataJson:

        bmr = calculateBasalMetabolicRate(i)
        macros = calculateTotalMacros(i)
        totalProteinInMeal = macros['totalProtein']
        totalLipidInMeal = macros['totalLipid']
        totalCaloriesInMeal = bmr
        fullDiet = calculateDietFourMeals(i)
        totalPtnCalculated = fullDiet['totalMacrosInDiet']['totalProteinInDiet']
        isBigger = totalPtnCalculated > (totalProteinInMeal +
                                         (totalProteinInMeal * 0.05))
        isLower = totalPtnCalculated < (totalProteinInMeal -
                                        (totalProteinInMeal * 0.03))
        totalProteinIsOk = (isBigger == False and isLower == False)
        if (totalProteinIsOk):
            userData.append(fullDiet)
            with open('user_data__result_with_csv.json', 'w', encoding='utf-8') as output_file:
                json.dump(userData, output_file, ensure_ascii=False)
                # resultado para alimentar a IA
                writer.writerow([
                    totalProteinInMeal,
                    bmr,
                    fullDiet['firstMealResult']['proteinSource'],
                    fullDiet['firstMealResult']['proteinSourceKcal'],
                    fullDiet['firstMealResult']['lipidSource'],
                    fullDiet['firstMealResult']['lipidSourceKcal'],
                    fullDiet['firstMealResult']['carboSource'],
                    fullDiet['firstMealResult']['carboSourceKcal'],

                    fullDiet['secondMealResult']['proteinSource'],
                    fullDiet['secondMealResult']['proteinSourceKcal'],
                    fullDiet['secondMealResult']['lipidSource'],
                    fullDiet['secondMealResult']['lipidSourceKcal'],
                    fullDiet['secondMealResult']['carboSource'],
                    fullDiet['secondMealResult']['carboSourceKcal'],

                    fullDiet['thirdMealResult']['proteinSource'],
                    fullDiet['thirdMealResult']['proteinSourceKcal'],
                    fullDiet['thirdMealResult']['lipidSource'],
                    fullDiet['thirdMealResult']['lipidSourceKcal'],
                    fullDiet['thirdMealResult']['carboSource'],
                    fullDiet['thirdMealResult']['carboSourceKcal'],

                    fullDiet['fourthMealResult']['proteinSource'],
                    fullDiet['fourthMealResult']['proteinSourceKcal'],
                    fullDiet['fourthMealResult']['lipidSource'],
                    fullDiet['fourthMealResult']['lipidSourceKcal'],
                    fullDiet['fourthMealResult']['carboSource'],
                    fullDiet['fourthMealResult']['carboSourceKcal'],

                    fullDiet['totalMacrosInDiet']['totalProteinInDiet'],
                    fullDiet['totalMacrosInDiet']
                    ['totalCaloriesInDiet'],
                ])
