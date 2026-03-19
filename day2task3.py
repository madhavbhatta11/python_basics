#loops
#for loop
for i in range(0,41):
    print(i)
#about loops
#for loop
fruit="Apple, ball"
for i in fruit:
  print(i)    
flist=["apple","banana","cfruit"]
for j in flist:
  print(j)
  for k in j:
    print(k)    
    # print(j)
# Range 
for i in range(0,10):# print up to 9
  print(i)
for m in range(0,11,2):
  print(m)

for n in range(1,10,2):
  print(n)
#do-while loop in python
while true:
  num=int(input("Enter the number"))
  if num>0:
    print("it is positive number")
    break
  else:
    print 

#about functions
def function_name( parameter ):
  pass
#Example of function

def isgreater(a, b):
  if a>b:
    print("first is greater")
  elif a<b:
    print("2nd is greater")
  else:
    print("equal")
a=int(input("Enter the first number"))
b=int(input("Enter 2nd number"))

isgreater(a, b)
c=int(input("Enter the THIRD number"))
d=int(input("Enter the FOURTH number"))
isgreater(c, d)
