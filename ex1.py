from random import sample, choice, randrange

Sword = "By taking this sword, you have +10 damage now. Maybe it will be useful later on!!"
Shield = "By taking this shield, you now have +10 defense. Might be useful in the near future!!"
Potion = "This potion gives you +5 damage boost over your sword Damage if you have one!!"
Book = "Now that you have read this book, you know more about defending. +5 to defense points on top of your Sheild defense, if you have one of course!!!!"
Script = "Now you know how to script, so go ahead and make your own game if you don't like mine."

roomNum = [2, 3, 4, 5, 6, 7, 8, 9, 10]
roomObj = ["Sword", "Shield", "Potion", "Book", "Script"]
roomDoors = [2, 3]
playerChoice = []
playerSword = set ()
playerShield = set ()
playerDmg = []
playerBlock = []
swordDmg = len(playerSword)
shieldBlock = len(playerShield)
dmg = len(playerDmg)
block = len(playerBlock)
attack = int(randrange(0,101)) + int(swordDmg * 10) + int(dmg * 5)
defense = int(randrange(1,101)) - int(shieldBlock * 10 ) - int(block * 5)
bossHealth = 200
enemyHealth = randrange(50,151)
			
"""
Function to show the rules of the game.
What's the game about you might ask, none of your business is the answer!!!!!!
Now fuck off and play the damn game.
"""			
def rules():
	print ("These are the rules of the game, at any prompt, you can type \"rules\" to see them again.")
	print ("1. There are 10 rooms and you start in room number 1.")
	print ("2. Depending on the number of doors in the room, you can go \"Right\", \"Left\", or \"Up\".")
	print ("3. You can revisit the previous room you were in by choosing \"Down\". Note that you can only go back to the previous room you were just in.")
	print ("4. Some rooms have items in them, you can interact with them by typing the name of the item you want.")
	print ("5. By typing anything besides the the stuff mentioned above, you can quit the game.")
	print ("6. After reaching room number 10, the game is over and you will win if you manage to defeat the boss in that room\n\n")
	Checker().answerCheck()

#Room function to generate the rooms the player is going to be in.
def room():
	if choice(roomNum) == 10:
		print ("Congratulation, you have made it to room number 10.")
		print ("You have the chance to attack the Boss and win the game.")
		print ("The Boss has 300 health.")
		fight = input("Would you like to attack the monster? ")
		if fight.lower() == "yes":
			if attack >= bossHealth / 2:
				print ("Congratulations!!!! You did " + attack + "damage to the monster and killed it. You have finished the game like a badass you are!!!!")
			elif defense < bossHealth / 2 and defense >= int(bossHealth / 3):
				print ("The monster attacked you before you had a chance, but you surviced with " + defense + " health and managed to get out of the room.\nCongratulations on finishing the game.")
			else:
				print ("The monster attacked you before you had a chance and killed you.\nNot sure why I'm telling you this considering that you are dead!!")
		else:
			print ("I see you chose to be a chicken and not fight the monster.\nThe monster didn't care tho, so he attacked and killed you anyways!!!")
	else:	
		print ("You have entered room number: " + str(choice(roomNum)) + ", There are " + str(choice(roomDoors)) + " doors in this room.")
		print ("These are the items available in this room: " + str(sample(roomObj, 2)))
		obj = input("Which one of those items whould you like to interact with? ")
		Checker().itemChecker(obj)
		Checker().answerCheck()

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
		print ("I see you chose to be a chicken and not fight the monster.\nThe monster didn't care and attacked you anyways!!!\nYou got lucky tho and manged to get to the next room, you might not be this lucky next time.")
		room()

#Checker class to check the user's answer in order to make the next moves.
class Checker:
	def answerCheck(self):
		answer = input("Where do you wanna go? ")
		if answer.lower() == "rules":
			rules()
		elif answer.lower() == "left" or answer.lower() == "l":
			room()
			playerChoice.append(answer)
		elif answer.lower() == "right" or answer.lower() == "r":
			room()
			playerChoice.append(answer)
		elif answer.lower() == "up" or answer.lower() == "u":
			room()
			playerChoice.append(answer)
		else:
			print ("I guess you missed the instructions!!!!\nYou won't get a chance to fix this issue, so you can start from scratch if you want")
			
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
			playerDmg.append(obj.lower())
		elif obj.lower() == "book":
			print (Book +  "\n")
			playerBlock.append(obj.lower())
		elif obj.lower() == "script":
			print (Script + "\n")
		else:
			print ("Seems like you don't want to interact with any of the items. It's okay, that won't affect you at all in the future")

print ("Welcome to hell!!!!\nWe are gonna have so much FUN!!!\n")	
rules()