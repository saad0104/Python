import sys

# command line arguments

# sys.argv is a list of strings which takes input from the command line.
# in sys.argv[0] its the name of the file that is being executing.
# sys.exit(..)  --> gets out of the program returning a string. 

 
if len(sys.argv)<2:
    sys.exit("Too Few Argument") 
elif len(sys.argv)>2 :
    sys.exit("Too many arguments")


print("I am", sys.argv[1])




