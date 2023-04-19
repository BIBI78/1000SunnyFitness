import random
from random import randint
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
    # dictionary with the users chosen options 
    chosen_options = {}
    # for loop on the argument 
    for workout_type in workout_types:
        # print and ask user which workouts and their number 
        print(f"Which {workout_type} exercises would you like to include in your workout? (enter numbers separated by commas please)")
        exercises = options[workout_type]
        # printing numbered list
        for i, exercise in enumerate(exercises):
            print(f"{i + 1}. {exercise}")
        # user input
        chosen = input()
        # validates user input, makes sure the users input is seperated commas and only takes in integers 
        # this validation process is probaly more complicated that it needs to be
        while not chosen.replace(',', '').isnumeric() or max([int(num) for num in chosen.split(",")]) > len(exercises) or min([int(num) for num in chosen.split(",")]) < 1:
            print("Please enter the numbers of the exercises you would like to include (comma-separated please!!!).")
            for i, exercise in enumerate(exercises):
                print(f"{i + 1}. {exercise}")
            chosen = input()
        # adding chosen exercises to dictionary
        chosen_exercises = [exercises[int(num) - 1] for num in chosen.split(",")]
        chosen_options[workout_type] = chosen_exercises
    return chosen_options


#3
# This function is supposed to generate a scheudle based on the users input
# Takes the arguments "options"

import random

import random
from random import randint

def suggest_weekly_schedule(options):
    days_of_the_week = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    workout_days = input("How many days a week would you want to workout (enter a number 1-7)? ")

    # loop to make sure user input is valid
    while not workout_days.isdigit() or int(workout_days) < 1 or int(workout_days) > 7:
        workout_days = input("That doesn't work, how many days would you like to workout a week? (enter a number 1-7): ")

    workout_days = int(workout_days)

    # generate a list of all exercises from the given workout categories
    all_exercises = []
    for category in options.keys():
        exercises = options[category]
        all_exercises.extend(exercises)

    # generate a random schedule by randomly selecting values from all_exercises list for the days of the week
    weekly_schedule = {}
    for day in days_of_the_week:
        if workout_days == 0:
            break
        random.shuffle(all_exercises)
        workout_plan = ",".join(random.sample(all_exercises,randint(1,len(all_exercises))))
        weekly_schedule[day]=workout_plan
        workout_days -= 1

    print("Here is a weekly schedule:\n")
    for day , plan in weekly_schedule.items():
        print(f"{day}: {plan}")

    return weekly_schedule

