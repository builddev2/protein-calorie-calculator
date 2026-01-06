weight = int(input("What is your weight in kilograms? "))
gender = input("What is your gender? (male/female) ")
age = int(input("What is your age? "))
height = int(input("What is your height in centimeters? "))
activity_level = input("What is your activity level? (1/2/3/4/5) ")

if gender == "male":
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
else:
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

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

print(f"Your basal metabolic rate is {round(bmr, 5)} calories.")
# print(f"Your total daily energy expenditure is {calories} calories.")
# protein_rounded = round(protein, 2) int(protein_rounded) if protein_rounded.is_integer() else protein_rounded
print(f"Your protein requirement is {round(protein, 2)} grams.")