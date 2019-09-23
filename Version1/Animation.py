
#Import the module
from Main import *

#Create an Aid object width width and height of 600
game = Aid(600, 600)

#Create a rectangle with a list of values
game.addRect("player", imgLoc=["res/AnimationExamples/img1.png", "res/AnimationExamples/img2.png", "res/AnimationExamples/img3.png", "res/AnimationExamples/img4.png", "res/AnimationExamples/img5.png"], layer=1)

#Create the variables for a repetitive change in images
testImageNum = 0
count = 10

#Create the game loop
while 1:

	#Get the keys
	keys = game.getKeys()

	#If the conter = 10
	if count == 10:

		#Set the player image to the second count
		game.player.setImage(testImageNum)
		#Add one to the counter for the image num
		testImageNum += 1

		#If the test num == 5, which is the number of images
		if testImageNum == 5:
			#Set the test num to 0
			testImageNum = 0
		#Set the count to 0
		count = 0

	#Add one to the count
	count += 1

	#If the up key is pressed, move the player up by 6 pixels
	if keys[K_UP]:
		game.player.y -= 6

	#If the down jets is pressed, move the player down by 6 pixels
	if keys[K_DOWN]:
		game.player.y += 6

	#If the player goes off the top of the screen, stop them
	if game.player.y <= 0:
		game.player.y = 0

	#IF the player goes off the bottom of the screen, stop them
	if game.player.y >= game.height - game.player.height:
		game.player.y = game.height - game.player.height

	#Update the game object
	game.update()