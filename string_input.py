"""Function to get user input as a string up to a maximum length."""

STRING_MAX_LENGTH = 30

def user_input() -> str:
    """Function to read user input, store in a variable, and return an error
    if the input is longer than STRING_MAX_LENGTH characters.

    :return: user input as string
    """
    while (True):
        user_string = input("Enter stock name (less than 30 characters): ")

        if len(user_string) > STRING_MAX_LENGTH:
            print("Error! Input length must not exceed 30 characters!")
        else:
            return user_string