Camel = str(input("camelCase: "))

print("snake_case: ",end="")
for c in Camel:
    if c.isupper():
        print("_"+c.lower(),end="")
    else:
        print(c,end="")