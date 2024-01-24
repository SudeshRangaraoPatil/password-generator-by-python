import random
import string

print("welcom to random password generator")
def main():

    length=int(input("enter length of password"))
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digit=string.digits
    symbol=string.punctuation
    combine=lower+upper+digit+symbol
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    main()
main()