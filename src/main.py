from auth import GSPREAD_CLIENT
from sheet import SHEET
from utils import draw_jolly_roger
from weight import weight_change, ask_user_info
from workout import suggest_workout_plan, suggest_workout_options, suggest_weekly_schedule




def main():
    draw_jolly_roger()
    user_info = ask_user_info()
    user_data = weight_change(user_info)
    
    workout_plan = user_data.get("workout_plan")
    if workout_plan:
        workout_options = suggest_workout_options(workout_plan)
        weekly_schedule = suggest_weekly_schedule(workout_options)  # pass workout_options here
        print(weekly_schedule)

main()


