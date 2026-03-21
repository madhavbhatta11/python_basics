#data types in python
# #1 lists in pyton
# list1=[input(" first word "),input("second word "),input("third word ")]
# if list1[0]=="hello":
#     print("first word is hello")
# else:
#     print("first word is not hello")
# print(list1)
# print(list1[0:2])
# list1.append(input("fourth word "))
# print(list1)
# list1.insert(2,input("fifth word "))    
# print(list1)
# list1.remove(input("enter word to remove "))    
# print(list1)
# list1.pop(0)
# print(list1)
# list1.clear()   
# print(list1)

#about tuple
#tuple1=(1,2,3,4,5,"name","roll","contact")
#print(tuple1)

#to-do list using list
tasks = []

while True:
    print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!",tasks)

    elif choice == "2":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found!")

    elif choice == "3":
        # print("Your Tasks:", tasks)
        if not tasks:
            print("No tasks added yet!")  
        else:  
            for i, t in enumerate(tasks):
                print(i+1, t)

    elif choice == "4":
        print("Exiting program...")
        break

