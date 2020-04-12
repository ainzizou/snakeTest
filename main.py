names = []


def add():
    # choice = input("How many names do you want to add :")
    # for index in range(int(choice)):
    name = input("please write name here: ")
    names.append(name)
    print("Thank you! Name has been added! \n **************")


def showName():
    print("*******************************")
    print("Here are the names that you input")
    if not names:
        print("No names available")
    else:
        for index in range(len(names)):
            print(index+1,".",names[index])


def main():
    choice = ''
    while choice != 0:
        print("Welcome to names dictionary !!")
        print("1. To add names")
        print("2. To vie names")
        print("0. To stop the program")
        choice = int(input("Press your choice here: "))
        if choice==1:
            add()
        elif choice==2:
            showName()

if __name__ == "__main__":
    main()
