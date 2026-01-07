def get_weight():
    try:
        weight = int(input("What is your weight in kilograms? "))
        if weight < 0 or weight > 1250:
            raise ValueError("Weight must be realistic.")
        return weight
    except ValueError:
        print("===Invalid input.===")
        return None

def get_other_user_input():
    print("=============================================")
    gender = input("What is your gender? (type male/anything else for female) ")
    print("=============================================")
    age = int(input("What is your age? "))
    print("=============================================")
    height = int(input("What is your height in centimeters? "))
    print("=============================================")
    print("Activity levels:")
    print("1 - Sedentary (little to no exercise)")
    print("2 - Lightly active (exercise 1-3 days/week)")
    print("3 - Moderately active (exercise 3-5 days/week)")
    print("4 - Very active (exercise 6-7 days/week)")
    print("5 - Extremely active (physical job + exercise)")
    activity_level = input("Choose your activity level (1-5): ")
    return gender, age, height, activity_level

def calculate_bmr(weight, gender, age, height):
    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

def see_activity_level(bmr, weight, activity_level):
    if activity_level == "1":
        bmr *= 1.2
        protein = 0.8 * weight
    elif activity_level == "2":
        bmr *= 1.375
        protein = 1.1 * weight
    elif activity_level == "3":
        bmr *= 1.55
        protein = 1.4 * weight
    elif activity_level == "4":
        bmr *= 1.725
        protein = 1.9 * weight
    elif activity_level == "5":
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
