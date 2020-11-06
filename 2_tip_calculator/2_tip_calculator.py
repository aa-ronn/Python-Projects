from os import system, name


def cls():
    # windows
    if name == 'nt':
        _ = system('cls')
    #mac and linux
    else:
        _ = system('clear')


go = True
while go:
    bill = float(input("What is the cost of the meal? "))
    tip = input("Tip percentage? ")

    # remove % if given
    if "%" in tip:
        tip = tip.replace("%", "")

    tip = float(tip)

    num_people = int(input("How people are spilting the bill? "))

    print("The cost for each person is ${:.2f}".format(
        round(((bill/num_people)*(tip/100+1)), 2)))

    # go again?
    restart = input("\n\nStart over (Y/N)?")
    if restart == "Y" or restart == "y":
        cls()
    else:
        go = False
