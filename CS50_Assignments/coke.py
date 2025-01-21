am = 50

while(am>0):
    print("Amount Due:",(am))
    a = int(input("Insert Coin: "))
    if a == 25 or a == 10 or a == 5 :
        am = am-a

x = abs(am)
print("Change Owed:" , x)
 