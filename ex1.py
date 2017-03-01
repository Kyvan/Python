from random import sample, choice, randrange

# Items to be randomly generated in Rooms.
Sword = "By taking this sword, you have +50 damage now. Maybe it will be useful later on!!"
Shield = "By taking this shield, you now have +10 defense. Might be useful in the near future!!"
Potion = "This potion gives you +5 damage boost!!"
Book = "Now that you have read this book, you know more about defending. +5 to defense!!!!"
Script = "Now you know how to script, so go ahead and make your own game if you don't like mine."

# Variables to be used in Room generation.
roomNum = [2, 3, 4, 5, 6, 7, 8, 9, 10]
roomObj = ["Sword", "Shield", "Potion", "Book", "Script"]
roomDoors = [2, 3]

# Variables to keep track of player's choices, health, and damage output.
playerChoice = []
playerSword = set ()
playerShield = set ()
playerPotion = []
playerBook = []
playerHealth = 300
playerDmg = 150
swordDmg = int(len(playerSword) * 50)
shieldBlock = int(len(playerShield) * 50)
dmg = int(playerDmg) + randrange(0,51) + int(swordDmg) + int(len(playerPotion) * 5)
block = int(playerHealth) + randrange(0,51) + int(shieldBlock) + int(len(playerBook) * 5)

# Variables to be used by the Final Boss and Random enemies in rooms.
bossDmg = randrange(700,801)
bossHealth = 450
enemyDmg = 400
enemyHealth = randrange(100,201)

"""
Function to show the rules of the game.
What's the game about you might ask, none of your business is the answer!!!!!!
Now fuck off and play the damn game.
"""			
def rules():
	print ("These are the rules of the game, at any prompt, you can type \"rules\" to see them again.")
	print ("1. There are 10 rooms and you could start in room any room you happen to spawn in.")
	print ("2. Depending on the number of doors in the room, you can go \"Right\", \"Left\", or \"Up\".")
	print ("3. You can revisit the previous room you were in by choosing \"Down\". Note that you can only go back to the previous room you were just in.")
	print ("4. Some rooms have items in them, you can interact with them by typing the name of the item you want.")
	print ("5. By typing anything besides the the stuff mentioned above, you can quit the game.")
	print ("6. After reaching room number 10, the game is over and you will win if you manage to defeat the boss in that room\n\n")
	room()

#Room function to generate the rooms the player is going to be in.
def room():
	if choice(roomNum) == 10:
		print ("Congratulation, you have made it to room number 10.")
		print ("You have the chance to attack the Boss and win the game.")
		print ("The Boss has 300 health.")
		fight = input("Would you like to attack the monster? ")
		if fight.lower() == "yes":
			if dmg >= bossHealth / 2:
				print ("Congratulations!!!! You did " + str(dmg) + "damage to the monster and killed it. You have finished the game like a badass you are!!!!")
			elif block < bossDmg / 2 and block >= int(bossDmg / 3):
				print ("The monster attacked you before you had a chance, but you surviced with " + str(block) + " health and managed to get out of the room.\nCongratulations on finishing the game.")
			else:
				print ("The monster attacked you before you had a chance and killed you.\nNot sure why I'm telling you this considering that you are dead!!")
		else:
			print ("I see you chose to be a chicken and not fight the monster.\nThe monster didn't care tho, so he attacked and killed you anyways!!!")
		print ("These are the choices you made while playing the game: " + str(playerChoice))
	else:	
		print ("You have entered room number: " + str(choice(roomNum)) + ", There are " + str(choice(roomDoors)) + " doors in this room.")
		print ("These are the items available in this room: " + str(sample(roomObj, 2)))
		obj = input("Which one of those items whould you like to interact with? ")
		Checker().itemChecker(obj)
		Checker().answerCheck()

# Function to generate a random enemy to be used in a random room.
def enemy():
	print ("There seems to be an enemy in the room!!!!!\nWould you like to attack it?")
	enemyFight = input("Would you like to attack the monster? ")
	if enemyFight.lower() == "yes":
		if attack >= int(enemyHealth / 2):
			print ("Congratulations!!!! You did " + attack + "damage to the monster and killed it.\nNow you are free to go to the next room.")
			room()
		else:
			print ("The monster attacked you before you had a chance and killed you.\nNot sure why I'm telling you this considering that you are dead!!")
	else:
		print ("I see you chose to be a chicken and not fight the monster.\nThe monster didn't care and attacked you anyways!!!")
		print ("You got lucky tho and manged to get to the next room, you might not be this lucky next time.")
		room()

#Checker class to check the user's answer.
class Checker:
	
	# Function to check and see what direction the user wants to go to. 
	def answerCheck(self):
		answer = input("Where do you wanna go? ")
		playerChoice.append(answer)
		if answer.lower() == "rules":
			rules()
		elif answer.lower() == "left" or answer.lower() == "l":
			room()
		elif answer.lower() == "right" or answer.lower() == "r":
			room()
		elif answer.lower() == "up" or answer.lower() == "u":
			room()
		else:
			print ("I guess you missed the instructions!!!!\nYou won't get a chance to fix this issue, so you can start from scratch if you want")
	
	# Function to check what item the user wants to interact with.
	def itemChecker(self, obj):
		if obj.lower() == "sword":
			print (Sword + "\n")
			if obj.lower() not in playerSword:
				playerSword.add(obj.lower())
			else:
				print ("You already have a Sword, so you can't keep this one.\n")
		elif obj.lower() == "shield":
			print (Shield + "\n")
			if obj.lower() not in playerShield:
				playerShield.add(obj.lower())
			else:
				print ("You already have a Shield, so you can't keep this one.\n")
		elif obj.lower() == "potion":
			print (Potion + "\n")
			playerPotion.append(obj.lower())
		elif obj.lower() == "book":
			print (Book +  "\n")
			playerBook.append(obj.lower())
		elif obj.lower() == "script":
			print (Script + "\n")
		else:
			print ("Seems like you don't want to interact with any of the items. It's okay, that won't affect you at all in the future!!!!\n")

print ("Welcome to hell!!!!\nWe are gonna have so much FUN!!!\n")	
rules()