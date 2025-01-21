 # students = {"Harry":"Gryffindor","Ron":"Gryffindor","Draco":"Slytherin"}

# print(students["Harry"])


# for st in students:
#     print(st)                # prints the keys
#     print(students[st])      # Prints the values stored in the keys


# In dictonary , the format is key:value

# students["Harry"]  -- >> Indicates the value stored in the key "Harry" of the dictionary "students" .


students = [
    {"name" : "Harry" , "house" : "Gryffindor" , "pet" : "Something"} ,
    {"name" : "Ron" , "house" : "Gryffindor" , "pet" : "Something"} ,
    {"name" : "Hermione" , "house" : "Gryffindor" , "pet" : "Something"} ,
    {"name" : "Draco" , "house" : "Slytherin" , "pet" : "Something"} ,       
]

for st in students:
    # print(st)                                     # Prints all the elements of the list
    print(st["name"] , st["house"] , st["pet"])     # Prints the values of the keys of the dictionaries
    