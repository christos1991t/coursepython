# oefening 1
liters = input('Insert ammount of liters:')


def convert(liters):
    liters = float(liters)
    cubic = liters/1000
    return cubic


result = convert(liters)

print(f'That is {result} cubic meters')

# oefening 2

user_password = input("Enter new password: ")


def strength(password):

    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    uppercase = False

    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


print(strength(user_password))
