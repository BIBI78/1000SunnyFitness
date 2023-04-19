from auth import GSPREAD_CLIENT
from sheet import SHEET
from utils import draw_jolly_roger
from weight import weight_change, ask_user_info
from workout import suggest_workout_plan, suggest_workout_options, suggest_weekly_schedule



def main():
    
    draw_jolly_roger()
    user_info = ask_user_info()
    user_data = weight_change(user_info)



main()


