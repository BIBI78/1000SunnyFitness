import gspread
from auth import GSPREAD_CLIENT

SHEET = GSPREAD_CLIENT.open('1000_sunny_fitness')
