def main():
    
    ti = str(input("What time is it?"))
    t = convert(ti)
    # print(t)
    if t >= 7 | t <= 8 :
        print("breakfast time")
        
    elif t >= 12 | t<= 13 :
        print("lunch time") 
        
    elif t>= 18 | t<= 19 :
        print("dinner time")
     

def convert(time):
    x ,y = time.split(":")
    x = int(x)
    return x
    


if __name__ == "__main__":
    main()