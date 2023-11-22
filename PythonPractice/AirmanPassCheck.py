# Challenge by a friend to see what I'd do with the prompt
# make a function that returns "True" if the password is valid, but a string like "Password too short" if it's too short
# it accepts 1 string argument, password_to_validate

def check_password(password: str):
    acceptable_password_length = 16
    print(True if len(password) >= acceptable_password_length else f"Password is too short")


password_to_check = input(f"Input Password:")
check_password(password_to_check)
