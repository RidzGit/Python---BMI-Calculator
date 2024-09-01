height = input("Enter your height : ")
weight = input("Enter your weight : ")
b = int(weight)
a = float(height)
bmi = b / a**2
bmi_int = int (bmi)
print(bmi_int)
if (bmi_int < 18.5) :
    print("Underweight")
elif (18.5 < bmi_int < 24.9) :
    print("Healthy Weight")
elif (25 < bmi_int < 29.9) :
    print("Over Weight")
elif (30 < bmi_int < 39.9) :
    print("Obese")
else :
    print("Severely Obese")