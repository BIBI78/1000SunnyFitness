import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import requests
import json
import random
import time 
from math import ceil


def weight_change(user_info):
    """this function takes user info parameter and works out weight change """
    weight_change = user_info["weight_change"]
    current_weight = user_info["weight"]
    desired_weight = user_info["desired_weight"]
    height = user_info["height"]
    age = int(user_info["age"]) # convert age to integer

    if weight_change == "lose":
        # this is weight loss
        weight_loss_rate = current_weight - desired_weight
        deficit_needed = weight_loss_rate * 7700
        # cest un peu le BMR
        recommended_deficit = (10*(current_weight) + 6.25*(height) - (5*age) + 5)
        days_needed = deficit_needed / recommended_deficit
        print(f"You should eat about {recommended_deficit} calories per day for about {days_needed} days")
        user_data = (current_weight, height, age, desired_weight)
    else:
        # this is weight gain
        #et ceci cest LA BMR
        BMR = 88.362 + (13.397 * current_weight) + (4.799 * height) - (5.677 * age)
        calories_per_day = BMR * 1.55 
        time_to_reach_desired_weight = (desired_weight - current_weight) / 0.5
        print("To gain this weight, you should eat about", ceil(calories_per_day), "calories per day.")
        print(f"and it will take approximately {time_to_reach_desired_weight} weeks to reach your desired weight.")
        user_data = (current_weight, height, age, desired_weight)
        # potential new code
    return user_data

#USER INFO
# I have editted this function over and over 
#This should prompt the user to re-enter their information if they input an age over 150, a height over 251 cm, or a weight over 635 kg.
def ask_user_info():
    print("WELCOME TO 1000 SUNNY FITNESS \n")
    name = input("What's your name?\n")
    while True:
        age = input("How old are you?\n")
        if age.isnumeric() and int(age) > 0:
            if int(age) > 150:
                print("This app is for humans, please enter a human age.")
                continue
            break
        print("Sorry matey, let's get your age again.")
    gender = input("What do you identify as?\n")
    while True:
        weight_change = input("Would you like to lose or gain weight? (lose or gain): ")
        if weight_change == "lose" or weight_change == "gain":
            break
        print("That doesn't work, please enter either 'lose' or 'gain'")

    while True:
        try:
            weight = float(input("Enter your current weight in kg: "))
            if weight <= 0 or weight > 635:
                print("This app is for humans, please enter a human weight.")
                continue
            break
        except ValueError:
            print("We need a number, try again.")

    while True:
        try:
            desired_weight = float(input("Enter your desired weight in kg: ")) if weight_change == "lose" else float(input("Enter the weight you'd like to build up to (in kg): "))
            if desired_weight <= 0 or desired_weight > 635:
                print("This app is for humans, please enter a human weight.")
                continue
            if weight_change == "gain" and desired_weight <= weight:
                raise ValueError("Desired weight must be greater than current weight.")
            elif weight_change == "lose" and desired_weight >= weight:
                raise ValueError("Desired weight must be less than current weight.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            height = float(input("Enter your height in cm: "))
            if height <= 0 or height > 251:
                print("This app is for humans, please enter a human height.")
                continue
            break
        except ValueError:
            print("Invalid input, please enter a number")


   

    user_info = {"name": name, "age": age, "gender": gender, "weight_change": weight_change, "weight": weight, "desired_weight": desired_weight, "height": height}

   
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
    

    return user_info

# WORKOUT SUGGESTIONS 
# problem when i enter a comma after at exercise options
#1
def suggest_workout_plan():
    exercises = []
    options = ["cardio", "weight lifting", "home workout"]
    while len(exercises) < 3:
        exercise = input("What exercises would you like to do? (Enter one or more, separated by commas): cardio, weight lifting, home workout\n")
        
        if all(c in ", " for c in exercise):
            print("Please enter at least one exercise.")
            continue
        
        for choice in exercise.split(','):
            choice = choice.strip().lower()
            while choice not in options:
                print("Sorry please choose from the options: cardio, weight lifting, home workout.")
                exercise = input("What exercises would you like to do? (Enter one or more, separated by commas): cardio, weight lifting, home workout\n")
                for choice in exercise.split(','):
                    choice = choice.strip().lower()
                continue
            if choice not in exercises:
                exercises.append(choice)
                if len(exercises) == 3:
                    break
        if len(exercises) < 3:
            more_exercises = input("Would you like to add any other exercises? (yes or no)\n")
            while more_exercises.lower() not in ["yes", "no"]:
                print("Please enter 'yes' or 'no'.")
                more_exercises = input("Would you like to add any other exercises? (yes or no)\n")
            if more_exercises.lower() == "no":
                break
            elif more_exercises.lower() == "yes":
                remaining_exercises = [option for option in options if option not in exercises]
                if len(remaining_exercises) > 0:
                    print("Here are the remaining exercises you can still choose from:")
                    for option in remaining_exercises:
                        print(option)
                else:
                    print("You have already chosen all available exercises.")
                continue
    if len(exercises) == 3:
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
    workout_days_str = input("How many days a week would you like to work out? (1-7)\n")
    while workout_days_str.isdigit() == False or int(workout_days_str) < 1 or int(workout_days_str) > 7:
        workout_days_str = input("Invalid input. How many days a week would you like to work out? (1-7)\n")
    workout_days = int(workout_days_str)
    original_workout_days = workout_days
    
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
    return weekly_schedule, original_workout_days





#### ACTIVITY FACTOR
# this kinda works
def calculate_activity_factor(user_info, suggest_weekly_schedule):
    weight_change = user_info["weight_change"]
    weight = user_info["weight"]
    desired_weight = user_info["desired_weight"]
    height = user_info["height"]
    age = int(user_info["age"])

    options = {
        "workout_plan": user_info["workout_plan"],
        
    }
   # weekly_schedule, workout_days = suggest_weekly_schedule(options)
    # original_workout_days = suggest_weekly_schedule(options)
    weekly_schedule, original_workout_days = suggest_weekly_schedule(options)[:2]



    activity_coef = original_workout_days

    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

    if weight_change == "lose":
        daily_caloric_intake = bmr * 0.8
    else:
        daily_caloric_intake = bmr * 1.2

    if desired_weight > weight:
        weight_change_factor = 1
    elif desired_weight == weight:
        weight_change_factor = 0
    else:
        weight_change_factor = -1

    activity_factor = (daily_caloric_intake + (weight_change_factor * 500)) / bmr

    blah = ("This is your recommended caloric intake per day with the activity factor:", ceil(activity_factor * daily_caloric_intake))
    print(blah)
    print("This is the activity coeff:", activity_coef)

    return activity_factor








##### MAIN #####
def main():
    
    user_info = ask_user_info()
    weight_change(user_info)
    

    activity_factor = calculate_activity_factor(user_info,suggest_weekly_schedule)
    #activity_factor = calculate_activity_factor(user_info)



    ###
    print("Activity factor:", activity_factor)
    
main()
