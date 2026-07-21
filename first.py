print("Simple Python calculator")
while True:
    first_num = float(input("Enter a number: "))
    second_num = float(input("Enter a 2nd number: "))


    choice = input("Enter operation(+, -, *, /, %, **): ")
    print(choice)
    
    if choice == "+":
        print(first_num, "+", second_num, "=", first_num + second_num)
    elif choice == "-":
        print(first_num, "-", second_num, "=", first_num - second_num)
    elif choice == "*":
        print(first_num, "*", second_num, "=", first_num * second_num)
    elif choice == "/":
        if second_num == 0:
            print("Cannot divide by 0.")
        else:
            print(first_num, "/", second_num, "=", first_num / second_num)
    elif choice == "%":
        print(first_num, "%", second_num, "=", first_num % second_num)
    elif choice == "**":
        print(first_num, "**", second_num, "=", first_num ** second_num)
    else:
        print("Invalid operator.")
    ask = input("Do you cant to calculate again? (y/n) ").lower()
    if ask == "n":
        print("byebye")
        break
        
        