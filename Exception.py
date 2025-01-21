# try :
#     x = int(input("What's X? "))

# except ValueError:
#     print("X is not an Integer")
    
# else : 
#     print(f"X is {x}")         # else block executes when the except block doesn't executes. 
    
# finally : 
#     print("Finally!")         # Finally always executes 


def main():
    x = get_int("What's int X? ")
    print(f"X is {x}")

def get_int(prompt):
    while True:
        try :
            return int(input(prompt))
    
        except ValueError:
            # print("X is not an integer")
            pass      # gets out of the block without doing anything
    
main()


# custom excepton can be raised using 'raise' keyword.