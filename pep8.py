import random
import os


# Draws pirate flag
from math import ceil


def draw_jolly_roger():
    print("WELCOME TO THE 1000 SUNNY")
    print("""
    .=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.'
    |                     ______                     |
    |                  .-"      "-.                  |
    |                 A            A                 |
    |     _          |              |          _     |
    |    ( V         |,  .-.  .-.  ,|         V )    |
    |     > "=._     | )(__A  A__)( |     _.=" <     |
    |    (_N"=._"=._ |A     AA     A| _.="_.="N_)    |
    |           "=._"(_     ^^     _)"_.="           |
    |               "=A__|IIIIII|__A="               |
    |              _.="| AIIIIIIA |"=._              |
    |    _     _.="_.="A          A"=._"=._     _    |
    |   ( A_.="_.="     `--------`     "=._"=._A )   |
    |    > _.="                            "=._ <    |
    |   (_A   free young thug                  A_)   |
    |                                                |
    .=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
    """)


#  CLEAR TERMINAL DISPLAY IMAGES
def clear_terminal():
    """
    Clears terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def display_goodbye_picture():
    """
    Clears terminal displays goodbye picture
    """
    clear_terminal()
    goodbye_picture = '''
                         .;&&=.      .;&&s,
                        ::%%&&&~;   ;::%% ';
                      _:::%%%  '** ;::%%%  ';
                    _;:::%%%%;   *;::%%%%;  ';
                 _;:::::%%%%%;   *:::%%%%%.   ';
               _;::::::%%%%%;    *;::%%%%%%%.  ';
             _;:::::%%%%%%;    _*; A::%%%%%%.=~:';
          _::::::%%%%%%%'   _**:'   '=:=~::%%;~;
       .::::%%%%%%%%%%%===***~'    _.-::::%;~;
           ~~_--===--~~~~~~~==+._.+:::%' %: ;
              =;::::::%%%%%%,   *;:::%' .;
                =;::::::%%%%%%   |::%' .;
                    ~;::::%%%%% *;::% .;
                       ~'+%%%P=' '~%P~
                       Good luck <333
'''
    print(goodbye_picture)


def display_girl_picture():
    """
    Clears terminal display's girl image
    """
    clear_terminal()
    girl_picture = '''
                                  _..
                                          .qd$$$$bp.
                                        .q$$$$$$$$$$m.
                                       .$$$$$$$$$$$$$$
                                     .q$$$$$$$$$$$$$$$$
                                    .$$$$$$$$$$$$PAA$$$$;
                                  .q$$$$$$$$$P^"_.`;$$$$
                                 q$$$$$$$P;AA   ,  /$$$$P
                               .$$$P^::Y$/`  _  .:.$$$/
                              .P.:..    AA `._.-:.. AA$P
                             $':.  __.. :   :..    :'
                            /:_..::.   `. .:.    .'|
                          _::..          T:..   /  :
                        .::..             J:..  :  :
                     .::..          7:..   F:.. :  ;
                 _.::..             |:..   J:.. `./
            _..:::..               /J:..    F:.  :
          .::::..                .T  AA:..   J:.  /
         /:::...               .' `.  AA:..   F_o'
        .:::...              .'     AA  AA:..  J ;
        ::::...           .-'AA`.    _.`._AA:..  AA
        ':::...         .'  `._7.-'_.-  `AA:.   AA
         AA:::...   _..-'__.._/_.--' ,:.   b:.   AA._
          `::::..-"_.'-"_..--"      :..   /):.   `.AA
            `-:/"-7.--""            _::.-'P::..    AA}
 _....------""""""            _..--".-'   AA::..     `-.
(::..              _...----"""  _.-'       `---:..    `-.
 AA::..      _.-""""   `""""---""                `::...___)
  `AA::..  .-"                           How about some physical activity?
    `"""""
'''

    print(girl_picture)


def display_drink_picture():
    clear_terminal()
    drink_picture = """
       ()   ()      ()    /
      ()      ()  ()  /
       ______________/___
       A            /   /
        A^^^^^^^^^^/^^^/
         A     ___/   /
          A   (   )  /
           A  (___) /
            A /    /
             A    /
              A  /
               A/
               ||
               ||
               ||
               ||
               ||
               /AA
              /;;AA
         ==============
         Do you only drink your meals? *GLUG GLUG GLUG* or ???
    """
    print(drink_picture)


# WEIGHT FUNCTIONS
def weight_changed(user_info):
    """
    Calculates weight loss/gain for user and calories need per day
    """
    weight_change = user_info["weight_change"]
    current_weight = user_info["weight"]
    desired_weight = user_info["desired_weight"]
    height = user_info["height"]
    age = int(user_info["age"])  # convert age to integer

    if weight_change == "lose":
        """
        Calculates user weight loss and caloric deficit per day
        """
        weight_loss_rate = current_weight - desired_weight
        deficit_needed = weight_loss_rate * 7700
        recommended_deficit = (10 * current_weight + 6.25 * height - (5 * age) + 5)
        days_needed = deficit_needed / recommended_deficit
        print(f"You should eat about {recommended_deficit} calories per day for about {days_needed} days")
        user_data = (current_weight, height, age, desired_weight)
    else:
        """
        Calculate weight gain, calories per day.
        """
        body_mass_index = 88.362 + (13.397 * current_weight) + (4.799 * height) - (5.677 * age)
        calories_per_day = body_mass_index * 1.55
        time_to_reach_desired_weight = (desired_weight - current_weight) / 0.5
        print("To gain this weight, you should eat about", ceil(calories_per_day), "calories per day.")
        print(f"and it will take approximately {time_to_reach_desired_weight} weeks to reach your desired weight.")
        user_data = (current_weight, height, age, desired_weight)
    return user_data


# USER INFO
def ask_user_info():
    """
    Asks user age, height, weight etc.
    """
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
            desired_weight = float(input("Enter your desired weight in kg: ")) if weight_change == "lose" else float(
                input("Enter the weight you'd like to build up to (in kg): "))
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

    user_info = {
        "name": name,
        "age": age,
        "gender": gender,
        "weight_change": weight_change,
        "weight": weight,
        "desired_weight": desired_weight,
        "height": height
    }

    while True:
        meal_plan = input("Would you like a meal plan? (yes or no): ")
        if meal_plan.lower() == "yes":
            user_info["meal_plan"] = suggest_meal_plan()
            meal_types = user_info["meal_plan"]
            options = {type: suggest_meal_options([type])[0] for type in meal_types}
            user_info["suggest_weekly_meal_schedule"] = suggest_weekly_meal_schedule(options)
            break
        elif meal_plan.lower() == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")

    while True:
        workout_plan = input("Would you like a workout plan? (yes or no): ")
        if workout_plan.lower() == "yes":
            user_info["workout_plan"] = suggest_workout_plan()
            workout_types = user_info["workout_plan"]
            options = {type: suggest_workout_options([type])[0] for type in workout_types}
            user_info["weekly_schedule"] = suggest_weekly_schedule(options, user_info)
            break
        elif workout_plan.lower() == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")

    return user_info


# WORKOUT FUNCTIONS
# 1
def suggest_workout_plan():
    exercises = []
    options = ["cardio", "weight lifting", "home workout"]
    while len(exercises) < 3:
        exercise = input(
            "What exercises would you like to do? "
            "(Enter one or more, separated by commas): "
            "cardio, weight lifting, home workout\n")

        if all(c in ", " for c in exercise):
            print("Please enter at least one exercise.")
            continue

        for choice in exercise.split(','):
            choice = choice.strip().lower()
            while choice not in options:
                print("Sorry, please choose from the options: cardio, weight lifting, home workout.")
                exercise = input(
                    "What exercises would you like to do? "
                    "(Enter one or more, separated by commas): cardio, weight lifting, home workout\n")
                for choice in exercise.split(','):
                    choice = choice.strip().lower()
                continue
            if choice not in exercises:
                exercises.append(choice)
                if len(exercises) == 3:
                    break
        if len(exercises) < 3:
            more_exercises = input("Would you like to add any other exercises? (yes or no)\n")
            while more_exercises.lower() not in ["yes", "no"]:
                print("Please enter 'yes' or 'no'.")
                more_exercises = input("Would you like to add any other exercises? (yes or no)\n")
            if more_exercises.lower() == "no":
                break
            elif more_exercises.lower() == "yes":
                remaining_exercises = [option for option in options if option not in exercises]
                if len(remaining_exercises) > 0:
                    print("Here are the remaining exercises you can still choose from:")
                    for option in remaining_exercises:
                        print(option)
                else:
                    print("You have already chosen all available exercises.")
                continue
    if len(exercises) == 3:
        print("You have chosen all 3.")
    print(f"This is what you have chosen: {', '.join(exercises)}")
    return exercises


# 2
# I suggest exercise types
def suggest_workout_options(workout_types):
    options = {
        "cardio": ["hiking", "long distance running", "boxing", "walking"],
        "weight lifting": ["bench press", "dumbbell press", "dead lift", "leg press", "squat", "pull-up"],
        "home workout": ["push-ups", "sit-ups", "squats", "jump rope", "crunches", "v-ups"]
    }

    chosen_options = []

    for workout_type in workout_types:
        print(f"Which {workout_type} exercises would you like "
              f"to include in your workout? (Enter numbers separated by commas, please)")
        exercises = options[workout_type]

        for i, exercise in enumerate(exercises, start=1):
            print(f"{i}. {exercise}")

        chosen = input()

        while not all(num.strip().isnumeric() and 1 <= int(num) <= len(exercises) for num in chosen.split(",")):
            print("Invalid input. Please enter the numbers of the exercises "
                  "you would like to include (comma-separated, please!).")

            for i, exercise in enumerate(exercises, start=1):
                print(f"{i}. {exercise}")

            chosen = input()

        chosen_exercises = [exercises[int(num.strip()) - 1] for num in chosen.split(",")]
        chosen_options.append(chosen_exercises)

    return chosen_options


# 3
# I suggest a weekly schedule
def suggest_weekly_schedule(options, user_info):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    workout_days_str = input("How many days a week would you like to work out? (1-7)\n")
    while not workout_days_str.isdigit() or int(workout_days_str) < 1 or int(workout_days_str) > 7:
        workout_days_str = input("Invalid input. How many days a week would you like to work out? (1-7)\n")
    workout_days = int(workout_days_str)
    original_workout_days = workout_days

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

    """
    This is part of the activity coef function.
    """
    weight_change = user_info["weight_change"]
    weight = user_info["weight"]
    desired_weight = user_info["desired_weight"]
    height = user_info["height"]
    age = int(user_info["age"])

    """
    Here I calculate the Activity Factor
    """
    activity_coef = original_workout_days
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    if weight_change == "lose":
        daily_caloric_intake = bmr * 0.8
    else:
        daily_caloric_intake = bmr * 1.2

    if desired_weight > weight:
        weight_change_factor = 1
    elif desired_weight == weight:
        weight_change_factor = 0
    else:
        weight_change_factor = -1

    activity_factor = (daily_caloric_intake + (weight_change_factor * 500)) / bmr

    print("Here's your weekly workout schedule:")
    for day, plan in weekly_schedule.items():
        print(f"{day}: {plan}")

    print("You have an activity coefficient of:", activity_coef, "so you should ACTUALLY eat about",
          abs(ceil(activity_factor * daily_caloric_intake) - daily_caloric_intake),
          "more each day you workout to stay on target.")

    return weekly_schedule, original_workout_days, activity_factor


# MEAL PLAN
# 1 suggest meal plan
def suggest_meal_plan():
    meals = []
    options = ["vegan", "halal", "gluten free", "whatever"]
    while len(meals) < 4:
        meal = input(
            "What meals would you like to have? (Enter one or more, "
            "separated by commas): vegan, halal, gluten free, whatever\n")
        if all(c in ", " for c in meal):
            print("Please enter at least one meal.")
            continue

        for choose in meal.split(','):
            choose = choose.strip().lower()
            while choose not in options:
                print("Sorry, please choose from the options: vegan, halal, gluten free, whatever")
                meal = input(
                    "What meals would you like to eat? (Enter one or more, "
                    "separated by commas): vegan, halal, gluten free, whatever\n")
                for choose in meal.split(','):
                    choose = choose.strip().lower()
                continue
            if choose not in meals:
                meals.append(choose)
                if len(meals) == 4:
                    break
        if len(meals) < 4:
            more_meals = input("Would you like to add any other meals? (yes or no)\n")
            if more_meals.lower() == "no":
                break
            elif more_meals.lower() == "yes":
                print("Here are the remaining meals you can still choose from:")
                for option in options:
                    if option not in meals:
                        print(option)
                continue
            else:
                print("Please enter 'yes' or 'no'.")
                continue
    if len(meals) == 4:
        print("You have chosen all 4.")
    print(f"This is what you have chosen: {', '.join(meals)}")
    return meals


# 2 suggest meal types
def suggest_meal_options(meal_types):
    options = {
        "vegan": ["tofu", "lentils", "quinoa", "spinach", "broccoli", "almonds", "oats"],
        "gluten free": ["brown rice", "buckwheat", "potatoes", "sweet potatoes", "quinoa", "almonds", "salmon"],
        "halal": ["chicken", "beef", "lamb", "fish", "eggs", "beans", "nuts"],
        "whatever": ["chicken", "salmon", "eggs", "broccoli", "brown rice", "quinoa", "avocado"]
    }

    chosen_options = []

    for meal_type in meal_types:
        print(f"Which {meal_type} meal type would you like? (Enter numbers separated by commas, please)")
        meals = options[meal_type]

        for i, meal in enumerate(meals, start=1):
            print(f"{i}. {meal}")

        chosen = input()

        while not all(num.strip().isnumeric() and 1 <= int(num) <= len(meals) for num in chosen.split(",")):
            print("Invalid input. Please enter the numbers of the meals you would "
                  "like to include (comma-separated, please!).")

            for i, meal in enumerate(meals, start=1):
                print(f"{i}. {meal}")

            chosen = input()

        chosen_meals = [meals[int(num.strip()) - 1] for num in chosen.split(",")]
        chosen_options.append(chosen_meals)

    return chosen_options


# 3 suggest weekly meal schedule
def suggest_weekly_meal_schedule(options):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meal_days = input("How many days a week would you like a meal plan? (1-7)\n")
    while not meal_days.isdigit() or int(meal_days) < 1 or int(meal_days) > 7:
        meal_days = input("Invalid input. How many days a week would you like a food plan? (1-7)\n")
    meal_days = int(meal_days)

    all_meals = []
    for meal_list in options.values():
        all_meals.extend(meal_list)

    weekly_schedule = {}
    for day in days_of_week:
        if meal_days == 0:
            break
        random.shuffle(all_meals)
        meal_plan = ",".join(random.sample(all_meals, random.randint(1, len(all_meals))))
        weekly_schedule[day] = meal_plan
        meal_days -= 1
    print("Voila food for the week:")
    for day, plan in weekly_schedule.items():
        print(f"{day}: {plan}")
    return weekly_schedule


def main():
    draw_jolly_roger()
    user_info = ask_user_info()
    weight_changed(user_info)


if __name__ == "__main__":
    main()