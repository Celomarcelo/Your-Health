import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('your-health-data')

print('Your health\n'
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
            raise ValueError("Age must be a positive integer.")
        return age
    except ValueError:
        print("Invalid input for age. Please enter a valid integer between 15 and 120.")
        return None

age = None
while age is None:
    age = validate_age(input("Enter your age:\n "))
    
def validate_weight(weight):
    """
    Function to validate weight
    """
    try:
        weight = float(weight)
        if not (30 <= weight <= 200):#check if the input is a number and a rational value
            raise ValueError("Weight must be a positive number.")
        return weight
    except ValueError:
        print("Invalid input for weight. Please enter a valid number between 30 and 200.")
        return None

weight = None
while weight is None:
    weight = validate_weight(input("Enter your weight in kg:\n "))

def validate_height(height):
    """
    Function to validate height
    """
    try:
        height = float(height.replace(',', '.'))
        if not (1 <= height <= 2.5): #check if the input is a number and a rational value, convert characters
            raise ValueError("Height must be a positive number between 1 and 2.5.")
        return height
    except ValueError:
        print("Invalid input for height. Please enter a valid number.")
        return None

height = None
while height is None:
    height = validate_height(input("Enter your height in meters:\n "))

def validate_gender(gender):
    """
    Function to validate gender
    """
    if gender.upper() not in ['M', 'F']:#check if the input is one of the given options
        print("Invalid input for gender. Please enter 'M' for male or 'F' for female.")
        return None
    return gender.upper()

gender = None
while gender is None:
    gender = validate_gender(input("Enter 'M' for male or 'F' for female:\n ").upper())

def validate_activity_level(activity_level):
    """
    Function to validate activity level
    """
    valid_levels = ['sedentary', 'light', 'moderate', 'active', 'very active']
    if activity_level.lower() not in valid_levels:#check if the input is one of the given options
        print("Invalid input for activity level. Please choose from: sedentary, light, moderate, active, very active.")
        return None
    return activity_level.lower()

activity_level = None
while activity_level is None:
    activity_level = validate_activity_level(input("Enter your activity level (sedentary, light, moderate, active, very active):\n "))

def validate_objective(objective):
    """
    Function to validate objective
    """
    valid_objectives = ['weight loss', 'muscle mass gain', 'maintenance']
    if objective.lower() not in valid_objectives:#check if the input is one of the given options
        print("Invalid input for goal. Please choose from: weight loss, muscle mass gain, maintenance.")
        return None
    return objective.lower()

objective = None
while objective is None:
    objective = validate_objective(input("Enter your goal (weight loss, muscle mass gain, maintenance):\n ").lower())

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
                'Legumes, such as beans, lentils, chickpeas and soybeans\n'
                'Natural seasonings and condiments, such as rosemary, vinegar, parsley, black pepper and oregano.')
    elif objective == 'muscle mass gain':
        return ('To gain muscle mass, experts recommend consuming a diet based on proteins."Chicken, red meat, salmon, eggs, tuna, cheese, milk, peanuts, avocado, beans, tofu, lentils, amaranth, buckwheat, turkey, sunflower seeds."')
    else:
        return ('To maintain your weight, experts recommend consuming a balanced diet. “Eat a variety of healthy foods, including fruits, vegetables, lean proteins, whole grains and healthy fats. Avoid processed foods, high in sugar and saturated fats.')
    
def update_your_health_worksheet(gender, age, objective):
    """
    Update Your Health worksheet, add new row with the data provided
    """
    data_worksheet = SHEET.worksheet("data")
    data_worksheet.append_row([gender, age, objective])
 
recommendation = meal_plan(objective)
macronutrient_distribution_info = macronutrient_distribution(objective)
full_gender = 'Male' if gender == 'M' else 'Female'
   
#display print statments 
print(f'According to the given values:\n'
      f'Age:{age} Weight:{weight} Height:{height} Gender:{full_gender} Activity level:{activity_level}')
print("Diet plan:")
print(f"Daily caloric needs: {calorie_need:.3f} cal")
for key, value in macronutrient_distribution_info.items():
    print(f"{key.capitalize()}: {value*100}%")
print("Meal plan:")
print(recommendation)
update_your_health_worksheet(gender, age, objective)
