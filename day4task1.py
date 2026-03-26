# square_num=[x for x in range(1,10)]
# print(square_num)
# import math
# squares = [x**2 for x in range(1, 11)]
# print(squares)
# y=int(input("Enter a number to find its square root: "))
# print(math.sqrt(y))
file = open("test.txt", "w")
file.write("Hello World")
file.close()

file = open("test.txt", "r")
# print(file.read())
file.close()

file = open("test.txt", "a+")
file.write("\nWelcome to Python programming!" \
"\nThis is a new line added to the file." \
"\nFile handling is important for data storage.")
print("Content appended to file.")
print("Updated file content:")
file.seek(0)  # Move cursor to beginning before reading

print(file.read())
# print(file.read())
file.close()