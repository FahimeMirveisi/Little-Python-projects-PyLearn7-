
weight = float(input("Enter your weight(kg):"))
height = float(input("Enter your height(m):"))

BMI = weight / (height * height)

print("Your body mass index is: ")

if BMI <= 18.5:
    print("Underweight")
elif 18.5< BMI <= 24.9:
    print("Normal weight")
elif 24.9 < BMI <= 29.9:
    print("Overweight")
elif 29.9 < BMI <= 34.9:
    print("Obesity")
else:
    print("Extreme obesity")