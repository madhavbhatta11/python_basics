#exception handling in python
# try:
#         num=int(input("Enter a number: "))
#         if num<18:
#             print("You are a minor.")
#         else:
#             print("You are an adult,age",num,"can vote")  
#         # break  # Exit the loop if input is valid
# except:
#         print("Invalid input. Please enter a valid number.")


#with taking atleast one input
while True:
    try:
        num=int(input("Enter a number: "))
        if num<18:
            print("You are a minor.")
        else:
            print("You are an adult,age",num,"can vote")  
        break  # Exit the loop if input is valid
    except:
        print("Invalid input. Please enter a valid number.") 
else:       
    print("Invalid input. Please enter a valid number.")