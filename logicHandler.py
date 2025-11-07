#Checker class to check the user's input.
class Checker:
	
	# Function to check and see what direction the user wants to go to. 
	def answerCheck(self, userAnswer):
		playerChoice.append(userAnswer)
		if userAnswer.lower() == "rules":
			rules()
		elif userAnswer.lower() == "up" or userAnswer.lower() == "u" \
			or userAnswer.lower() == "right" or userAnswer.lower() == "r":
			room()
		else:
			print ("I guess you missed the instructions!!!!\n \
				Why don't you try again and see what happens.")
