#Alarm Clock
#Created by: Abdulahi Osoble
#------------------------------------
 
import webbrowser
import time
import random
import os
#Finding out if the file exists
if os.path.isfile("input.txt"):
	print "FILE NOT FOUND!!"

print"what time should the alarm be set at? "
print"example format \t hh:mm"
#Entering the alarm time
Atime = raw_input("> ")
#To get current time and declaring it under a variable
t  = time.strftime("%H:%M")
#To open the file and read the links
with open("input.txt") as o:
	urls = o.readlines()

#Loop will run while the alarm time hasn't been reached
while t != Atime:
	print"Current time: " + t
	#Restate the time to refresh its value under the variable
	t  = time.strftime("%H:%M")
	#Make it sleep for 1 minute to stop it from flooding the command line with updates
	time.sleep(60)

if t == Atime:
	print"ALARM! WAKE UP!"
	#Choose a random link to open
	random_link = random.choice(urls)
	#Open that random link
	webbrowser.open(random_link)