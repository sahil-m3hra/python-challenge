# Write python code to calculate the BMI (Body mass index).
# Accept height and weight from user.

height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
bmi = (weight)/(height**2)
print(f"Your BMI is: {round(bmi,2)}")