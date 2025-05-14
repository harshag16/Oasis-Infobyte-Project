print("Welcome to the BMI Calculator!")

try:
    weight = float(input("Please enter your weight in kilograms: "))

    height_input = input("Please enter your height in meters: ")
    if not height_input.strip():
        raise ValueError("Height entry is compulsory!")

    height = float(height_input)

    bmi = weight / height**2

    if bmi < 18.5:
        category = "You are Underweight"
    elif bmi < 24.9:
        category = "You have Normal weight"
    elif bmi < 29.9:
        category = "You are Overweight"
    else:
        category = "You are Obese"

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")

except ValueError as e:
    print(f"Error: {e}")
