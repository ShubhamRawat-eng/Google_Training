name = input("Enter your name: ")

match name:
    case "harry"| "hermione"| "ron":
        print("gryffindor")
    case "draco":
        print("slytherin")
    case _:
        print("Who?")