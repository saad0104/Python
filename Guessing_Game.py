from random import randint as rin


def green(text):
    return f"\033[92m{text}\033[0m"


print("\n **********  Guessing Game  ************ \n")
while True:
    # print(num)
    try :
        n = int(input("** Guess a number between 1 to 100 (123 to exit) : "))
    except ValueError:
        print("Please Enter an Integer.") 
    else:
        num = rin(1,100)
        if n == 123:
            print("See You!")
            break
    
        if n == num :
            print("Congrarulations! You guessed it Right. ")
        else :
            print("Woops.Make Another Choice.")
            print(f"You were {green(abs(num-n))} away")
            

