weight = float(input("Enter weight here: "))
height = float(input("Enter height here: "))

BMI=weight/(height/100)**2 

if BMI <= 18.4:
    print("you are underweight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <= 29.9:
    print("you are overweight")
elif BMI <= 34.9:
    print("you are severely overweight")
elif BMI <= 39.9:
    print("you are obese")
else:
    print("you are severely obese")

