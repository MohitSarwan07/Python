#If Elif Else Ladder:
a = int(input("Enter Your Age: "))
#if statement no. 1
if(a%2 == 0):
    print("a is an even number")
#End of statement no. 1
#if statement no. 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")
elif(a<0):
    print("You have entered an invalid negative age")
elif(a==0):
    print("You have entered 0 which is not a valid age")
else:
    print("You are below the age of consent")
#End of if statement no. 2

print("|End of Program|")