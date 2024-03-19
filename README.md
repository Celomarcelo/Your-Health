# Your Health

Calculate your diet according to your goal.

## Overview

This project aims to assist users in determining their dietary needs based on various factors such as age, weight, height, gender, and activity level. It provides functions to calculate caloric needs, determine macronutrient distribution, validate user inputs, generate meal plans, and analyze data from a Google Sheets document.

## Prerequisites

Before running the code, ensure you have the following dependencies installed:

- [gspread](https://gspread.readthedocs.io/en/latest/)
- [oauth2client](https://oauth2client.readthedocs.io/en/latest/)
- [pprint](https://docs.python.org/3/library/pprint.html)

You also need to set up authentication with Google Sheets API and provide the necessary credentials (`creds.json`).

## Usage

1. Run the script.
2. Follow the prompts to enter your age, weight, height, gender, activity level, and goal.
3. The script will calculate your daily caloric needs, display macronutrient distribution, suggest a meal plan based on your goal, and provide insights based on data analysis.

## Functions

### `calculate_caloric_needs(age, weight, height, gender, activity_level)`

Calculates caloric needs based on the Harris-Benedict Equation.

### `macronutrient_distribution(objective)`

Calculates macronutrient distribution based on the user's goal.

### `validate_age(age)`

Validates the user's age input.

### `validate_weight(weight)`

Validates the user's weight input.

### `validate_height(height)`

Validates the user's height input.

### `validate_gender(gender)`

Validates the user's gender input.

### `validate_activity_level(activity_level)`

Validates the user's activity level input.

### `validate_objective(objective)`

Validates the user's goal input.

### `meal_plan(objective)`

Generates a meal plan based on the user's goal.

### `update_your_health_worksheet(gender_column_name, age_column_name, objective_column_name)`

Updates the Your Health worksheet with new user data.

### `count_gender(sheet, column_name)`

Counts occurrences of genders (M and F) in a specific column of the worksheet.

### `count_objective(sheet, column_name)`

Counts occurrences of objectives (weight loss, muscle mass gain, maintenance) in a specific column of the worksheet.

## Function Testing Summary

The table below summarizes the behavior of each function in the code and whether they passed or failed the tests:
