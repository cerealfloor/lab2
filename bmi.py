def calculate_bmi(height,weight):
    print("Height ="+ str(height))
    print("Weight ="+ str(weight))
    bmi=weight/(height*height)
    print("Your bmi is :" + str(bmi))
    if bmi<18.5:
        print("You are under weight")
        print("-1")
    elif bmi>18.4 and bmi<25:
        print("Your weight is normal")
        print("0")
    else:
        print("You are over weight")
        print("1")


calculate_bmi(weight=71,height=1.72)