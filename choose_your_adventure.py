name = input("Type your name:")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and your can go from left to right, Which way to go? "
)

if answer == "left":
    answer = input("You come to a river, your can walk around it or swim accross? Try walk to walk around it or swim accross")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif(answer == "walk"):
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("No a valid option. You lose.") 

elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you want to cross?")
    if answer == "back":
        print("you go back and lose")
    
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to stranger. ")
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("No a valid option. You lose,")
    else:
        print("Not a valid option.You lose")
else:
    print("Not a valid option. You lose.")