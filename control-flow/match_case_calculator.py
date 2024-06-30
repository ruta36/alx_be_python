first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

match  operator  : 
    case "+" :
        result = first_num + second_num
        print(f"The result is {result:.3f}.")
    case "-" :
        result = first_num - second_num
        print(f"The result is {result:.3f}.")
    case "*" :
        result = first_num * second_num
        print(f"The result is {result:.3f}.")
    case "/" :
        if second_num == 0 :
            print("Cannot divide by zero")
        else :
            result = first_num / second_num
            print(f"The result is {result:.3f}.")
    case _ :
        print("The operator you enter does not exist.")

