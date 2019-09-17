
#This is a demonstration of how the module can be used

#Import the module
from Main import *
#Import the randint function from random
from random import randint

#Set up the aid class with width and height of 600 and the standard colour of 70, 70, 70
game = Aid(600, 600)

#Add the player rectangle
game.addRect("player", imgLoc="res/Player.png", layer=1)
#Set the players x to 20, and the y to the middle of the screen
game.player.x = 20
game.player.y = game.width / 2 - game.player.width / 2

#Add the five enemies
for x in range(5):
	game.addRect("enemy{}".format(x), imgLoc="res/Laser.png", layer=2)

game.addRect("backdrop", imgLoc="res/background.png", layer=0)

#Define a function to iterate through the enemies and reset them all
def resetEnemies():
	for x in range(5):
		#Set the y to a random integer between 0 and the height of the game minus the height of the enemy
		eval("game.enemy{}".format(x)).y = randint(0, game.height- eval("game.enemy{}".format(x)).height)
		#Set the x to a random integer between the width and 200 past the width of the game
		eval("game.enemy{}".format(x)).x = randint(game.width, game.width + 200)
		#Give the enemy a random speed between -15 and -4
		eval("game.enemy{}".format(x)).speed[0] = randint(-15, -4)

#Run the reset enemies function
resetEnemies()

#Create the game loop
while 1:

	#Get the keys
	keys = game.getKeys()

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

	#Iterate through the enemies
	for x in range(5):
		#Check if the enemy has gone off screen
		if eval("game.enemy{}".format(x)).x < 0 - eval("game.enemy{}".format(x)).width:
			#Set the enemy back to the same random values as before
			eval("game.enemy{}".format(x)).y = randint(0, game.height- eval("game.enemy{}".format(x)).height)
			eval("game.enemy{}".format(x)).x = randint(game.width, game.width + 200)
			eval("game.enemy{}".format(x)).speed[0] = randint(-15, -4)

		#If the player has collided with the enemy
		if game.player.collide(eval("game.enemy{}".format(x))):
			#Reset the enemies
			resetEnemies()
			#Set the player back to the start
			game.player.x = 20
			game.player.y = game.width / 2 - game.player.width / 2

	#Update the game
	game.update()