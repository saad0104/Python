
# x = int(input("What's X?"))

# if(x%2==0):

#     print(x ,"is even")

# else:
#     print(x,"is Odd")



def main():
    x = int(input("What is X : "))
    
    if(is_even(x)):
        print("Even")

    else:
        print("Odd")


def is_even(n):
    return (n%2==0)

    # if n%2==0:
    #     return True
    # else:
    #     return False
    

main()