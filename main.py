names = []

def add():
    # choice = input("How many names do you want to add :")
    # for index in range(int(choice)):
    name = input("please write name here: ")
    names.append(name)
    print("Thank you! '" + name + "' has been added! \n **************")

def deleteName():
    showName()
    delName = input("Who do you want to delete? ")
    try:
        names.remove(delName)
        print(delName + " has been deleted!")
    except:
        print("Please enter name instead")


def showName():
    print("*******************************")
    print("Here are the names that you input")
    if not names:
        print("No names available")
    else:
        for index in range(len(names)):
            print(index + 1, ".", names[index])


def main():
    choice = ''
    while choice != 0:
        print("Welcome to names dictionary !!")
        print("1. To add name")
        print("2. To view name")
        print("3. To delete name")
        print("0. To stop the program")
        try:
            choice = int(input("Press your choice here: "))
            if choice == 1:
                add()
            elif choice == 2:
                showName()
            elif choice == 3:
                deleteName()
            elif choice == 0:
                break
        except:
            print("Something is wrong")
    print("Thank you for using ! come back again!")


if __name__ == "__main__":
    main()
