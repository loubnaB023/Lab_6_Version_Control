# this my first github addition 

# Loubna Benchakouk
def encode_password(password):
    if len(password) != 8 or not password.isdigit():
        print("Password must be an 8-digit string containing only integers.")

    encoded_password = ""

    for digit in password:
        shifted_digit = (int(digit) + 3)
        encoded_password += str(shifted_digit)

    return encoded_password

def decode_password(password):
    if len(str(password)) != 8
        print("Password must be an 8-digit string containing only integers.")
        return None
    decoded = ""
    for digit in str(password):
        decoded_int = int(digit) - 3
        decoded += str(decoded_int)
    return decoded_password

def main():
    while True:

        # print menu
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        option = input('Please enter an option:')

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            encoded_password = input("Please enter the encoded password: ")
            original_password = decode_password(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
        elif option == "3":
            break
        else:
            print("Invalid option. Please choose a valid option (1, 2, or 3).")


if __name__ == '__main__':
    main()
