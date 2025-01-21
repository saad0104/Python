# from random import choice as c
import random

def green(text):
    return f"\033[92m{text}\033[0m"

print("\n******  Tossing the Coin  *******\n")

inp = str(input("Choose your side. : Heads or Tales ? : ")).lower().strip()
print(f"You Choose : {green(inp.capitalize())}")


if(inp == "heads" or inp == "tales"):
     
    # coin2 = c(["heads","tales"])
    coin = random.choice(["heads", "tales"])
    print(f"Toss Result : {green(coin.capitalize())}")

    if inp == coin:
        print(f"Congratulations! You {green("won")} the toss.")
    else :
        print(f"Woops. You {green("lost")} the toss.")
        
else:
    print("Please Enter in Correct Format.")