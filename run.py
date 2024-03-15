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
activity_level = input("Enter your activity level (sedentary, light, moderate, active, very active): ").lower()