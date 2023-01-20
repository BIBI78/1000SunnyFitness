import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
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

#1
def weight_loss_time(weight, desired_weight,age,height):
    weight_loss_rate = weight - desired_weight
    deficit_needed = weight_loss_rate * 7700
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    deficit_per_day = recomended_deficit 
    days_needed = deficit_needed / deficit_per_day
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    deficit_needed = recomended_deficit
    return days_needed
#2

def weight_gain_time(weight, height, age, desired_weight):
    # this is the bmr for weight loss 
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    weight_gain_time = BMR * 1.55
    time_to_reach_desired_weight = (desired_weight - weight) / 0.5
    return weight_gain_time, time_to_reach_desired_weight


def weight_change():
    while True:
        weight_change = input("Would you like to lose or gain weight? (lose or gain): \n")
        if weight_change == "lose":
            weight = float(input("Enter your current weight in kg:\n "))
            height = float(input("Enter your height (in cm): \n"))
            age = int(input("Enter your age: "))
            desired_weight = float(input("Enter your desired weight in kg: \n"))
            recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
            time = weight_loss_time(weight, desired_weight,age,height)
            print(f"You should eat about  {recomended_deficit} calories per day for about {time} days")
            deficit_per_day = recomended_deficit 
            weight_loss_time(weight, desired_weight,age,height)
            break
        elif weight_change == "gain":
            weight = float(input("Enter your current weight (in kg): \n"))
            height = float(input("Enter your height (in cm): \n"))
            age = int(input("Enter your age: "))
            desired_weight = float(input("Enter the weight youd like to build up to (in kg): \n"))
            calories_per_day, time_to_reach_desired_weight = weight_gain_time(weight, height, age, desired_weight)
            print("To gain this weight, you should eat about", ceil(calories_per_day), "calories per day.")
            print("and will take approximately {} weeks to reach your desired weight.".format(time_to_reach_desired_weight))
            weight_gain_time(weight, height, age, desired_weight)
            break
        else:
            print("Invalid response, please enter either 'lose' or 'gain'")



def main ():
    weight_change()



main()