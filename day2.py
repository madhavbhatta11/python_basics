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
    #adding condition in case
    case _ if num<0:
        print("number is ngetive")
    case _ if num!=1 and num1=2 and num>=0 and num !=0:
        print("Out of range , and number is ", num)

    
