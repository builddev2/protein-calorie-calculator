# import argparse
GENDER_MALE = "male"
GENDER_FEMALE = "female"

def get_weight():
    while True:
        try:
            weight = int(input("What is your weight in kilograms? "))
            if weight <= 0 or weight > 1250:
                print("Weight must be between 1 and 1250.")
                continue
            return weight
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_other_user_input():
    print("=============================================")
    while True:
        gender = input("What is your gender? (male/female) ")
        if gender in [GENDER_MALE, GENDER_FEMALE]:
            break
        print("Please enter 'male' or 'female'.")
    print("=============================================")
    while True:
        try:
            age = int(input("What is your age in years? "))
            if 0 < age <= 150:
                break
            print("Please enter a realistic age.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("=============================================")
    while True:
        try:
            height = int(input("What is your height in centimeters? "))
            if 0 < height <= 315:
                break
            print("Please enter a realistic height.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("=============================================")
    print("Activity levels:")
    print("1 - Sedentary (little to no exercise)")
    print("2 - Lightly active (exercise 1-3 days/week)")
    print("3 - Moderately active (exercise 3-5 days/week)")
    print("4 - Very active (exercise 6-7 days/week)")
    print("5 - Extremely active (physical job + exercise)")
    while True:    
        try:
            activity_level = int(input("Choose your activity level (1-5): "))
            if activity_level > 5 or activity_level <= 0:
                print("Invalid number.")
                continue
            return gender, age, height, activity_level
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        

def calculate_bmr(weight, gender, age, height):
    """
    Calculate Basal Metabolic Rate using Mifflin-St Jeor equation.

    Args:
        weight (int): Weight in kilograms
        gender (str): 'male' or 'female'
        age (int): Age in years
        height (int): Height in centimeters

    Returns:
        float: BMR in calories per day

    Reference: Mifflin, M. D., et al. (1990)
    """
    if gender.lower() == GENDER_MALE:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:  # female
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return bmr

def calculate_tdee(bmr, activity_level):
    """
    Calculate Total Daily Energy Expenditure based on activity level.

    Args:
        bmr (float): Basal Metabolic Rate in calories
        activity_level (int): Activity level (1-5)

    Returns:
        float: TDEE in calories per day
    """
    activity_multipliers = {
        1: 1.2,    # Sedentary
        2: 1.375,  # Lightly active
        3: 1.55,   # Moderately active
        4: 1.725,  # Very active
        5: 1.9     # Extremely active
    }
    return bmr * activity_multipliers[activity_level]

def calculate_protein(weight, activity_level):
    """
    Calculate daily protein requirements based on weight and activity level.

    Args:
        weight (int): Weight in kilograms
        activity_level (int): Activity level (1-5)

    Returns:
        float: Protein requirement in grams per day
    """
    protein_factors = {
        1: 0.8,   # Sedentary
        2: 1.1,   # Lightly active
        3: 1.4,   # Moderately active
        4: 1.9,   # Very active
        5: 2.0    # Extremely active (adjusted from 2.5 to stay within guidelines)
    }
    return weight * protein_factors[activity_level]

def show_results(bmr, tdee, protein):
    """
    Display the calculated nutritional results.

    Args:
        bmr (float): Basal Metabolic Rate in calories
        tdee (float): Total Daily Energy Expenditure in calories
        protein (float): Daily protein requirement in grams
    """
    print("\n" + "=" * 40)
    print("    YOUR DAILY NUTRITIONAL NEEDS")
    print("=" * 40)
    print(f"Basal Metabolic Rate (BMR): {round(bmr, 1)} calories")
    print(f"Total Daily Energy Expenditure (TDEE): {round(tdee, 1)} calories")
    print(f"Recommended Daily Protein: {round(protein, 1)} grams")
    print("=" * 40)

def main():
    # Get all inputs
    weight = get_weight()
    gender, age, height, activity_level = get_other_user_input()
    # Calculate BMR
    bmr = calculate_bmr(weight, gender, age, height)
    # Calculate TDEE
    tdee = calculate_tdee(bmr, activity_level)
    # Calculate protein requirements
    protein = calculate_protein(weight, activity_level)
    # Show results
    show_results(bmr, tdee, protein)

if __name__ == "__main__":
    main()                                                                                                                                                                                                                  