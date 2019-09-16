
#This is a demonstration of how the module can be used

#Import the module
from Main import *
#Import random
import random

#Set up the aid class as a, with a width and height of 600 and a dark green background
a = Aid(600, 600, (0, 100, 0))
#Add the player as an image of a blue rectangle
a.addRect("player", imgLoc="res/Player.png")
#Add the enemy as a red box with 20x20 dimensions
a.addRect("enemy", width=20, height=20)

#Set the player x to 20 and on the ground
a.player.x = 20
a.player.y = a.height - a.player.height

#Set the enemy a random distance of between 200 and 0 pixels off screen
a.enemy.x = random.randint(a.width, a.width + 200)
#Set the enemy speed to a random int between -10 and -5
a.enemy.speed[0] = random.randint(-10, -5)
#Set the enemy height to on the floor
a.enemy.y = a.height - a.enemy.height

#Set a variable for whether the player is currently jumping
jumping = False

#Run the game loop
while 1:

	#Get the pressed keys
	keys = a.getKeys()

	#If space is pressed and the player is not currently jumping
	if keys[K_SPACE]:
		if not jumping:
			#Set the player to be moving at 15 pixels a tick upwards
			a.player.speed[1] -= 15
			#Set the jumping variable to true
			jumping = True

	#If the player is currently jumping
	if jumping:
		#Add one to the y speed, which will overcome the 15 taking the player up then bring him down at an increasing pace
		a.player.speed[1] += 1
		#If the player has gone bellow the ground
		if a.player.y > a.height - a.player.height:
			#Set the jumping variable to false
			jumping = False
			#Set the y speed to 0
			a.player.speed[1] = 0
			#Set the player on the ground
			a.player.y = a.height - a.player.height

	#If the enemy has gone off the screen
	if a.enemy.x <= -a.enemy.width:
		#Set the x speed to a random int between -5 and -3
		a.enemy.speed[0] = random.randint(-5, -3)
		#Set the x to a random int between 0 and 200 pixels off screen
		a.enemy.x = random.randint(a.width, a.width + 200)

	#If the player collides with the enemy
	if a.player.collide(a.enemy):
		#Set the x speed to a random int between -5 and -3
		a.enemy.speed[0] = random.randint(-5, -3)
		#Set the x to a random int between 0 and 200 pixels off screen
		a.enemy.x = random.randint(a.width, a.width + 200)
		#Set the player's x to 20
		a.player.x = 20
		#Set the player y to the have it on the ground
		a.player.y = a.height - a.player.height
		#Set both the player speed to 0
		a.player.speed = [0, 0]
		#Set that the player is no longer jumping
		jumping = False

	#Update the game
	a.update()
