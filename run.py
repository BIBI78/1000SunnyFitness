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

#
# new weight change test function - KG bs 
def weight_change(user_info):
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

    while True:
        meal_plan = input("Would you like a meal plan? (yes or no): ")
        if meal_plan.lower() == "yes":
            user_info["meal_plan"] = suggest_meal_plan()
            break
        elif meal_plan.lower() == "no":
            break
    else:
        print("Invalid input. Please enter yes or no.")

    return user_info

       




# WORKOUT SUGGESTIONS 
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




#DIET // MEAL PLAN
# suggest meal plan 
# so basically this should be a copy paste of workout 
# i should suggest 3 meal plans , vegetarien , gluton free , and whatver with meat etc 
#1
#def suggest_meal_plan():

def suggest_meal_plan():
    meals = []
    options = ["vegan", "gluten free", "whatever", "halal"]
    
    # Ask if the user wants a meal plan
    meal_plan = ""
    # If the user wants a meal plan, ask for meal types
    print("Here are the available meal plans:")
    print("\n".join(options))
        
        # aask for meal types
    while len(meals) < 4:
            meal = input("What kind of meals would you like? (Enter one or more, separated by commas): ")
            
            # split by commas
            for choice in meal.split(","):
                # strip white space and make lowercase
                choice = choice.strip().lower()
                
                if choice in options and choice not in meals:
                    meals.append(choice)
                    if len(meals) == 4:
                        break
                else:
                    print("Hein?  please choose from the list of meal plans.")
            
            # If we haven't reached 4 meals yet, ask if the user wants to add more
            if len(meals) < 4:
                more_meals = input("Would you like to add anything else? (yes or no)\n")
                if more_meals.lower() == "no":
                    break
                elif more_meals.lower() == "yes":
                    print("Heres whats left for the  meal plans you can still add:")
                    for option in options:
                        if option not in meals:
                            print(option)
                    continue
                else:
                    print("Please enter yes or no")
                    continue
    
        # Print the chosen meals
            if len(meals) == 4:
                 print("Ok so everything.")
                 print(f"This is what you decided on: {', '.join(meals)}")
    
    return meals

#2 suggest meal types
#Here im gonna suggest meal options / types , in greater detail
def suggest_meal_options(meal_types):

    options = {
    "vegetarian": ["tofu", "lentils", "quinoa", "spinach", "broccoli", "almonds", "oats"],
    "gluten-free": ["brown rice", "buckwheat", "potatoes", "sweet potatoes", "quinoa", "almonds", "salmon"],
    "halal": ["chicken", "beef", "lamb", "fish", "eggs", "beans", "nuts"],
    "any": ["chicken", "salmon", "eggs", "broccoli", "brown rice", "quinoa", "avocado"]
    }

    chosen_options = []
    #loop on argument
    for meal_type in meal_types:
        print(f"Which {meal_type} meal type would you like (enter number seperated by comma please)")
        meals = options[meal_type]
        for i, meal in enumerate(meals):
            # pint numbered list
            print(f"{i+1}.{exercise}")
            #user input
        chosen = input()
        chosen_exercises = []
        #  validate user input
        while not chosen.replace(',','').isnumeric() or max([int(num) for num in chosen.split(",")]) > len(meals) or min([int(num) for num in chosen.split(",")]) < 1 :
            print("Inavllid input. Please enter the numbers of the meals you would like to include (comma-separated please!!!).")
            for i , meal in enumerate(meals):
                print(f"{i +1}.{meal}")
            chosen = input()
        chosen_meals =  [meal[int(num) - 1] for num in chosen.split(",")]
        chosen_options.append(chosen_meals)
    return chosen_options


#3 
#suggest meal schudle , days and shit 
# this is gonna be a little different 
#3 
#suggest meal schedule, days and shit 
# this is gonna be a little different 
def suggest_weekly_meal_scheudle(options):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    all_meals = []
    for meal_list in options.values():
        all_meals.extend(meal_list)
    
    weekly_schedule = {}
    for day in days_of_week:
        if meal_days == 0:
            break
        random.shuffle(all_meals)
        meal_plan = ",".join(random.sample(all_meals,random.randint(1,len(all_meals))))
        weekly_schedule[day] = meal_plan
        meal_days -= 1
    print("Voila food for the week:")
    for day, plan in weekly_schedule.items():
        print(f"{day}: {plan}")
    return weekly_schedule







##### MAIN #####
def main():
    draw_jolly_roger()
    user_info = ask_user_info()
    weight_change(user_info)
    

    
main()