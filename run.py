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
def weight_change(user_info):
    weight_change = user_info["weight_change"]
    while True:
        try:
            weight = float(input("Enter your current weight in kg: "))
            if weight <= 0:
                raise ValueError("Nobody is that light,weeight must be greater than 0.")
            break
        except ValueError as e:
            print(f"We need a number, try again.")

    while True:
        try:
            height = float(input("Enter your height (in cm): "))
            if height <= 0:
                raise ValueError("Height must be greater than 0.")
            break
        except ValueError as e:
            print(f"Huh? Height must be greater than 0.")

    age = int(user_info["age"])

    while True:
        try:
            desired_weight = float(input("Enter your desired weight in kg: ")) if weight_change == "lose" else float(input("Enter the weight you'd like to build up to (in kg): "))
            if desired_weight <= 0:
                raise ValueError("Desired weight must be greater than 0.")
            if weight_change == "gain" and desired_weight <= weight:
                raise ValueError("Desired weight must be greater than current weight.")
            break
        except ValueError as e:
            print(f"Invalid input, please enter a number")

    if weight_change == "lose":
        weight_loss_rate = weight - desired_weight
        deficit_needed = weight_loss_rate * 7700
        recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
        days_needed = deficit_needed / recomended_deficit
        print(f"You should eat about {recomended_deficit} calories per day for about {days_needed} days")
        user_data = (weight, height, age, desired_weight)
    else:
        BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        calories_per_day = BMR * 1.55
        time_to_reach_desired_weight = (desired_weight - weight) / 0.5
        print("To gain this weight, you should eat about", ceil(calories_per_day), "calories per day.")
        print(f"and it will take approximately {time_to_reach_desired_weight} weeks to reach your desired weight.")
        user_data = (weight, height, age, desired_weight)

    return user_data




#USER INFO
def get_user_info():
    print("WELCOME TO 1000 SUNNY FITNESS \n")
    name = input("What's your name?\n")
    while True:
        age = input("How old are you?\n")
        if age.isnumeric() and int(age) > 0:
            break
        print("Sorry matey lets get your age again.")
    # do i even need this really ?
    gender = input("What gender do you identify as?\n") 
    while True:
        weight_change = input("Would you like to lose or gain weight? (lose or gain): ")
        if weight_change == "lose" or weight_change == "gain":
            break
        print("That doesnt work, please enter either 'lose' or 'gain'")
    user_info = {"name": name, "age": age, "gender": gender, "weight_change": weight_change}
    return user_info
  

def main():
    draw_jolly_roger()
    user_info = get_user_info()
    weight_change(user_info)

main()