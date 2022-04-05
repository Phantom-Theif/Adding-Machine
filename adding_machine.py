while True:
    try:
        print("This is an adding machine")
        first_num = int(input("What is the first number you want to add? "))
        second_num = int(input("What is the second number you want to add? "))
        sum = first_num + second_num
        print("The sum of your two numbers are", sum)
        break
    except:
        print("your input is not correct...")