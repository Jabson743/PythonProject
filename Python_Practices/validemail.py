import email


def email_validation(email):
    email = r'[A-z][a-z]* + \d'
    address = input("Enter your email address: ")
    if email == email:
        return "This email address is valid"
    else:
        return "This email address is invalid"

print(email_validation(email))