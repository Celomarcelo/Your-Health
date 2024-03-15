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
    
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
gender = input("Enter 'M' for male or 'F' for female: ").upper()
activity_level = input("Enter your activity level (sedentary, light, moderate, active, very active): ").lower()