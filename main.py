def encode(password):
    result_str = ""
    for i in password:
        i = int(i)
        result = i + 3
        if result >= 10:
            result -= 10
        result_list.append(result)
        result = 0
    for j in result_list:
        result_str += str(j)
    return result_str
while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    user_input = input("Please enter an option: ")
    if user_input == "1":
        result_list = []
        result = 0
        result_str = ""
        password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
        print()

        encoded_password = encode(password)
    elif user_input == "2":
        print("The encoded password is", encoded_password, ", and the original password is", password + ".")
        print()
    elif user_input == "3":
        exit()