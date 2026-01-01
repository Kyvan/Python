#Checker class to check the user's input.
from game.game import player_choice, rules, room


def answer_check(user_answer):
	player_choice.append(user_answer)
	if user_answer.lower() == "rules":
		rules()
	elif user_answer.lower() == "up" or user_answer.lower() == "u" \
		or user_answer.lower() == "right" or user_answer.lower() == "r":
		room()
	else:
		print ("I guess you missed the instructions!!!!\n \
			Why don't you try again and see what happens.")