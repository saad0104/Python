name = input("What's your name?")

# if name == "Harry":
#     print("Gryfindor")
# elif name == "Hermione":
#     print("Gryfindor")
# elif name == "Ron":
#     print("Gryfindor")
# elif name == "Draco":
#     print("Slytherin")
# else :
#     print("Who?")

match name :
    case "Harry" | "Hermione" | "Ron":
        print("Gryfindor")
    # case "Hermione":
    #     print("Gryfindor")
    # case "Ron":
    #     print("Gryfindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
        