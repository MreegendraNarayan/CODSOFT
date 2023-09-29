import random
import string
def generating_passcode(length):
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    digits=string.digits
    special_char=string.punctuation

    difficulty=input("Enter complexity of your passcode (low,medium,high): ").lower()
    if difficulty=="low":
        chars=lowercase+digits
    elif difficulty=="medium":
        chars=lowercase+uppercase+digits
    elif difficulty=="high":
        chars=lowercase+uppercase+digits+special_char
    else:
        print("Wrong choice of difficulty lvl, aap dream11 pe team banao, ye me karta hoon")
        chars=lowercase+uppercase+digits
    passcode=''.join(random.choice(chars)for _ in range(length))
    return passcode
def main():
    try:
        length=int(input("Enter the length of the passcode: "))
        if length <=0:
            print("Bhai, 0 length ka passcode?")
        else:
            passcode=generating_passcode(length)
            print("Generated Passcode: "+passcode)
    except ValueError:
        print("Invalid input mate, can you please enter a valid integer for the passcode?")
if __name__=="__main__":
    main()
            