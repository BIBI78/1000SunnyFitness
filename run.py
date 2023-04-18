import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import requests
import json
import random
import time 
from math import ceil


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('1000_sunny_fitness')


# Draws pirate flag
def draw_jolly_roger():
    print("WELCOME TO THE 1000 SUNNY")
    jolly_roger =  '.=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.\n'
    jolly_roger += '|                     ______                     |\n'
    jolly_roger += '|                  .-"      "-.                  |\n'
    jolly_roger += '|                 /            \                 |\n'
    jolly_roger += '|     _          |              |          _     |\n'
    jolly_roger += '|    ( \         |,  .-.  .-.  ,|         / )    |\n'
    jolly_roger += '|     > "=._     | )(__/  \__)( |     _.=" <     |\n'
    jolly_roger += '|    (_/"=._"=._ |/     /\     \| _.="_.="\_)    |\n'
    jolly_roger += '|           "=._"(_     ^^     _)"_.="           |\n'
    jolly_roger += '|               "=\__|IIIIII|__/="               |\n'
    jolly_roger += '|              _.="| \IIIIII/ |"=._              |\n'
    jolly_roger += '|    _     _.="_.="\          /"=._"=._     _    |\n'
    jolly_roger += '|   ( \_.="_.="     `--------`     "=._"=._/ )   |\n'
    jolly_roger += '|    > _.="                            "=._ <    |\n'
    jolly_roger += '|   (_/   free young thug                  \_)   |\n'
    jolly_roger += '|                                                |\n'
    jolly_roger += '.=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.\n'
    print(jolly_roger)

#WEIGHT FUNCTIONS
# Weight loss function , this calculates the days needed for the user to lose weight.
# So this new function combines weight loss and and weight gain. 
# this function takes the user data provided earlier and does  the necessary calculations for weight loss or gain
# new weight change test function - KG bs 
# add upper and lower bounds to numeric user info
def weight_change(user_info):
    # here im just take the weight change key from the user info dictionary , and the same for the rest.
    weight_change = user_info["weight_change"]
    current_weight = user_info["weight"]
    desired_weight = user_info["desired_weight"]
    height = user_info["height"]
    age = int(user_info["age"]) # convert age to integer

    if weight_change == "lose":
        # this is weight loss
        weight_loss_rate = current_weight - desired_weight
        deficit_needed = weight_loss_rate * 7700
        recommended_deficit = (10*(current_weight) + 6.25*(height) - (5*age) + 5)
        days_needed = deficit_needed / recommended_deficit
        print(f"You should eat about {recommended_deficit} calories per day for about {days_needed} days")
        user_data = (current_weight, height, age, desired_weight)
    else:
        # this is weight gain
        BMR = 88.362 + (13.397 * current_weight) + (4.799 * height) - (5.677 * age)
        calories_per_day = BMR * 1.55 
        time_to_reach_desired_weight = (desired_weight - current_weight) / 0.5
        print("To gain this weight, you should eat about", ceil(calories_per_day), "calories per day.")
        print(f"and it will take approximately {time_to_reach_desired_weight} weeks to reach your desired weight.")
        user_data = (current_weight, height, age, desired_weight)
        # potential new code
    return user_data
# need to add ACTIVITY FACTOR 



#USER INFO

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
    gender = input("What gender do you identify as?\n")
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
                raise ValueError("Desired weight gotta be greater than current weight")
            elif weight_change == "lose" and desired_weight >= weight:
                raise ValueError("Desired weight gotta be less than current weight")
            break
        # this (e) i dont quite understand , got it from a forum , need it to remedy problem with except value eerrors
        # and the wieght loss mess 
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
            print("Please enter a number!")

    user_info = {"name": name, "age": age, "gender": gender, "weight_change": weight_change, "weight": weight, "desired_weight": desired_weight, "height": height}

    while True:
        workout_plan = input("Would you like a workout plan? (yes or no): ")
        if workout_plan.lower() == "yes":
            user_info["workout_plan"] = suggest_workout_plan()
            #here im getting the workout info from the user info and assigning it
            workout_types = user_info["workout_plan"]
            ## this part is complicated // DICTIONARY
            # here im creating a dictionary where the keys are the workout types 
            # and the values are the suggested workout optionns:
            # "type" is the key and and suggest_workout_options()[type][#] is the "value"
            #suggest_workout_options takes "workout_type" as an argument then returns a list at whatever index [#]
            options = {type: suggest_workout_options([type])[0] for type in workout_types}
           ####
           ####
           #### space for more code
            break
        elif workout_plan.lower() == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")

    return user_info


   
#workout info
# 1
# this function suggestion 3 workout types( cardio , weights ,home)
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
#workout options , create dictionary 
def suggest_workout_options(workout_types):
    # need to pass an argument , this is just the workout options options ?
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
        #validates user input, makes sure the users input is seperated commas and only takes in integers 
        # this validation process is probaly more complicated that it needs to be
        while not chosen.replace(',', '').isnumeric() or max([int(num) for num in chosen.split(",")]) > len(exercises) or min([int(num) for num in chosen.split(",")]) < 1:
            print("Please enter the numbers of the exercises you would like to include (comma-separated please!!!).")
            for i, exercise in enumerate(exercises):
                print(f"{i + 1}. {exercise}")
            chosen = input()
        chosen_exercises = [exercises[int(num) - 1] for num in chosen.split(",")]
        chosen_options.append(chosen_exercises)
    return chosen_options

    
#3
# This function is supposed to generate a scheudle based on the users input
def suggest_weekly_schedule():
 days_of_the_week["Monday," "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
 workout_days = input("How many days a week would you wanna workout (enter a number 1-7\n )")
 # this is  a loop to make sure user input is valid
while workout_days.isdigit() == False or int(workout_days) < 1 or int(work_out) > 7:
    workout_days = input("That doesnt work, how many days would you like to workout a week? (eneter a number 1-7\n )")
# int , converts stirng to an integer, a number
workout_days=int(workout_days)






def main():
    draw_jolly_roger()
    user_info = ask_user_info()
    weight_change(user_info)

main()