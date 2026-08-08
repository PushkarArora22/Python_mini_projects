def main():
    password=input("Enter a password")
    print(checker(password))

def checker(password):
    has_upper=False
    has_digit=False
    for i in password:
        if i.isupper():
            has_upper=True
        if i.isdigit():
            has_digit=True
    if len(password)>=8 and has_upper==True and has_digit==True:
        return "Strong"
    else:
        return "Weak"

main()
