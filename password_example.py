"""
Check Login Credentials

Password Checker. Created by Chenyuhan Shen. 24-11-2021
"""


def main():
    """Starting Program."""
    password = input("Enter a pass word")

    if check_password(password):
        print("Logged in")
    else:
        print("Illegal access")


def check_password(password):
    """Check if password is valid."""
    return password == "12345678"


main()
