from random import sample, choice, randrange

# Items to be randomly generated in Rooms.
Weapon = "By taking this weapon, you have +50 damage now. Maybe it will be useful later on!!"
Armor = "By taking this Armor, you now have +10 defense. Might be useful in the near future!!"
Potion = "This potion gives you +5 damage boost!!"
Book = "Now that you have read this book, you know more about defending. +5 to defense!!!!"
Script = "Now you know how to script, so go ahead and make your own game if you don't like mine."

# Variables to be used in Room generation.
roomNums = [1, 2]
roomnumber = 0
roomObj = ["Weapon", "Armor", "Potion", "Book", "Script"]

# Variables to keep track of player's choices, health, and damage output.
roomChoice = []
playerChoice = []
playerWeapon = []
playerArmor = []
playerPotion = []
playerBook = []
playerHealth = 450
playerDmg = 150 + randrange(0, 50)
weaponDmg = int(len(playerWeapon) * 15)
armorBlock = int(len(playerArmor) * 15)
block = int(playerHealth) + randrange(0, 50) + int(armorBlock) + int(len(playerBook) * 5)

# Variables to be used by the Final Boss and Random enemies in rooms.
bossDmg = randrange(300, 500)
bossHealth = 275
monsterDmg = 200
monsterHealth = randrange(100, 201)


# Room function to generate the rooms the player is going to be in.
def room():
    roomnumber = choice(roomNums)
    if roomnumber == 2:
        print("Congratulation, you have made it to room number 10.")
        print("You have the chance to attack the Boss and win the game.")
        print("The Boss has 300 health.")
        bossfight = input("Would you like to attack the boss? ")
        if bossfight.lower() == "yes" or bossfight.lower() == "y":
            dmg = int(playerDmg) + int(len(playerWeapon) * weaponDmg) + int(len(playerPotion) * 5)
            if dmg > bossHealth:
                print("Congratulations!!!! You did " + str(
                    dmg) + " damage to the final boss and killed it. You have finished the game like a badass you are")
            elif int(block / 2) > bossDmg:
                print("The final boos attacked you before you had a chance, but you surviced with " + str(
                    block - bossDmg) + " health got out of the room.\nCongratulations on finishing the game.")
            else:
                print(
                    "The final boss attacked you before you had a chance and killed you!!!")
        else:
            print("I see you chose to be a chicken and not fight the final boss.")
            print("The final boss didn't care, so he attacked and killed you anyways!!!")
        print("These are the choices you made while playing the game: " + str(playerChoice))
    elif roomnumber % 2 == 0:
        monster()
    else:
        print("You have entered room number: " + str(roomnumber))
        itemchecker()
        answercheck()


"""
Function to show the rules of the game.
What's the game about you might ask, none of your business is the answer!!!!!!
Now fuck off and play the damn game.
"""


def rules():
    print("These are the rules of the game, at any prompt, you can type \"rules\" to see them again.")
    print("1. There are 10 rooms and you could start in any room you happen to spawn in.")
    print("2. You have the choice of going to \"Right\" or \"Up\" in each room.")
    print("3. Some rooms have items in them, you can interact with them by typing the name of the item you want.")
    print("4. By typing anything besides the stuff mentioned above, you can quit the game.")
    print("5. After reaching room number 10, the game is over.")
    print("You will win if you manage to defeat the boss in that room\n\n")
    room()


# Function to generate a random monster to be used in a random room.
def monster():
    print("You have entered room number: " + str(roomnumber))
    print("There seems to be a monster in this room. You must fight it so you can intract with the items in the room!!")
    monsterfight = input("So, do you wanna attack it or just move on??? ")
    if monsterfight.lower() == "yes" or monsterfight.lower() == "y":
        dmg = int(playerDmg) + int(len(playerWeapon) * weaponDmg) + int(len(playerPotion) * 5)
        if dmg >= monsterHealth:
            print("Congratulations!!!! You did " + str(dmg) + " damage to the monster and killed it.")
            itemchecker()
            answercheck()
        elif int(block / 2) >= monsterDmg:
            print("The monster attacked you before you had a chance, but you surviced with " + str(
                block - monsterDmg) + " and managed to get away from it. Quickly, ")
            room()
        else:
            print("The monster attacked you before you had a chance and killed you.")
            print("Not sure why I'm telling you this considering that you are dead!!")
    else:
        print("I see you chose to be a chicken and not fight the monster.")
        print("The monster didn't care and attacked you anyways!!!")
        print("You got lucky tho and manged to get to the next room, you might not be this lucky next time.\n")
        room()


# Function to check and see what direction the user wants to go to.
def answercheck():
    answer = input("Where do you wanna go? ")
    playerChoice.append(answer)
    if answer.lower() == "rules":
        rules()
    elif answer.lower() == "up" or answer.lower() == "u" or answer.lower() == "right" or answer.lower() == "r":
        room()
    else:
        print("I guess you missed the instructions!!!!")
        print("You won't get a chance to fix this issue, so you can start from scratch.")


# Function to check what item the user wants to interact with.
def itemchecker():
    obj = input("Which one of these items " + str(sample(roomObj, 2)) + " whould you like to interact with? ")
    if obj.lower() == "weapon":
        print(Weapon + "\n")
    elif obj.lower() == "armor":
        print(Armor + "\n")
    elif obj.lower() == "potion":
        print(Potion + "\n")
        playerPotion.append(obj.lower())
    elif obj.lower() == "book":
        print(Book + "\n")
        playerBook.append(obj.lower())
    elif obj.lower() == "script":
        print(Script + "\n")
    else:
        print("Seems like you don't want to interact with any of the items.")
        print("It's okay, that won't affect you at all in the future!!!!")


print("Welcome to hell!!!!\nWe are gonna have so much FUN!!!\n")
rules()
