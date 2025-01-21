fruits = {
    'apple' : 130,
    'avocado california' : 50,
    'banana' : 110,
    'cantaloupe' : 50,
    'grapefruit' : 60,
    'grapes' : 90,
    'honeydew Melon' : 50,
    'kiwifruit' : 90,
    'lemon' : 15,
    'lime' : 20,
    'nectarine' : 60,
    'orange' : 80,
    'peach' : 60,
    'pear' : 100,
    'pineapple' : 50,
    'plums' : 70,
    'strawberries' : 50,
    'sweet cherries' : 100,
    'tangreine' : 50,
    'watermelon' : 80
}
    
inp = input("Item: ").lower()
     
for key in fruits:
    if key in inp:
        print("Calories:" ,fruits[key])