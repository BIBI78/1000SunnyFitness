import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

"""
def weight_loss_time(weight, desired_weight, deficit_per_day):
    weight_loss_rate = weight - desired_weight
    #this eqn is from the net
    deficit_needed = weight_loss_rate * 7700
    days_needed = deficit_needed / deficit_per_day
    return days_needed



weight = float(input("Enter your current weight in kg: "))
desired_weight = float(input("Enter your desired weight in kg: "))
deficit_per_day = int(input("Enter your estimated calorie deficit per day/ how much you plan to eat per day: "))
time = weight_loss_time(weight, desired_weight, deficit_per_day)
print(f"It will take approximately {time} days to reach your desired weight")  

"""


def weight_loss_time(weight, desired_weight,age,height):
    weight_loss_rate = weight - desired_weight
    deficit_needed = weight_loss_rate * 7700
    days_needed = deficit_needed / deficit_per_day
    return days_needed

weight = float(input("Enter your current weight in kg: "))
height = float(input("Enter your height (in cm): "))
age = int(input("Enter your age: "))
desired_weight = float(input("Enter your desired weight in kg: "))
recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
deficit_per_day = recomended_deficit
time = weight_loss_time(weight, desired_weight,age,height)
#print(f"It will take qbout {time} days to reach your desired weight")  
print(f"You should eat about  {recomended_deficit} calories per day for about {time} days") 