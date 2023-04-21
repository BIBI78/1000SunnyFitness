import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import requests
import json
import random
import time 
from math import ceil



#USER INFO
# I have editted this function over and over 
#This should prompt the user to re-enter their information if they input an age over 150, a height over 251 cm, or a weight over 635 kg.

def ask_user_info():
    print("WELCOME TO 1000 SUNNY FITNESS \n")
    name = input("What's your name?\n")

    user_info = {"name": name}

    #########



    while True:
        workout_plan = input("Would you like a workout plan? (yes or no): ")
        if workout_plan.lower() == "yes":
            user_info["workout_plan"] = suggest_workout_plan()
            workout_types = user_info["workout_plan"]
            options = {type: suggest_workout_options([type])[0] for type in workout_types}
            user_info["weekly_schedule"] = suggest_weekly_schedule(options) 
            break
        elif workout_plan.lower() == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")


    while True:
        food_plan = input("Would you like a food plan? (yes or no): ")
        if food_plan.lower() == "yes":
            food_types = suggest_food_plan()
            options = {type: suggest_food_options([type])[0] for type in food_types}
            user_info["food_plan"] = food_types
            user_info["weekly_schedule"] = suggest_weekly_food_schedule(options)
            break
        elif food_plan.lower() == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")

    return user_info



#1
# I suggest exercises 
# i should rename this function , this actually jsut suggest 3 exercise types
def suggest_workout_plan():
    # this is where i create an empty list for exercises 
    exercises = []
    # also a list  of options 
    options = ["cardio", "weight lifting", "home workout"]
    # this is my loop , asking the user to choose exercises up to 3, because thats how many i have in the options 
    while len(exercises) < 3:
        exercise = input("What exercises would you like to do? (Enter one or more, separated by commas): cardio, weight lifting, home workout\n")
        # I use the split fucntion  to split the list by commas
        for choice in exercise.split(','):
            choice = choice.strip().lower()
            if choice in options:
                if choice not in exercises:
                    # this is me add thier choice to the empty list options 
                    exercises.append(choice)
                    if len(exercises) == 3:
                        break
            else:
                print("Sorry please choose from the options: cardio, weight lifting, home workout.")
        if len(exercises) < 3:
            # this more_exercises idea is not mine
            more_exercises = input("Would you like to add any other exercises? (yes or no)\n")
            if more_exercises.lower() == "no":
                break
            elif more_exercises.lower() == "yes":
                print("Here are the remaining exercises you can still choose from: ")
                for option in options:
                    if option not in exercises:
                        print(option)
                continue
            else:
                print("Please enter 'yes' or 'no'.")
                continue
    if len(exercises) == 3:
        # aight
        print("You have chosen all 3.")
    print(f" This is what you have chosen: {', '.join(exercises)}")
    return exercises
#2
# I suggest exercise types 
def suggest_workout_options(workout_types):
    # this is my workout options, it takes the argument WORKOUT_TYPES
    # options is a dictionary mapping each workout type to a list of exercises 
    options = {
        "cardio": ["hiking", "long distance running", "boxing", "walking"],
        "weight lifting": ["bench press", "dumbbell press", "dead lift", "leg press", "squat", "pull up"],
        "home workout": ["push ups", "sit ups", "squats", "jump rope", "crunches", "v ups"]
    }
    # empty list with the users chosen options 
    chosen_options = []
    # for loop on the argument ??? each type in workout ???
    for workout_type in workout_types:
        # print and ask user which workouts and their number 
        print(f"Which {workout_type} exercises would you like to include in your workout? (enter numbers separated by commas please)")
        exercises = options[workout_type]
        # this part is not mine, got help from a friend, try to rewrite this in my own way.!!!
        for i, exercise in enumerate(exercises):
            # pirnting numbered list
            print(f"{i + 1}. {exercise}")
            #user input
        chosen = input()
        chosen_exercises = []
        #validates user input, in a very complicated way
        while not chosen.replace(',', '').isnumeric() or max([int(num) for num in chosen.split(",")]) > len(exercises) or min([int(num) for num in chosen.split(",")]) < 1:
            print("Invalid input. Please enter the numbers of the exercises you would like to include (comma-separated please!!!).")
            for i, exercise in enumerate(exercises):
                print(f"{i + 1}. {exercise}")
            chosen = input()
        chosen_exercises = [exercises[int(num) - 1] for num in chosen.split(",")]
        chosen_options.append(chosen_exercises)
    return chosen_options

#3
# I suggest a weekly scheudle 
def suggest_weekly_schedule(options):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    workout_days = input("How many days a week would you like to work out? (1-7)\n")
    while workout_days.isdigit() == False or int(workout_days) < 1 or int(workout_days) > 7:
        workout_days = input("Invalid input. How many days a week would you like to work out? (1-7)\n")
    workout_days = int(workout_days)
    
    all_exercises = []
    for exercise_list in options.values():
        all_exercises.extend(exercise_list)
        
    weekly_schedule = {}
    for day in days_of_week:
        if workout_days == 0:
            break
        random.shuffle(all_exercises)
        workout_plan = ", ".join(random.sample(all_exercises, random.randint(1, len(all_exercises))))
        weekly_schedule[day] = workout_plan
        workout_days -= 1
    print("Here's your weekly workout schedule:")
    for day, plan in weekly_schedule.items():
        print(f"{day}: {plan}")
    return weekly_schedule



    ##############
    while True:
        food_plan = input("Would you like a food plan? (yes or no): ")
        if food_plan.lower() == "yes":
            food_types = suggest_food_plan()
            options = {type: suggest_food_options([type])[0] for type in food_types}
            user_info["food_plan"] = food_types
            user_info["weekly_schedule"] = suggest_weekly_food_schedule(options)
            break
        elif food_plan.lower() == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")

    return user_info


       





#DIET // MEAL PLAN
# 
#1 suggesst foood plan
def suggest_food_plan():
    # this is where i create an empty list for exercises 
    meals = []
    # also a list  of options 
    options = ["vegan", "halal", "whatever"]
    # this is my loop , asking the user to choose exercises up to 3, because thats how many i have in the options 
    while len(meals) < 3:
        meal = input("What meals would you like to do? (Enter one or more, separated by commas): vegan, halal, whatever\n")
        # I use the split fucntion  to split the list by commas
        for choice in meal.split(','):
            choice = choice.strip().lower()
            if choice in options:
                if choice not in meals:
                    # this is me add thier choice to the empty list options 
                    meals.append(choice)
                    if len(meals) == 3:
                        break
            else:
                print("Sorry please choose from the options: vegan, halal, whatever")
        if len(meals) < 3:
            # this more_exercises idea is not mine
            more_meals = input("Would you like to add any other meals? (yes or no)\n")
            if more_meals.lower() == "no":
                break
            elif more_meals.lower() == "yes":
                print("Here are the remaining exercises you can still choose from: ")
                for option in options:
                    if option not in meals:
                        print(option)
                continue
            else:
                print("Please enter 'yes' or 'no'.")
                continue
    if len(meals) == 3:
        # aight
        print("You have chosen all 3.")
    print(f" This is what you have chosen: {', '.join(meals)}")
    return meals

 
#2 suggest food ops 
def suggest_food_options(food_types):
    # this is my workout options, it takes the argument WORKOUT_TYPES
    # options is a dictionary mapping each workout type to a list of exercises 
    options = {
        "vegan": ["tofu", "lentils", "quinoa", "spinach", "broccoli", "almonds", "oats"],
        "halal": ["chicken", "beef", "lamb", "fish", "eggs", "beans", "nuts"],
        "whatever": ["chicken", "salmon", "eggs", "broccoli", "brown rice", "quinoa", "avocado"]
    }
    # empty list with the users chosen options 
    chosen_options = []
    # for loop on the argument ??? each type in workout ???
    for food_type in food_types:
        # print and ask user which workouts and their number 
        print(f"Which {food_type} exercises would you like to include in your food? (enter numbers separated by commas please)")
        meals = options[food_type]
        # this part is not mine, got help from a friend, try to rewrite this in my own way.!!!
        for i, meal in enumerate(meals):
            # pirnting numbered list
            print(f"{i + 1}. {meal}")
            #user input
        chosen = input()
        chosen_meals = []
        #validates user input, in a very complicated way
        while not chosen.replace(',', '').isnumeric() or max([int(num) for num in chosen.split(",")]) > len(meals) or min([int(num) for num in chosen.split(",")]) < 1:
            print("Invalid input. Please enter the numbers of the meals you would like to include (comma-separated please!!!).")
            for i, meal in enumerate(meals):
                print(f"{i + 1}. {meal}")
            chosen = input()
        chosen_meals = [meals[int(num) - 1] for num in chosen.split(",")]
        chosen_options.append(chosen_meals)
    return chosen_options
#3 
#suggest meal schudle , days and shit 
# this is gonna be a little different 
def suggest_weekly_food_schedule(options):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    food_days = input("How many days a week would you like food plan? (1-7)\n")
    while food_days.isdigit() == False or int(food_days) < 1 or int(food_days) > 7:
        food_days = input("Invalid input. How many days a week would you like food plan? (1-7)\n")
    food_days = int(food_days)
    
    all_meals = []
    for meal_list in options.values():
        all_meals.extend(meal_list)
        
    weekly_schedule = {}
    for day in days_of_week:
        if food_days == 0:
            break
        random.shuffle(all_meals)
        food_plan = ", ".join(random.sample(all_meals, random.randint(1, len(all_meals))))
        weekly_schedule[day] = food_plan
        food_days -= 1
    print("Here's your weekly food schedule:")
    for day, plan in weekly_schedule.items():
        print(f"{day}: {plan}")
    return weekly_schedule



##### MAIN #####
def main():
   
    user_info = ask_user_info()
    
    
main()