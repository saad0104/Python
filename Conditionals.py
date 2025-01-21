# Conditional Symbols
 #   >   >=    <     <=   ==    !=

#   if     elif     else
#   or    and


x = int(input("X = "))
y = int(input("Y = "))

if x<y:
    print("X is less than Y")

elif x>y : 
    print("X is greater than Y")

else:
    print("X and Y are equal")



if x>y or x<y :
    print("X and Y are not equal")
else :
    print("X and Y are equal")