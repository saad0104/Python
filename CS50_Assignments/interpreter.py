d = input("Expression: ").strip()

x, y, z = d.split(" ")

x = float(x)
z = float(z)

match y :
    case "+":
        print(x+z)
    case "-" :
        print(x-z)
    case "*" :
        print(x*z)
    case "/" :
        print(x/z)
        
