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
    days_needed = deficit_needed / deficit_per_day
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    return days_needed

"""
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
    # this is the bmr for weight loss 
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    weight_gain_time = BMR * 1.55
    time_to_reach_desired_weight = (desired_weight - weight) / 0.5
    return weight_gain_time, time_to_reach_desired_weight

"""
weight = float(input("Enter your current weight (in kg): "))
height = float(input("Enter your height (in cm): "))
age = int(input("Enter your age: "))
desired_weight = float(input("Enter the weight youd like to build up to (in kg): "))

calories_per_day,time_to_reach_desired_weight = weight_gain_time(weight, height, age, desired_weight)
print("To gain this weight, you should eat about", ceil(calories_per_day), "calories per day.")
print("and will take approximately {} weeks to reach your desired weight.".format(time_to_reach_desired_weight))

"""

#3


###option function###
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

def weight_loss_time(weight, desired_weight,age,height):
    weight_loss_rate = weight - desired_weight
    deficit_needed = weight_loss_rate * 7700
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    deficit_per_day = recomended_deficit
    days_needed = deficit_needed / deficit_per_day
    return days_needed




def weight_gain_time(weight, height, age, desired_weight):
    # this is the bmr for weight loss ?
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    weight_gain_time = BMR * 1.55
    time_to_reach_desired_weight = (desired_weight - weight) / 0.5
    return weight_gain_time, time_to_reach_desired_weight


#weight_change()






"""
def main():
"""

# 1 weight loss commands 
"""
weight = float(input("Enter your current weight in kg:\n "))
height = float(input("Enter your height (in cm): \n"))
age = int(input("Enter your age:\n "))
desired_weight = float(input("Enter your desired weight in kg: \n"))
recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)

#tried to use the same eqn i used for the gain weight function but it didnt reallly make sense
#recomended_deficit2 = (88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)) - 500

deficit_per_day = recomended_deficit
time = weight_loss_time(weight, desired_weight,age,height)
print(f"You should eat about  {recomended_deficit} calories per day for about {time} days") 
print(f"You should eat about  {recomended_deficit2} calories per day for about {time} days") 
"""


#2 weight gain commands
"""
weight = float(input("Enter your current weight (in kg): \n"))
height = float(input("Enter your height (in cm): \n"))
age = int(input("Enter your age: \n"))
desired_weight = float(input("Enter the weight youd like to build up to (in kg): \n"))

calories_per_day,time_to_reach_desired_weight = weight_gain_time(weight, height, age, desired_weight)
print("To gain this weight, you should eat about", ceil(calories_per_day), "calories per day.")
print("and will take approximately {} weeks to reach your desired weight.".format(time_to_reach_desired_weight))
"""


"""

sales = SHEET.worksheet('Sheet1')
data = sales.get_all_values()


print(data)

"""
"""
def get_user_data():
    print ("please answer the following questions")
    weight = float(input("Enter your current weight (in kg): "))
    height = float(input("Enter your height (in cm): "))
    age = int(input("Enter your age: "))
    desired_weight = float(input("Enter your desired weight (in kg): "))



"""



#get_user_data()

"""

def update_data_sheet(data):

    print("updating worksheet")
    user_worksheet = SHEET.worksheet("Sheet1")
    user_worksheet.append_row(data)




data= get_user_data()
user_data = data
update_data_sheet(data)


update_data_sheet(data)
"""



def get_user_data():
    """
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print ("please answer the following questions\n")
        weight = float(input("Enter your current weight (in kg): \n"))
        height = float(input("Enter your height (in cm):\n "))
        age = int(input("Enter your age: "))
        desired_weight = float(input("Enter your desired weight (in kg): \n"))

        #data_str = input("Enter your data here: ")

        sales_data = (weight,height,age,desired_weight)

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data


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


def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("Sheet1")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")



def main():
    data = get_user_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    weight_change()


main()