x = str(input("Greeting: "))
x = x.lower().strip()
z = x.split(" ")[0]
# print(z)
if z[0:5]=="hello":
    print("$0")
else :
    if z[0]=="h":
        print("$20")
    else:
        print("$100")
