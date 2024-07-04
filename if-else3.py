##start

pwd: str = input("what's the password?")

if pwd == "python1234":
    print("we're in baby!")
else:
    print("aww, maybe try again?")


##more ways to write it

if not (pwd == "python1234"):
    print("aww, maybe try again?")
else:
    print("we're in baby!")

    #########

PASSWORD: str = "python1234" ##big letters imply on cons
if not (pwd == PASSWORD):
    print("we're in baby!")
else:
    print("aww, maybe try again?")

    ##end