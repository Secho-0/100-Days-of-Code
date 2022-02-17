from art import TREASURE 
print(TREASURE)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("Your journey onto the island begins, do you head Left or Right down the beach?")
beach = input(">")

if beach.lower().startswith('l'):
    print("You head down the beach, you see what appears to be a school of fish in the distance,"
          " do you Swim or Wait?")
    fishies = input(">")

    if fishies.lower().startswith('w'):
        print("Successfully dodging the school of fish, realizing they were in fact Piranha;"
              " you continue down the beach, winding down a path that leads you to three doors in a cliff face."
              "\n Do you take the Red door, Blue door or Yellow Door?")
        door = input(">")

        if door.lower().startswith('r'):
            print("You successfully chose the haste buff. Too bad it was to hasten your death."
                  "\n You are burned alive. GAME OVER ")
        elif door.lower().startswith('y'):
            print("You succeed in picking the ugliest door. As punishment several Chimera leap out and tackle you."
                  "\n The beasts maul you until there's nothing but a fine mist lingering in the air, thats you.\n"
                  "You're the mist. GAME OVER.")
        else:
            print("Against all odds, you've managed to make your way to the Treasure. Congratulations!"
                  "\n YOU WIN")
    else:
        print("We're here for treasure not fish. Probably shouldnt be wandering off the course should  we?\n"
              "You are dead. GAME OVER")
else:
    print("You encounter a biblically accurate angel, your mind is blown by the sheer awesomeness "
          "of their voice and the grotesqueness of their form.\n You are dead. GAME OVER.")
