import json
import random
import numpy as np
import csv

ages = list(range(18, 75))  # possible ages from 18 to 60
weights = list(range(45, 140))  # possible weights from 50 to 100 kg
heights = list(range(150, 210))  # possible heights in cm
protein_per_kg = [1.6, 1.7, 1.8, 1.9, 2.0,  2.1, 2.2, 2.3]
activity_levels = ['sedentary', 'lightlyActive', 'moderatelyActive',
                   'veryActive', 'superActive']  # possible activity levels
genders = ['male', 'female']  # possible genders
diet_objectives = ['maintainWeight', 'loseWeight',
                   'gainWeight']  # possible diet objectives


def load_food_lists():
    with open("foodlist.json") as f:
        food_list = json.load(f)
    return food_list


def generate_user_data():
    mock_user_data = []
    with open('C:/projects/easy_diet_data/data_files/user_data_mock_CSV2.csv', mode='w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['totalProteinIdealInAllMeals',
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
                         ])
        for i in range(1000):
            food_list = load_food_lists()

        # generate random user data
            age = random.choice(ages)
            weight = random.choice(weights)
            height = random.choice(heights)
            activity_level = random.choice(activity_levels)
            gender = random.choice(genders)
            diet_objective = random.choice(diet_objectives)
            proteinPerKilogramOfBodyWeight = random.choice(
                protein_per_kg)

            # create meal food lists
            first_meal_food_list = random.sample(
                [food for food in food_list if food.get('highProtein')], 1)
            first_meal_food_list += random.sample(
                [food for food in food_list if food.get('highLipid')], 1)
            first_meal_food_list += random.sample(
                [food for food in food_list if food.get('highCarb')], 1)

            second_meal_food_list = random.sample(
                [food for food in food_list if food.get('highProtein')], 1)
            second_meal_food_list += random.sample(
                [food for food in food_list if food.get('highLipid')], 1)
            second_meal_food_list += random.sample(
                [food for food in food_list if food.get('highCarb')], 1)

            third_meal_food_list = random.sample(
                [food for food in food_list if food.get('highProtein')], 1)
            third_meal_food_list += random.sample(
                [food for food in food_list if food.get('highLipid')], 1)
            third_meal_food_list += random.sample(
                [food for food in food_list if food.get('highCarb')], 1)

            fourth_meal_food_list = random.sample(
                [food for food in food_list if food.get('highProtein')], 1)
            fourth_meal_food_list += random.sample(
                [food for food in food_list if food.get('highLipid')], 1)
            fourth_meal_food_list += random.sample(
                [food for food in food_list if food.get('highCarb')], 1)

            # create user data dictionary

            totalProteinIdealInAllMeals = weight * proteinPerKilogramOfBodyWeight
            # get foods from first meal
            proteinSourceFirstMealFirstFoodProteinCoeficient = first_meal_food_list[0]['protein']
            proteinSourceFirstMealSecondFoodProteinCoeficient = first_meal_food_list[1]['protein']
            proteinSourceFirstMealThirdFoodProteinCoeficient = first_meal_food_list[2]['protein']

            proteinSourceFirstMealFirstFoodKcalCoeficient = first_meal_food_list[0]['energyInKcal']
            proteinSourceFirstMealSecondFoodKcalCoeficient = first_meal_food_list[1]['energyInKcal']
            proteinSourceFirstMealThirdFoodKcalCoeficient = first_meal_food_list[2]['energyInKcal']
            # get foods from second meal
            proteinSourceSecondMealFirstFoodProteinCoeficient = second_meal_food_list[0]['protein']
            proteinSourceSecondMealSecondFoodProteinCoeficient = second_meal_food_list[1]['protein']
            proteinSourceSecondMealThirdFoodProteinCoeficient = second_meal_food_list[2]['protein']

            proteinSourceSecondMealFirstFoodKcalCoeficient = second_meal_food_list[0]['energyInKcal']
            proteinSourceSecondMealSecondFoodKcalCoeficient = second_meal_food_list[1]['energyInKcal']
            proteinSourceSecondMealThirdFoodKcalCoeficient = second_meal_food_list[2]['energyInKcal']
            # get foods from third meal
            proteinSourceThirdMealFirstFoodProteinCoeficient = third_meal_food_list[0]['protein']
            proteinSourceThirdMealSecondFoodProteinCoeficient = third_meal_food_list[1]['protein']
            proteinSourceThirdMealThirdFoodProteinCoeficient = third_meal_food_list[2]['protein']
            proteinSourceThirdMealFirstFoodKcalCoeficient = third_meal_food_list[0]['energyInKcal']
            proteinSourceThirdMealSecondFoodKcalCoeficient = third_meal_food_list[1]['energyInKcal']
            proteinSourceThirdMealThirdFoodKcalCoeficient = third_meal_food_list[2]['energyInKcal']
            # get foods from fourth meal
            proteinSourceFourthMealFirstFoodProteinCoeficient = fourth_meal_food_list[0]['protein']
            proteinSourceFourthMealSecondFoodProteinCoeficient = fourth_meal_food_list[1]['protein']
            proteinSourceFourthMealThirdFoodProteinCoeficient = fourth_meal_food_list[2]['protein']
            proteinSourceFourthMealFirstFoodKcalCoeficient = fourth_meal_food_list[0]['energyInKcal']
            proteinSourceFourthMealSecondFoodKcalCoeficient = fourth_meal_food_list[1]['energyInKcal']
            proteinSourceFourthMealThirdFoodKcalCoeficient = fourth_meal_food_list[2]['energyInKcal']

            writer.writerow([totalProteinIdealInAllMeals,
                             proteinSourceFirstMealFirstFoodProteinCoeficient,
                             proteinSourceFirstMealSecondFoodProteinCoeficient,
                             proteinSourceFirstMealThirdFoodProteinCoeficient,
                             proteinSourceFirstMealFirstFoodKcalCoeficient,
                             proteinSourceFirstMealSecondFoodKcalCoeficient,
                             proteinSourceFirstMealThirdFoodKcalCoeficient,

                             proteinSourceSecondMealFirstFoodProteinCoeficient,
                             proteinSourceSecondMealSecondFoodProteinCoeficient,
                             proteinSourceSecondMealThirdFoodProteinCoeficient,
                             proteinSourceSecondMealFirstFoodKcalCoeficient,
                             proteinSourceSecondMealSecondFoodKcalCoeficient,
                             proteinSourceSecondMealThirdFoodKcalCoeficient,

                             proteinSourceThirdMealFirstFoodProteinCoeficient,
                             proteinSourceThirdMealSecondFoodProteinCoeficient,
                             proteinSourceThirdMealThirdFoodProteinCoeficient,
                             proteinSourceThirdMealFirstFoodKcalCoeficient,
                             proteinSourceThirdMealSecondFoodKcalCoeficient,
                             proteinSourceThirdMealThirdFoodKcalCoeficient,

                             proteinSourceFourthMealFirstFoodProteinCoeficient,
                             proteinSourceFourthMealSecondFoodProteinCoeficient,
                             proteinSourceFourthMealThirdFoodProteinCoeficient,
                             proteinSourceFourthMealFirstFoodKcalCoeficient,
                             proteinSourceFourthMealSecondFoodKcalCoeficient,
                             proteinSourceFourthMealThirdFoodKcalCoeficient,
                             ])

            mock_user_data.append({
                "age": age,
                "weight": weight,
                "height": height,
                "activityLevel": activity_level,
                "gender": gender,
                "proteinPerKilogramOfBodyWeight": proteinPerKilogramOfBodyWeight,
                "dietObjective": diet_objective,
                "firstMealFoodList": first_meal_food_list,
                "secondMealFoodList": second_meal_food_list,
                "thirdMealFoodList": third_meal_food_list,
                "fourthMealFoodList": fourth_meal_food_list,
            })
            with open('C:/projects/easy_diet_data/data_files/new_data_mock_to_regression2.json', 'w', encoding='utf-8') as output_file:
                json.dump(mock_user_data, output_file, ensure_ascii=False)
            print('Dados criados = ', i)

            # print("Current length of output_arr:", len(mock_user_data))
#             return user_data
generate_user_data()
# # exam    ple usage
# user_data = generate_user_data()
# print(user_data)

# Create a list of 100 mock userData objects with random values for each attribute
# mock_user_data = []
# for i in range(100):
#     age = random.choice(ages)
#     weight = random.choice(weights)
#     height = random.choice(heights)
#     activity_level = random.choice(activity_levels)
#     gender = random.choice(genders)
#     diet_objective = random.choice(diet_objectives)
#     mock_user_data.append({
#         'age': age,
#         'weight': weight,
#         'height': height,
#         'activityLevel': activity_level,
#         'gender': gender,
#         'dietObjective': diet_objective
#     })

#     with open('user_data.json', 'w', encoding='utf-8') as output_file:
#         json.dump(mock_user_data, output_file, ensure_ascii=False)
#     print(mock_user_data)
#     print("Current length of output_arr:", len(mock_user_data))
