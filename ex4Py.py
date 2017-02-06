"""

*Student Name: Noah Gorny

*Student ID: 209399757

*Course Exercise Group: 02 Math

*Exercise name: ex4Py

"""
# To use wordcap and such
import string

def ReadText():
	"""
	Read the text from "movies.txt"
	and returns it as lines of text

	Keyword argument:
	Return- The text from "movies.txt"
	"""
	with open("movies.txt") as text:
		linesOfText = text.readlines()
	return linesOfText;

def AddToDic(theLines, dic):
	"""
	Gets lines of text and sort them inside the dictionary dic
	The order is- movie: {Set of actors}
	
	Keyword argument:
	TheLines- Lines of text recieved from "movies.txt"
	Dic- The dictionary to place the text into using the correct order
	Return- Sorts dic as needed
	"""
	# For each line in the lines of the text:
	for line in theLines:
		# Lowercase the lines
		line=line.lower()
		# Remove the end of line char
		line=line.translate(None, "\n")
		# And split them using split
		lineList=line.split(',')
		# The actor name is the first name on each line
		actorName=lineList[0].lstrip()
		lineList.remove(lineList[0])
		# For each movie left in the line
		for movie in lineList:
			movie=movie.strip()
			if movie not in dic:
				# If the movie is not in the dict yet, add it	
				dic[movie]=set()
			pass
			# Add the actor to the set of the movie		
			dic[movie].add(actorName)
		pass
	pass
	return;

def MissionOne(dic):
	"""
	Does mission one of the Python program- Asks for two movies
	And an operator and then prints the actors as needed
	
	Keyword argument:
	Dic- The dictionary used as the database of the program
	Return- Prints the needed actors
	"""	
	oneInput=raw_input("Please enter two movies and an operator(&,|,^) separated with ',':\n")
	oneInput=oneInput.split(',')
	# Var used to determine if the input was ok
	inputOkay=True
	for i in range(0,len(oneInput)):
		oneInput[i]=oneInput[i].strip()
		oneInput[i]=oneInput[i].lower()
	# Checks if the two movies exist in the dict:
	if((oneInput[0] in dic) and (oneInput[1] in dic)):
		if(oneInput[2]=='|'):
			# Gets the union actors
			inputSet=dic[oneInput[0]].union(dic[oneInput[1]])
			if(bool(inputSet)):
				print "The union actors are:"
		elif(oneInput[2]=='&'):	
			# Gets the intersection actors
			inputSet=dic[oneInput[0]].intersection(dic[oneInput[1]])
			if(bool(inputSet)):
				print "The intersection actors are:"
		elif(oneInput[2]=='^'):
			# Gets the symmetric difference actors
			inputSet=dic[oneInput[0]].symmetric_difference(dic[oneInput[1]])
			if(bool(inputSet)):
				print "The symmetric difference actors are:"
		else:
			# The code should not get into here- bad operator
			print "Error- BAD operator"
			inputOkay=False
		if(inputOkay):
			if(bool(inputSet)):
				# If there are actors, print them
				PrintSet(inputSet)
			else:
				# If there is none, print this
				print "There are no actors in this group."
	else:
		# One of the movies is not in the database- print "Error"
		print "Error"
	return;

def MissionTwo(dic):
	"""
	Does mission two of the Python program- Asks for an actor
	and prints all the actors that played with this actor
	
	Keyword argument:
	Dic- The dictionary used as the database of the program
	Return- Prints the needed actors
	"""
	actorInput=raw_input("Please enter an actor:\n")
	actorInput=actorInput.lower()
	actorInput=actorInput.strip()
	# Var used to determine whether the actors exists in the dict or not
	actorExist=False

	# The Co-Actors set used to contain all the actors that played
	# with the chosen actor.
	coActors=set()
	# For each movie in the dict
	for movie in dic:
		if actorInput in dic[movie]:
			# The actor does exists (in this movie)
			actorExist=True
			for actor in dic[movie]:
				if(actor != actorInput):
					# Add all the other actors that played in the same movie
					coActors.add(actor)
				pass
			pass
		pass
	pass
	if(actorExist):
		if(bool(coActors)):
			# There is co-stars, print them
			print "The actor's co-stars are:"
			PrintSet(coActors)
		else:
			# There is no co-stars, print this instead
			print "There are no actors in this group."
	else:
		# The actor does not exist in the database, print "Error"
		print "Error"
	return;

def PrintSet(theSet):
	"""
	Sorts the set by names, capwords it and then prints
	the whole set as one line, each element seperated with ','
	
	Keyword argument:
	TheSet- The set that we need to print
	Return- Prints the set as the format requires
	"""
	# Sort the set by names and make it into a list
	newList=sorted(theSet)
	for i in range(0, len(newList)):
		# Capwords each name in the list
		newList[i]=string.capwords(newList[i])
	# Prints the whole list with the elements seperated with ','
	print  ', '.join(newList)
	return;

def main():
	# Creating the database
	print "Processing..."
	# Creating dic as a new dictionary
	dic={}
	# Var used to know when to stop the main loop
	run=True
	# Read the text from "movies.txt"
	theLines=ReadText()
	# Process it into dic
	AddToDic(theLines, dic)
	# While the main loop in running:
	while run:
		print "Please select an option:"
		print "1) Query by movies"
		print "2) Query by actor"
		print "3) Quit"
		choice= input("")
		if(choice==1):
			# Do mission number one
			MissionOne(dic)
		elif(choice==2):
			# Do mission number two
			MissionTwo(dic)
		elif(choice==3):
			# End the program
			run=False
		else:
			# Bad key pressed
			print("BUG!!\n Not supposed to get in here")
	# End of the program
	return 1;

if __name__ == "__main__":
	# To start the program properly
    main()