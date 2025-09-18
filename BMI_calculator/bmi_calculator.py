def bmi_calculate(weight, height):
    return (weight)/(height**2)

def bmi_category(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'overweight'
    else:
        return 'obese'

if __name__ == "__main__":
    print("======BMI Calculator=========")

    weight = int(input("Enter weight in kg: \t"))
    height_in_cm = float(input("Enter height in cm: \t"))
    height = height_in_cm / 100

    bmi_value = bmi_calculate(weight, height)
    category = bmi_category(bmi_value)

    print(f"your BMI is {bmi_value:.2f} and your BMI category is: {category}")
