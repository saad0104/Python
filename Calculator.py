# Addition,int and float type input,type conversion,printing desired digits 
# after floating point(round,f string),round() function.


#Arithmatic Operations--

#  +    -    *    /    %

# print(int(input("x ")) + int(input("y ")))   -->> Code of taking input and addition of two integer in just one line. 


x = float(input("What's x? "))
y = int(input("What's y? "))
 # To take int type input,we just have put the input() function inside the int() function.
 #To take float type input,   float(input())


#to converrt the string type data to integer   -->>  int(variable)
#x = int(x)

#z = x + y 
#print(z)


print(x + y)

print(f"{(x+y):,}")     # To print a comma on the thosands place,we can take the help of the format string aka f string.
#By putting the result like the previous line,we can do this.Be creful with spaces.


print(round(x+y,2))
#The round function rounds the number into desired places.In this case it prints 2 digits after the floating point.
#This can be done by using f string also.
print(f"{x+y:.2f}")

