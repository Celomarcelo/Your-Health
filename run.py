import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
from colorama import init, Fore, Style

init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('your-health-data')

print(Fore.CYAN + 'Your health\n'
          'Calculate your diet according to your goal.')

def calculate_caloric_needs(age, weight, height, gender, activity_level):
    """
    Function that calculates calories like the Harris-Benedict Equation
    """
    # Calculate calorie needs based on gender and activity level

    if gender == 'M':
        calorie_need = 66.47 + (13.75 * weight) + (5.00 * height) - (6.76 * age)
    else:
        calorie_need = 655.1 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
    
    if activity_level == 'sedentary':
        calorie_need *= 1.2
    elif activity_level == 'light':
        calorie_need *= 1.375
    elif activity_level == 'moderate':
        calorie_need *= 1.55
    elif activity_level == 'active':
        calorie_need *= 1.725
    else:
        calorie_need *= 1.9
    
    return calorie_need

def macronutrient_distribution(objective):
    """
    Function that calculates macronutrients and defines the goal
    """
    if objective == 'weight loss':
        return {'proteins': 0.3, 'carbohydrates': 0.4, 'fats': 0.3}
    elif objective == 'muscle mass gain':
        return {'proteins': 0.4, 'carbohydrates': 0.4, 'fats': 0.2}
    else:
        return {'proteins': 0.3, 'carbohydrates': 0.5, 'fats': 0.2}

# Collecting user information
def validate_age(age):
    """
    Function to validate age
    """
    try:
        age = int(age)
        if not (15 <= age <= 120):#check if the input is a number and a rational value
            raise ValueError(Fore.RED + "Age must be a positive integer.")
        return age
    except ValueError:
        print(Fore.RED + "Invalid input for age. Please enter a valid integer between 15 and 120.")
        return None

age = None
while age is None:
    age = validate_age(input(Fore.BLUE + "Enter your age:\n "))
    
def validate_weight(weight):
    """
    Function to validate weight
    """
    try:
        weight = float(weight)
        if not (30 <= weight <= 200):#check if the input is a number and a rational value
            raise ValueError(Fore.RED + "Weight must be a positive number.")
        return weight
    except ValueError:
        print(Fore.RED + "Invalid input for weight. Please enter a valid number between 30 and 200.")
        return None

weight = None
while weight is None:
    weight = validate_weight(input(Fore.BLUE + "Enter your weight in kg:\n "))

def validate_height(height):
    """
    Function to validate height
    """
    try:
        height = float(height.replace(',', '.'))
        if not (1 <= height <= 2.5): #check if the input is a number and a rational value, convert characters
            raise ValueError(Fore.RED + "Height must be a positive number between 1 and 2.5.")
        return height
    except ValueError:
        print(Fore.RED + "Invalid input for height. Please enter a valid number.")
        return None

height = None
while height is None:
    height = validate_height(input(Fore.BLUE + "Enter your height in meters:\n "))

def validate_gender(gender):
    """
    Function to validate gender
    """
    if gender.upper() not in ['M', 'F']:#check if the input is one of the given options
        print(Fore.RED + "Invalid input for gender. Please enter 'M' for male or 'F' for female.")
        return None
    return gender.upper()

gender = None
while gender is None:
    gender = validate_gender(input(Fore.BLUE + "Enter 'M' for male or 'F' for female:\n ").upper())

def validate_activity_level(activity_level):
    """
    Function to validate activity level
    """
    valid_levels = {
        '1': 'sedentary',
        '2': 'light',
        '3': 'moderate',
        '4': 'active',
        '5': 'very active'
    }

    if activity_level not in valid_levels:
        print(Fore.RED + "Invalid input for activity level. Please choose a number from 1 to 5.")
        return None

    return valid_levels[activity_level]

activity_level = None
while activity_level is None:
    activity_input = input(Fore.BLUE + "Enter the number corresponding to your activity level (1 for sedentary, 2 for light, 3 for moderate, 4 for active, 5 for very active):\n")
    activity_level = validate_activity_level(activity_input)

def validate_objective(objective):
    """
    Function to validate objective
    """
    valid_objectives = {
        '1': 'weight loss',
        '2': 'muscle mass gain',
        '3': 'maintenance'
    }

    if objective not in valid_objectives:
        print(Fore.RED + "Invalid input for goal. Please choose a number from 1 to 3.")
        return None

    return valid_objectives[objective]

objective = None
while objective is None:
    objective_input = input(Fore.BLUE + "Enter the number corresponding to your goal (1 for weight loss, 2 for muscle mass gain, 3 for maintenance):\n")
    objective = validate_objective(objective_input)

# Calculating calorie needs
calorie_need = calculate_caloric_needs(age, weight, height, gender, activity_level)

def meal_plan(objective):
    """
    function that shows the eating plan according to the objective
    """
    # Generate meal plan based on the objective
    if objective == 'weight loss':
        return ('To lose weight, you can follow a diet based on:\n'
                'Low-calorie fruits, such as strawberries, tangerines, kiwi, pears, apples, plum melons, watermelons, oranges and pineapple\n'
                'Vegetables, such as zucchini, cucumber, lettuce, tomato, cabbage, kale, broccoli and cauliflower\n'
                'Whole grains, such as brown rice, whole wheat pasta, whole grain bread and oats\n'
                'Lean proteins, such as chicken, fish, seafood, eggs and tofu\n'
                'Low-fat dairy products, such as skimmed milk, low-fat yogurt and white cheeses\n'
                'Vegetable drinks, such as soy, oat and rice drinks\n'
                'Healthy fats in moderation, such as olive oil, Brazil nuts, almonds and walnuts\n'
                'Natural seasonings and condiments, such as rosemary, vinegar, parsley, black pepper and oregano.\n'
                'And an exercise plan according to the objective.\n')
    elif objective == 'muscle mass gain':
        return ('To gain muscle mass, experts recommend consuming a diet based on proteins:\n'
                '"Chicken, red meat, salmon, eggs, tuna, cheese, milk, peanuts, avocado, beans, tofu, lentils, amaranth, buckwheat, turkey, sunflower seeds"\n'
                'And an exercise plan according to the objective.\n')
    else:
        return ('To maintain your weight, experts recommend consuming a balanced diet:\n'
                '“Eat a variety of healthy foods, including fruits, vegetables, lean proteins, whole grains and healthy fats. Avoid processed foods, high in sugar and saturated fats.\n'
                'And an exercise plan according to the objective.\n')
    
def update_your_health_worksheet(gender_column_name, age_column_name, objective_column_name):
    """
    Update Your Health worksheet, add new row with the data provided
    """
    data_worksheet = SHEET.worksheet("data")
    data_worksheet.append_row([gender_column_name, age_column_name, objective_column_name])

def count_gender(sheet, column_name):
    """
    Function to count occurrences of genders (M and F) in a specific column.
    """
    # Extract column data
    column_data = sheet.col_values(sheet.find(column_name).col)

    # Count occurrences of 'M' and 'F'
    count_m = column_data.count('M')
    count_f = column_data.count('F')

    # Determine the result based on counts
    if count_m > count_f:
        result = 'Men'
    elif count_m < count_f:
        result = 'Women'
    else:
        result = 'an equal number of men and women'

    return result


def count_objective(sheet, column_name):
    """
    Function to count occurrences of objectives (weight loss, muscle mass gain, maintenance) in a specific column.
    """
    # Extract column data
    column_data = sheet.col_values(sheet.find(column_name).col)

    # Count occurrences of different objectives
    count_weight = column_data.count('weight loss')
    count_muscle = column_data.count('muscle mass gain')
    count_maintenance = column_data.count('maintenance')

    # Determine the result based on counts
    if count_weight > count_muscle and count_weight > count_maintenance:
        result = 'weight loss'
    elif count_muscle > count_weight and count_muscle > count_maintenance:
        result = 'muscle mass gain'
    elif count_maintenance > count_weight and count_maintenance > count_muscle:
        result = 'maintenance'
    elif count_weight == count_muscle and count_weight != count_maintenance:
        result = 'weight loss and muscle mass gain'
    elif count_muscle == count_maintenance and count_muscle != count_weight:
        result = 'muscle mass gain and maintenance'
    elif count_weight == count_maintenance and count_weight != count_muscle:
        result = 'weight loss and maintenance'
    else:
        result = 'weight loss, muscle mass gain and maintenance.'

    return result
 
update_your_health_worksheet(gender, age, objective)
recommendation = meal_plan(objective)
macronutrient_distribution_info = macronutrient_distribution(objective)
full_gender = 'Male' if gender == 'M' else 'Female'
sheet = SHEET.sheet1  
column_name1 = "gender_column_name"
column_name2 = "objective_column_name"
gender_result = count_gender(sheet ,column_name1)
objective_result = count_objective(sheet ,column_name2) 
diet_plan_color = Fore.BLUE
print_stat_color = Fore.YELLOW 
#display print statments 
print(Fore.YELLOW + 'According to the given values:\n'
      f'Age: {diet_plan_color}{age} ' 
      f'{print_stat_color}Weight: {diet_plan_color}{weight} '
      f'{print_stat_color}Height: {diet_plan_color}{height} '
      f'{print_stat_color}Gender: {diet_plan_color}{full_gender} '
      f'{print_stat_color}Activity level: {diet_plan_color}{activity_level}' + Style.RESET_ALL)
print(Fore.LIGHTYELLOW_EX + "Diet plan:")
print(f"Daily caloric needs: {calorie_need:.3f} cal")
for key, value in macronutrient_distribution_info.items():
    print(f"{key.capitalize()}: {value*100}%")
print(Fore.LIGHTYELLOW_EX + "Meal plan:")
print(recommendation)
print(Fore.MAGENTA + 'According to the database:\n'
      f'There are more {gender_result} looking for {objective_result}.')

