import string
import random


if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(input("Enter the desired password length: "))
    if plen < 8:
        print("Password length must be at least 8 characters.")
    else:
        s = []
        s.append(random.choice(s4))
        # s.append(random.choice(s1))  # at least one lowercase
        # s.append(random.choice(s2))  # at least one uppercase
        # s.append(random.choice(s3))  # at least one digit
        # s.append(random.choice(s4))  # at least one special character
        remaining_length = plen - 4  # remaining length after ensuring one of each type

    s.extend(random.choices(s1 + s2 + s3 + s4, k=remaining_length))
    s.extend(list(s1))  # add all lowercase
    s.extend(list(s2))  # add all uppercase
    s.extend(list(s3))  # add all digits
    s.extend(list(s4))  # add all special characters
    s.extend(list(s1))  # add all lowercase
    # random.shuffle(s)  # shuffle the list
    print("your password is: ")
    print("".join(random.sample(s, plen)))  # print the list as a string
    # print("".join(s[0:plen]))  # print the list as a string
    # Generate password
