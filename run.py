import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint



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
print(f"You should eat about  {recomended_deficit} calories per day for about {time} days") 