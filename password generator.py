import string
import random
if __name__ == "__main__":
    p1 = string.ascii_uppercase
    p2 = string.ascii_lowercase
    p3 = string.digits
    p4 = string.punctuation
    pass_len = int(input("Enter your password length: "))
    s = []
    s.extend(p1)
    s.extend(p2)
    s.extend(p3)
    s.extend(p4)
    random.shuffle(s)
    print("Your Password is: ","".join(s[0 : pass_len]))