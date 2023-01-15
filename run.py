import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
from math import ceil

"""
#1
def weight_loss_time(weight, desired_weight,age,height):
    weight_loss_rate = weight - desired_weight
    deficit_needed = weight_loss_rate * 7700
    days_needed = deficit_needed / deficit_per_day
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    return days_needed

weight = float(input("Enter your current weight in kg: "))
height = float(input("Enter your height (in cm): "))
age = int(input("Enter your age: "))
desired_weight = float(input("Enter your desired weight in kg: "))
recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)

#tried to use the same eqn i used for the gain weight function but it didnt reallly make sense
#recomended_deficit2 = (88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)) - 500

deficit_per_day = recomended_deficit
time = weight_loss_time(weight, desired_weight,age,height)
print(f"You should eat about  {recomended_deficit} calories per day for about {time} days") 
print(f"You should eat about  {recomended_deficit2} calories per day for about {time} days") 

"""


#2

def weight_gain_time(weight, height, age, desired_weight):
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    weight_gain_time = BMR * 1.55
    time_to_reach_desired_weight = (desired_weight - weight) / 0.5
    return weight_gain_time, time_to_reach_desired_weight

weight = float(input("Enter your current weight (in kg): "))
height = float(input("Enter your height (in cm): "))
age = int(input("Enter your age: "))
desired_weight = float(input("Enter the weight youd like to build up to (in kg): "))

calories_per_day,time_to_reach_desired_weight = weight_gain_time(weight, height, age, desired_weight)
print("To gain this weight, you should eat about", ceil(calories_per_day), "calories per day.")
print("and will take approximately {} weeks to reach your desired weight.".format(time_to_reach_desired_weight))

