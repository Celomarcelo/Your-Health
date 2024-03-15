def calculate_caloric_needs(age, weight, height, gender, activity_level):
    """
    Function that calculates calories like the Harris-Benedict Equation
    """

age = int(input("Enter your age: "))
def validate_age(age):
    """
    Function to validate age
    """
    try:
        age = int(age)
        if 18<= age <= 100:
            raise ValueError("Age must be a positive integer between 18 and 100.")
        return age
    except ValueError:
        print("Invalid input for age. Please enter a valid integer.")
        return None

while age is None:
    age = validate_age(input("Enter your age: "))
    
weight = float(input("Enter your weight in kg: "))
def validate_weight(weight):
    """
    Function to validate weight
    """
    try:
        weight = float(weight)
        if 30 <= weight <= 200:
            raise ValueError("Weight must be a positive number between 30 and 200.")
        return weight
    except ValueError:
        print("Invalid input for weight. Please enter a valid number.")
        return None

while weight is None:
    weight = validate_weight(input("Enter your weight in kg: "))
    
height = float(input("Enter your height in meters: "))
def validate_height(height):
    """
    Function to validate height
    """
    try:
        height = height.replace(',', '.')
        height = float(height)
        if 1 <= height <= 2.5:
            raise ValueError("Height must be a positive number between 1 and 2.5.")
        return height
    except ValueError:
        print("Invalid input for height. Please enter a valid number.")
        return None

while height is None:
    height = validate_height(input("Enter your height in meters: "))

gender = input("Enter 'M' for male or 'F' for female: ").upper()
def validate_gender(gender):
    """
    Function to validate gender
    """
    if gender.upper() not in ['M', 'F']:
        print("Invalid input for gender. Please enter 'M' for male or 'F' for female.")
        return None
    return gender.upper()

while gender is None:
    gender = validate_gender(input("Enter 'M' for male or 'F' for female: "))
    
    
activity_level = input("Enter your activity level (sedentary, light, moderate, active, very active): ").lower()
def validate_activity_level(activity_level):
    """
    Function to validate activity level
    """
    valid_levels = ['sedentary', 'light', 'moderate', 'active', 'very active']
    if activity_level.lower() not in valid_levels:
        print("Invalid input for activity level. Please choose from: sedentary, light, moderate, active, very active.")
        return None
    return activity_level.lower()

while activity_level is None:
    activity_level = validate_activity_level(input("Enter your activity level (sedentary, light, moderate, active, very active): "))
