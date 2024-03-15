def calculate_caloric_needs(age, weight, height, gender, activity_level):
    """
    Function that calculates calories like the Harris-Benedict Equation
    """

age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
gender = input("Enter 'M' for male or 'F' for female: ").upper()
activity_level = input("Enter your activity level (sedentary, light, moderate, active, very active): ").lower()