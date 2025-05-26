def calculate_bmi(height, weight):

    print("height:", height)
    print("weight:", weight)
    bmi = weight / (height ** 2)
    print("bmi:", bmi)
    if bmi<18.5:
        print("Underweight")
    elif 18.5<=bmi<=25.0:
        print("Normal weight")
    else:
        print("Overweight")


calculate_bmi(weight=57, height=1.73)