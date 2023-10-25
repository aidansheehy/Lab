def encode():
    password = input("Please enter your password to encode:")
    global encoded_pass
    encoded_pass = ""
    for i in password:
        new_digit = int(i) + 3
        if new_digit >= 10:
            new_digit -= 10
        encoded_pass += str(new_digit)
    return encoded_pass


def main():

    option = '0'
    while option >= '0':
        print()
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = input("Please enter an option:")
        if option == '1':
            encode()
            print("Your password has been encoded and stored!")
        if option == '2':
            decode()
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}.")
        if option == '3':
            exit()

if __name__=='__main__':
    main()