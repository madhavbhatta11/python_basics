#match _ case statement
num = int(input("Enter the number: "))

match num:
    case 0:
        print('The number is "Zero"')
    case 1:
        print("The number is 1")
    case 2:
        print("The number is <= 2")
    case _:
        print("The value is:", num)
