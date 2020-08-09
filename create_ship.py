import facebook, random, time, datetime

#Insert paintmin tool access token here:
access_token = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
graph = facebook.GraphAPI(access_token) 


#Count wow reacts
def wow_counter(post_id, access_token, graph):
	wow_total = graph.get_object(id = post_id, fields = 'reactions.type(WOW).limit(0).summary(total_count)')
	wowint = int(wow_total['reactions']['summary']['total_count'])
	wowstr = str(wow_total['reactions']['summary']['total_count'])
	print("WOW react count: " + wowstr)
	return wowint

#Count haha reacts
def haha_counter(post_id, access_token, graph):
	haha_total = graph.get_object(id = post_id, fields = 'reactions.type(HAHA).limit(0).summary(total_count)')
	hahaint = int(haha_total['reactions']['summary']['total_count'])
	hahastr = str(haha_total['reactions']['summary']['total_count'])
	print("HAHA react count: " + hahastr)
	return hahaint

#Count sad reacts
def sad_counter(post_id, access_token, graph):
	sad_total = graph.get_object(id = post_id, fields = 'reactions.type(SAD).limit(0).summary(total_count)')
	sadint = int(sad_total['reactions']['summary']['total_count'])
	sadstr = str(sad_total['reactions']['summary']['total_count'])
	print("SAD react count: " + sadstr)
	return sadint

#Count love reacts
def love_counter(post_id, access_token, graph):
	love_total = graph.get_object(id = post_id, fields = 'reactions.type(LOVE).limit(0).summary(total_count)')
	loveint = int(love_total['reactions']['summary']['total_count'])
	lovestr = str(love_total['reactions']['summary']['total_count'])
	print("LOVE react count: " + lovestr)
	return loveint

#Count angry reacts
def angry_react(post_id, access_token, graph):
	angry_total = graph.get_object(id = post_id, fields = 'reactions.type(ANGRY).limit(0).summary(total_count)')
	angryint = int(angry_total['reactions']['summary']['total_count'])
	angrystr = str(angry_total['reactions']['summary']['total_count'])
	print("ANGRY react count: " + angrystr)
	return angryint


#Define a winner
def vote_results(candidate1, candidate2, candidate3, candidate4):
	print("\nvoting results: \n")
	vote1 = wow_counter(post_id, access_token, graph)
	vote2 = haha_counter(post_id, access_token, graph)
	vote3 = sad_counter(post_id, access_token, graph)
	vote4 = love_counter(post_id, access_token, graph)

	if (vote1 > vote2) and (vote1 > vote3) and (vote1 > vote4):
		winner = candidate1

	elif (vote2 > vote1) and (vote2 > vote3) and (vote2 > vote4):
		winner = candidate2

	elif (vote3 > vote1) and (vote3 > vote2) and (vote3 > vote4):
		winner = candidate3

	elif (vote4 > vote1) and (vote4 > vote3) and (vote4 > vote2):
		winner = candidate4

	else: 
		#tie, pick randomly 
		winner = "tie"
	return winner


#IMPORTANT!!!
#Item 1 = wow
#Item 2 = haha
#Item 3 = sad
#Item 4 = love
#Keep consistency!!!


#Start off by selecting mission.
#Count the lines in the mission_list file and saves it as int.
#Then creates a list var with the chosen mission.

mission_count = len(open("mission_list").readlines()) - 1
chosen_mission = random.sample(range(1, mission_count), 1)


f= open("mission_list", "r")
f1 = f.readlines()
mission = str(f1[chosen_mission[0]])


#Time to select hull.
#Counts the lines in the booster_list file and saves it as int.
#Then creates a list var with the chosen 4.
hull_count = len(open("hull_list").readlines()) - 1
chosen_hulls = random.sample(range(1, hull_count), 4)


#opens the file per lines, picking the line based on ints chosen. saves as str. Remember to close the file.
f= open("hull_list", "r")
f1 = f.readlines()
hull1 = str(f1[chosen_hulls[0]])

hull2 = str(f1[chosen_hulls[1]])

hull3 = str(f1[chosen_hulls[2]])

hull4 = str(f1[chosen_hulls[3]])

f.close()
	

#IMPORTANT!!!
#Item 1 = wow
#Item 2 = haha
#Item 3 = sad
#Item 4 = love
#Keep consistency!!!



#do the image part.
#will skip now for more core functions

content = "You have been tasked to create a spaceship to complete a mission. \nYour mission is the following: " + mission + "\nTo start, please select the hull of your new ship below by reacting with your favorite:\n\nWow - " + hull1 + "\nHaha - " + hull2 + "\nSad - " + hull3 + "\nLove - " + hull4

print(content)
post_id = graph.put_photo(image = open('WhitelineofZucc.jpg', 'rb'), message = content)['post_id'] 
print("Post on FB is made. This is the post ID: " + post_id)

#wait X amount of time
print("Code has been paused to allow voting.")
time.sleep(600)

#retrieve reacts, select winner
#Picks the booster with most votes. If tie, select at random and mark tie = true

tie = bool(False)
hull_final = vote_results(hull1,hull2,hull3,hull4)
if hull_final == "tie":
	print("There was a tie! Selecting one at random")
	tie = bool(True)
	hull_final = random.choice([hull1,hull2,hull3,hull4])

print("The winner was: " + hull_final)

#######################################################################################transition to next post


#Time to select hull.
#Counts the lines in the booster_list file and saves it as int. -1 because of last line in file
#Then creates a list var with the chosen 4.
engine_count = len(open("engine_list").readlines()) - 1
eligible_engines = random.sample(range(1, engine_count), 4)


#opens the file per lines, picking the line based on ints chosen. saves as str. Remember to close the file.
f= open("engine_list", "r")
f1 = f.readlines()
engine1 = str(f1[eligible_engines[0]])

engine2 = str(f1[eligible_engines[1]])

engine3 = str(f1[eligible_engines[2]])

engine4 = str(f1[eligible_engines[3]])

f.close()




#Define the content of the FB post. Change if it was a tie on previous post
if tie == True:
	content ="You have been tasked to create a spaceship to complete a mission. \nYour mission is the following: " + mission +" \nThe previous vote was a tie. It has been selected randomly.\nYour current parts: \nHull: " + hull_final + "\n\nNow, please select an engine from the options below: \n\nWow - " + engine1 + "\nHaha - " + engine2 + "\nSad - " + engine2 + "\nLove - " + engine4
else:
	content ="You have been tasked to create a spaceship to complete a mission. \nYour mission is the following: " + mission +" \nYour current parts: \nHull: " + hull_final + "\nNow, please select an engine from the options below: \n\nWow - " + engine1 + "\nHaha - " + engine2 + "\nSad - " + engine3 + "\nLove - " + engine4

print(content)

#Make the FB post with the content info.
post_id = graph.put_photo(image = open('WhitelineofZucc.jpg', 'rb'), message = content)['post_id'] 
print("Post on FB is made. This is the post ID: " + post_id)

#wait X amount of time
print("Code has been paused to allow voting.")
time.sleep(600)

#retrieve reacts, select winner
#Picks the booster with most votes. If tie, select at random and mark tie = true

tie = bool(False)
engine_final = vote_results(engine1,engine2,engine3,engine4)
if engine_final == "tie":
	print("There was a tie! Selecting one at random")
	tie = bool(True)
	engine_final = random.choice([engine1,engine2,engine3,engine4])

print("The winner was: " + engine_final)

#######################################################################################transition to next post


#Time to select cockpit.
#Counts the lines in the booster_list file and saves it as int. -1 because of last line in file
#Then creates a list var with the chosen 4.
cockpit_count = len(open("cockpit_list").readlines()) - 1
eligible_cockpits = random.sample(range(1, cockpit_count), 4)


#opens the file per lines, picking the line based on ints chosen. saves as str. Remember to close the file.
f= open("cockpit_list", "r")
f1 = f.readlines()
cockpit1 = str(f1[eligible_cockpits[0]])

cockpit2 = str(f1[eligible_cockpits[1]])

cockpit3 = str(f1[eligible_cockpits[2]])

cockpit4 = str(f1[eligible_cockpits[3]])

f.close()




#Define the content of the FB post. Change if it was a tie on previous post
if tie == True:
	content ="You have been tasked to create a spaceship to complete a mission. \nYour mission is the following: " + mission +" \nThe previous vote was a tie. It has been selected randomly.\nYour current parts: \nHull: " + hull_final + "Engine: " + engine_final + "\n\nNow, please select a cockpit from the options below: \nWow - " + cockpit1 + "\nHaha - " + cockpit2 + "\nSad - " + cockpit3 + "\nLove - " + cockpit4
else:
	content ="You have been tasked to create a spaceship to complete a mission. \nYour mission is the following: " + mission +" \nYour current parts: \nHull: " + hull_final + "Engine: " + engine_final + "\n\nNow, please select a cockpit from the options below: \n\nWow - " + cockpit1 + "\nHaha - " + cockpit2 + "\nSad - " + cockpit3 + "\nLove - " + cockpit4

print(content)

#Make the FB post with the content info.
post_id = graph.put_photo(image = open('WhitelineofZucc.jpg', 'rb'), message = content)['post_id'] 
print("Post on FB is made. This is the post ID: " + post_id)

#wait X amount of time
print("Code has been paused to allow voting.")
time.sleep(600)

#retrieve reacts, select winner
#Picks the booster with most votes. If tie, select at random and mark tie = true

tie = bool(False)
cockpit_final = vote_results(cockpit1,cockpit2,cockpit3,cockpit4)
if cockpit_final == "tie":
	print("There was a tie! Selecting one at random")
	tie = bool(True)
	cockpit_final = random.choice([cockpit1,cockpit2,cockpit3,cockpit4])

print("The winner was: " + cockpit_final)

#######################################################################################transition to next post


#Time to select boosters. 

#Counts the lines in the booster_list file and saves it as int.
#Then creates a list var with the chosen 4.
booster_count = len(open("booster_list").readlines()) - 1
chosen_boosters = random.sample(range(1, booster_count), 4)


#opens the file per lines, picking the line based on ints chosen. saves as str. Remember to close the file.
f= open("booster_list", "r")
f1 = f.readlines()
booster1 = str(f1[chosen_boosters[0]])

booster2 = str(f1[chosen_boosters[1]])

booster3 = str(f1[chosen_boosters[2]])

booster4 = str(f1[chosen_boosters[3]])

f.close()


#do the image part.
#will skip now for more core functions

#Define the content of the FB post. Change if it was a tie on previous post
if tie == True:
	content ="You have been tasked to create a spaceship to complete a mission. \nYour mission is the following: " + mission +" \nThe previous vote was a tie. It has been selected randomly.\nYour current parts: \nHull: " + hull_final + "Engine: " + engine_final + "Cockpit: " +cockpit_final + "\n\nNow, please select the boosters from the options below: \nWow - " + booster1 + "\nHaha - " + booster2 + "\nSad - " + booster3 + "\nLove - " + booster4
else:
	content ="You have been tasked to create a spaceship to complete a mission. \nYour mission is the following: " + mission +" \nYour current parts: \nHull: " + hull_final + "Engine: " + engine_final + "Cockpit: " +cockpit_final + "\n\nNow, please select the boosters from the options below: \n\nWow - " + booster1 + "\nHaha - " + booster2 + "\nSad - " + booster3 + "\nLove - " + booster4

print(content)

#Make the FB post with the content info.
post_id = graph.put_photo(image = open('WhitelineofZucc.jpg', 'rb'), message = content)['post_id'] 
print("Post on FB is made. This is the post ID: " + post_id)

#wait X amount of time
print("Code has been paused to allow voting.")
time.sleep(600)

#retrieve reacts, select winner
#Picks the booster with most votes. If tie, select at random and mark tie = true

tie = bool(False)
booster_final = vote_results(booster1,booster2,booster3,booster4)
if booster_final == "tie":
	print("There was a tie! Selecting one at random")
	tie = bool(True)
	booster_final = random.choice([booster1, booster2, booster3, booster4])

print("The winner was: " + booster_final)

#######################################################################################transition to next post



#Time to select ending. 

#Counts the lines in the ending_list file and saves it as int. -1 cuz of last line
#Then creates a list var with the chosen 4.
ending_count = len(open("ending_list").readlines()) - 1
chosen_ending = random.sample(range(1, ending_count), 4)

#pick one
f= open("ending_list", "r")
f1 = f.readlines()
ending = str(f1[chosen_ending[0]])

#define travel distance
altitudeINT = random.randrange(2147483600)
altitude = str(altitudeINT)
print("Chosen altitude is: " + altitude)

#do the image part.
#will skip now for more core functions

#Define the content of the FB post. Change if it was a tie on previous post
if tie == True:
	content ="You have been tasked to create a spaceship to complete a mission. \nYour mission is the following: " + mission +" \nThe previous vote was a tie. It has been selected randomly.\n\nYour spaceship is now complete. Here are the details: \nHull: " + hull_final + "Engine: " + engine_final + "Cockpit: " +cockpit_final + "Boosters: " +booster_final + "\nPrepare for launch and start the countdown:\n10, 9, 8, 7, 6, 5, 4, 3, 2, 1!\nAnd we have takeoff!\n\nAfter travelling for "+altitude + " meters, your ship"+ending + "\n\nWe shall receive a new mission tomorrow."
else:
	content ="You have been tasked to create a spaceship to complete a mission. \nYour mission is the following: " + mission +" \n\nYour spaceship is now complete. Here are the details: \nHull: " + hull_final + "Engine: " + engine_final + "Cockpit: " +cockpit_final + "Boosters: " +booster_final+ "\nPrepare for launch and start the countdown:\n10, 9, 8, 7, 6, 5, 4, 3, 2, 1!\nAnd we have takeoff!\n\nAfter travelling for "+altitude + " meters, your ship"+ending + "\n\nWe shall receive a new mission tomorrow."

print(content)

#Make the FB post with the content info.
post_id = graph.put_photo(image = open('dorime.png', 'rb'), message = content)['post_id'] 
print("Post on FB is made. This is the post ID: " + post_id)
