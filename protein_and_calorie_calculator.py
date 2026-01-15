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
        Calculate Basal Metabolic Rate using Harris-Benedict equation.
        
        Args:
            weight (int): Weight in kilograms
            gender (str): 'male' or 'female'
            age (int): Age in years
            height (int): Height in centimeters
        
        Returns:
            float: BMR in calories per day
        
        Reference: Harris, J. A., & Benedict, F. G. (1918)
        """
    
    while True:
        if gender.lower() == GENDER_MALE:
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        elif gender.lower() == GENDER_FEMALE:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age)
        else:
            print("That is not a gender. Please")
            print("try again.")
            gender = input("Please enter 'male' or 'female': ")
            continue
        return bmr

def see_activity_level(bmr, weight, activity_level):
    if activity_level == 1:
        bmr *= 1.2
        protein = 0.8 * weight
    elif activity_level == 2:
        bmr *= 1.375
        protein = 1.1 * weight
    elif activity_level == 3:
        bmr *= 1.55
        protein = 1.4 * weight
    elif activity_level == 4:
        bmr *= 1.725
        protein = 1.9 * weight
    elif activity_level == 5:
        bmr *= 1.9
        protein = 2.5 * weight
    return bmr, protein

def show_results(bmr, protein):
    print("=" * 15, "Results", "=" * 15)
    print(f"Your basal metabolic rate is {round(bmr, 3)} calories.")
    print(f"Your protein requirement is {round(protein, 1)} grams.")
    print("=" * 40)

def main():
    # Get all inputs
    weight = get_weight()
    gender, age, height, activity_level = get_other_user_input()
    # Calculate BMR
    bmr = calculate_bmr(weight, gender, age, height)
    # Apply activity level
    bmr, protein = see_activity_level(bmr, weight, activity_level)
    # Show results
    show_results(bmr, protein)

if __name__ == "__main__":
    main()                                                                                                                                                                                                                  