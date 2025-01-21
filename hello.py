# Comments

"""
x = input();
y = input();   Multiline commenting
print(x+y);
"""


# x = input(); # Function to take string input.

x = input("Name ")


print("Hello" , x)   # ',' prints a space automatically
#print() function automatically prints a newline.

print("Hello", x, end="",sep="@@@") 
# The deafult value of "end" in print function is '\n' which is a newline.
#Not to print a newline automatically.we have to change the value of end to nothing." end="" "
#The default value of 'sep' in print function is " " (a space).That means a space seperates two strings.
#To change the default string seperator of print function,we have to change the value of "sep=@@@"


print("Hello " + x)   # '+' represents Concatenation of strings.
 # Prints the string inside qoutation and the variable added with a '+' symbol.

#Format String
print(f"Hello {x}")   
 # f at the begining tells the compiler that this a specila type of string named Format String
 # so handle it accordingly.So it prints the value of the variable inside {}.Without f at the 
 # begining,it will print ' Hello {x} '.

#String 
'''
x = x.strip() # Removes Whitespace from the string
x = x.capitalize() # Capitilizes the first letter of the string
x = x.title()   # Capitilizes the first line of every word of the string
'''
x = x.strip().title()   

# We can do it like this also
# x = input().strip().title()  #mofo just did 8 lines code in just a single line 

first,last = x.split(" ")
#Splits the string.The character inside the qoutation(" ") is the seperator for the string.Usually it is a space.
#After spliting  puts the values into variables named first and last.

print("Hello",x)
print("Hello",last)  #Input- Saad Mahmud   #Output - Hello Mahmud





