# Building a Daily Protein and Calorie Calculator in Python

## Overview
You're going to build a program that calculates personalized daily calorie and protein requirements based on user inputs like weight, height, age, gender, and activity level.

## Understanding the Science First

Before coding, you need to understand the formulas:

### 1. BMR (Basal Metabolic Rate)
This is the number of calories your body burns at rest. The most common formula is the **Mifflin-St Jeor Equation**:

- **For Men**: BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age) + 5
- **For Women**: BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age) - 161

### 2. TDEE (Total Daily Energy Expenditure)
This is your BMR multiplied by an activity factor:

- Sedentary (little/no exercise): BMR × 1.2
- Lightly active (exercise 1-3 days/week): BMR × 1.375
- Moderately active (exercise 3-5 days/week): BMR × 1.55
- Very active (exercise 6-7 days/week): BMR × 1.725
- Extremely active (physical job + exercise): BMR × 1.9

### 3. Protein Requirements
General guidelines (in grams per kg of body weight):
- Sedentary: 0.8 g/kg
- Lightly active: 1.0-1.2 g/kg
- Moderately active: 1.2-1.6 g/kg
- Very active/athlete: 1.6-2.2 g/kg

---

## Program Structure Planning

Think of your program as having these main components:

1. **Input Collection** - Get data from the user
2. **Data Validation** - Make sure inputs are valid
3. **Calculation Functions** - Do the math
4. **Output Display** - Show results to the user
5. **Main Program Flow** - Tie everything together

---

## Step-by-Step Development Guide

### Step 1: Set Up Your Python File
Create a new file called `calorie_calculator.py` and think about what you'll need at the top of your file. Consider:
- Do you need any import statements? (Hint: you might not need any for a basic version)
- Should you add a comment explaining what the program does?

---

### Step 2: Create a Function to Get User Input

**Goal**: Write a function that collects all necessary information from the user.

**Things to consider**:
- What data type should each input be? (string, integer, float?)
- Should you use `input()` for getting user responses?
- How will you handle the conversion from string to numbers?
- What information do you need to collect?
  - Age
  - Gender
  - Weight (decide on units: kg or lbs?)
  - Height (decide on units: cm or inches?)
  - Activity level

**Helpful hint**: You can create a function like `get_user_data()` that returns all this information. Think about whether to return them as separate values or as a dictionary.

**Example structure** (don't copy, understand the pattern):
```
function get_user_data():
    ask for age
    ask for gender
    ask for weight
    ask for height
    ask for activity level
    return all the data
```

---

### Step 3: Create Input Validation Functions

**Goal**: Ensure the user enters valid data.

**Create helper functions** to validate:

1. **Numeric inputs** - Check if age, weight, height are positive numbers
2. **Gender input** - Check if it's 'male' or 'female' (or M/F)
3. **Activity level** - Check if it's one of the valid options

**Think about**:
- Should you use if/else statements or try/except for validation?
- What should happen if the user enters invalid data? Ask again? Show error?
- Should you convert inputs to lowercase for easier comparison?

**Pattern to consider**:
```
function validate_positive_number(value, field_name):
    check if value is positive
    if not, show error
    return True or False

function validate_gender(gender):
    check if gender is valid
    return True or False
```

---

### Step 4: Handle Unit Conversions (If Needed)

**Goal**: If you want to support multiple units, create conversion functions.

**Consider creating**:
- Function to convert pounds to kilograms (kg = lbs / 2.205)
- Function to convert inches to centimeters (cm = inches × 2.54)

**Ask yourself**:
- Will you let users choose their preferred units?
- Or will you standardize on one system?

---

### Step 5: Create BMR Calculation Function

**Goal**: Calculate Basal Metabolic Rate using the Mifflin-St Jeor equation.

**Function structure to think about**:
```
function calculate_bmr(weight_kg, height_cm, age, gender):
    if gender is male:
        use male formula
    else:
        use female formula
    return bmr_value
```

**Important**:
- Make sure weight is in kg
- Make sure height is in cm
- The formulas are different for men and women
- Use parentheses carefully in your calculations!

---

### Step 6: Create TDEE Calculation Function

**Goal**: Calculate Total Daily Energy Expenditure based on activity level.

**Think about**:
- How will you represent activity levels? (numbers 1-5? strings like "sedentary"?)
- You need to multiply BMR by the appropriate activity factor
- Consider using a dictionary to map activity levels to multipliers

**Example approach**:
```
function calculate_tdee(bmr, activity_level):
    create a mapping of activity levels to multipliers
    look up the multiplier for the given activity level
    multiply bmr by the multiplier
    return tdee
```

**Activity multipliers reminder**:
- Sedentary: 1.2
- Lightly active: 1.375
- Moderately active: 1.55
- Very active: 1.725
- Extremely active: 1.9

---

### Step 7: Create Protein Calculation Function

**Goal**: Calculate daily protein needs based on weight and activity level.

**Think about**:
- Different activity levels need different amounts of protein per kg
- You'll multiply weight (in kg) by a protein factor
- Consider using a dictionary similar to the TDEE function

**Pattern**:
```
function calculate_protein(weight_kg, activity_level):
    create a mapping of activity levels to protein factors (g/kg)
    look up the factor for the given activity level
    multiply weight by the factor
    return protein_grams
```

**Protein factors reminder**:
- Sedentary: 0.8 g/kg
- Lightly active: 1.0-1.2 g/kg (pick a value like 1.1)
- Moderately active: 1.2-1.6 g/kg (pick a value like 1.4)
- Very active: 1.6-2.2 g/kg (pick a value like 1.9)

---

### Step 8: Create a Display Results Function

**Goal**: Show the results in a clear, user-friendly format.

**Consider**:
- Rounding numbers to 1 or 2 decimal places
- Using formatted strings (f-strings) for nice output
- Adding units (calories, grams)
- Maybe showing a breakdown of the calculation?

**Think about showing**:
- BMR value
- TDEE value (total daily calories)
- Protein requirement in grams
- Maybe additional context or tips?

**Example output format**:
```
=== YOUR DAILY NUTRITIONAL NEEDS ===
Basal Metabolic Rate (BMR): XXXX calories
Total Daily Energy Expenditure (TDEE): XXXX calories
Recommended Daily Protein: XXX grams
```

---

### Step 9: Create the Main Function

**Goal**: Orchestrate the entire program flow.

**Your main function should**:
1. Welcome the user
2. Call the input function to get user data
3. Validate all inputs (maybe in a loop until valid)
4. Call the BMR calculation function
5. Call the TDEE calculation function
6. Call the protein calculation function
7. Call the display function to show results
8. Ask if they want to calculate again (optional enhancement)

**Structure**:
```
function main():
    print welcome message
    get user data
    calculate bmr
    calculate tdee
    calculate protein
    display results
```

---

### Step 10: Add the Program Entry Point

At the bottom of your file, add:
```python
if __name__ == "__main__":
    main()
```

**What does this do?**
This ensures your main function only runs when the script is executed directly, not when imported as a module.

---

## Testing Your Program

### Test Cases to Try:

1. **Basic test**:
   - Age: 30, Gender: Male, Weight: 70kg, Height: 175cm, Activity: Moderately active
   - Expected BMR ≈ 1663 calories
   - Expected TDEE ≈ 2578 calories

2. **Different gender**:
   - Age: 25, Gender: Female, Weight: 60kg, Height: 165cm, Activity: Lightly active
   - Expected BMR ≈ 1370 calories
   - Expected TDEE ≈ 1884 calories

3. **Input validation**:
   - Try negative numbers
   - Try text where numbers are expected
   - Try invalid activity levels

---

## Enhancement Ideas (After Basic Version Works)

Once you have the basic program working, consider adding:

1. **Goal-based adjustments**:
   - Ask if they want to lose weight, gain weight, or maintain
   - Adjust TDEE by ±500 calories accordingly

2. **BMI calculation**:
   - Calculate and display Body Mass Index
   - Formula: BMI = weight(kg) / (height(m))²

3. **Macronutrient breakdown**:
   - Calculate carbs and fats too
   - Common ratio: 40% carbs, 30% protein, 30% fat

4. **Save results to file**:
   - Let users save their results to a text file
   - Track progress over time

5. **Better user interface**:
   - Menu system with options
   - Ability to use different unit systems (metric/imperial)
   - Color-coded output using libraries like `colorama`

6. **Error handling**:
   - Use try/except blocks to handle unexpected inputs gracefully
   - Provide helpful error messages

---

## Key Python Concepts You'll Practice

- **Functions**: Breaking code into reusable pieces
- **Input/Output**: Getting user data and displaying results
- **Data types**: Strings, integers, floats
- **Conditionals**: if/else statements for gender and validation
- **Dictionaries**: Mapping activity levels to multipliers
- **String formatting**: f-strings for nice output
- **Type conversion**: Converting strings to numbers
- **Return values**: Passing data between functions

---

## Common Pitfalls to Avoid

1. **Forgetting to convert input()**: The `input()` function always returns a string. Use `int()` or `float()` to convert.

2. **Order of operations**: Use parentheses in formulas to ensure correct calculation order.

3. **Case sensitivity**: "Male" ≠ "male". Use `.lower()` to standardize.

4. **Division vs integer division**: In Python 3, `/` gives you floats, which is what you want for these calculations.

5. **Not handling invalid input**: Always validate user input before using it in calculations.

---

## Getting Started

1. Open your Python editor or IDE
2. Create a new file called `calorie_calculator.py`
3. Start with Step 1 and work through each step
4. Test frequently as you build each function
5. Don't be afraid to use `print()` statements to debug
6. Refer back to the formulas at the top when implementing calculations

Good luck! Remember, programming is about problem-solving and iteration. Your first version doesn't need to be perfect—get it working, then improve it.
