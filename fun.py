import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
from math import ceil
#this is the most develloped code , most up to date*
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('1000_sunny_fitness')

# Pirate flag #
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


#1
def weight_loss_time(weight, desired_weight,age,height):
    weight_loss_rate = weight - desired_weight
    deficit_needed = weight_loss_rate * 7700
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    deficit_per_day = recomended_deficit 
    days_needed = deficit_needed / deficit_per_day
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    deficit_needed = recomended_deficit
    #user_data = (weight,height,age,desired_weight)
    return days_needed 
#2

def weight_gain_time(weight, height, age, desired_weight):
    # this is the bmr for weight loss 
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    weight_gain_time = BMR * 1.55
    time_to_reach_desired_weight = (desired_weight - weight) / 0.5
    #user_data = (weight,height,age,desired_weight)
    return weight_gain_time, time_to_reach_desired_weight


def weight_change():
    while True:
        weight_change = input("WELCOME TO 1000 SUNNY FITNESS \n Would you like to lose or gain weight? (lose or gain): \n")
        if weight_change == "lose":
            print("Please answer the following questions\n")
            weight = float(input("Enter your current weight in kg:\n "))
            height = float(input("Enter your height (in cm): \n"))
            age = int(input("Enter your age: "))
            desired_weight = float(input("Enter your desired weight in kg: \n"))
            recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
            time = weight_loss_time(weight, desired_weight,age,height)
            print(f"You should eat about  {recomended_deficit} calories per day for about {time} days")
            deficit_per_day = recomended_deficit 
            weight_loss_time(weight, desired_weight,age,height)
            user_data = (weight,height,age,desired_weight)
            break
        elif weight_change == "gain":
            print("Please answer the following questions\n")
            weight = float(input("Enter your current weight (in kg): \n"))
            height = float(input("Enter your height (in cm): \n"))
            age = int(input("Enter your age: "))
            desired_weight = float(input("Enter the weight youd like to build up to (in kg): \n"))
            calories_per_day, time_to_reach_desired_weight = weight_gain_time(weight, height, age, desired_weight)
            print("To gain this weight, you should eat about", ceil(calories_per_day), "calories per day.")
            print("and will take approximately {} weeks to reach your desired weight.".format(time_to_reach_desired_weight))
            weight_gain_time(weight, height, age, desired_weight)
            user_data = (weight,height,age,desired_weight)
            break
        else:
            print("Invalid response, please enter either 'lose' or 'gain'")

def stored_user_data():
    weight, age , height,desired_weight = weight_change()
    user_data = (weight,height,age,desired_weight)
    return user_data,




# USE THIS TO VALIDATE DATA #
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 4:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True





# DECLARE GLOBAL VARIABLES HERE?? #
 #user_data = (weight,height,age,desired_weight)
 # maybe define user ddata and weight in another fucntion that does ask the user anything in the terminal 




def main ():
    draw_jolly_roger()
    weight_change()
    stored_user_data()
   
    
  
    


main()
