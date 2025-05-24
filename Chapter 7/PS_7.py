#Problem 1
# num = int(input("Enter a number: "))
# i = 0
# for i in range(10):
#     i += 1
#     print(f"{num} X {i} = {num*i}")

#Problem 2
# l = ["Harry", "Soham", "Sachin", "Rahul","Sahil","Saleem"]

# for item in l:
#     if ("S" in item):
#         print("Namaste uncle",item)

#Aonther solution:
# l = ["Harry", "Soham", "Sachin", "Rahul","Sahil","Saleem"]
# for name in l:
#     if (name.startswith("S")):
#         print(f"Hello {name}")

#Problem 3: Problem 1 using while loop
# num = int(input("Enter a number: "))
# i = 0
# while(i<10):
#     i += 1
#     print(i*num)

#Problem 4
# n = int(input("Enter a number: "))
# i = 0
# for i in range(2,n):
#     if (n%i) == 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")

#Problem 5
# n = int(input("Enter a Number: "))
# i = 0
# sum = 0
# while(i<=n):
#     sum += i
#     i +=1

# print(sum)

#Problem 6
# n = int(input("Enter a number: "))
# product = 1
# for i in range(1,n+1):
#     product = product * i

# print(f"The factorial of {n} is : {product}")

#Problem 7
'''
n = 3
  *
 ***
*****
'''
# n = int(input("Enter a number:" ))
# for i in range(1, n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("")

#Problem 8
'''
n = 3
*
**
***
'''
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print("*"* i,end="")
#     print("")

#Problem 9
'''
n = 3
***
* *
***
'''
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     if (i == 1 or i ==n):
#         print("*"* n,end="")
#     else:
#         print("*" , end="")
#         print(" "* (n-2) , end="")
#         print("*" , end="")
#     print("")

#Problem 10
num = int(input("Enter a number: "))
i = 10

for i in range(1,11):
    print(f"{num} x {11-i} = {num*(11-i)}")
    

              




    
    