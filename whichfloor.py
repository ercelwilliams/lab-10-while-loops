maximum_stories = int(10)
userstring = input("On what floor of the building is your office? ")
usernum = int(userstring)

while usernum > maximum_stories:
	print("You entered: " + str(usernum) + "  but there are only " + str(maximum_stories) + " floors in this building. Try again...")
	userstring = input("You entered: " + str(usernum) + "  but there are only " + str(maximum_stories) + " floors in this building. Try again...")
	usernum = int(userstring, 10)

print("Congrats! You work on floor: " + usernum)
