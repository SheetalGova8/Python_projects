# Here's a simple BMI (Body Mass Index) calculator in Python:

def calculate_bmi(weight, height):
  bmi = weight / (height ** 2)
  return bmi

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print("Your BMI is: ", round(bmi, 2))

if bmi < 18.5:
  print("You are underweight")
elif bmi < 24.9:
  print("You are normal weight")
elif bmi < 29.9:
  print("You are overweight")
else:
  print("You are obese")