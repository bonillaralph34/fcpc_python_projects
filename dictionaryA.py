print("1. Add Number")
print("2. Search Number")
print("3. Exit the program")
dictContact = {}
loop = True
while loop:

    user_choice = input("Enter your choice:")

    if user_choice == '1':
        inp_name = input("Enter your name: ")
        inp_number = input("Enter your number: ")
        print()

        dictContact[inp_name] = inp_number


    elif user_choice == '2':
        dictContact[inp_name] = inp_number
        search = input("Enter the name: ")
        print(dictContact[search])

    else:
        break
