
#Import the module
from Main import *

#Create a new aid object with width and height of 600
a = Aid(600, 600)

#Add a button of name test on the 0'th layer with three images to the class
a.addButton(name="test", layer=0, imgLoc=["res/Button1.png", "res/Button2.png", "res/Button3.png"])
#Add a button of name test2 on the 0'th layer with width and height of 200, text of Test and black text with size 50
a.addButton(name="test2", layer=0, width=200, height=200, text="Test", size=50, txtColour=(0,0,0))
#Move the second button the the right hand side of the screen
a.test2.x = a.width - a.test2.width

#Add a text object to the aid
a.addText(name="pressed", layer=1, text="Button Pressed", size=50, colour=(0,0,0))
#Set the text object to the middle of the screen
a.pressed.x = a.width / 2 - a.pressed.width / 2
#And 4/6ths of the way down
a.pressed.y = 600 / 6 * 4
#Tell the class that the text is not being drawn
a.pressed.drawing = False

#Set a counting value to 0
counting = 0

#Start our game loop
while 1:

	#import the mosuse postion and the buttons pressed
	mouseButtons = a.getMouseButtons()
	mousePos = a.getMousePos()

	#If counting does not == 0
	if not counting == 0:
		#Minus one from counting
		counting -= 1

	#If either buttons are pressed and counting is 0
	if a.test.pressed(mousePos, mouseButtons) and counting == 0 or a.test2.pressed(mousePos, mouseButtons) and counting == 0:
		#Set the pressed drawing state to the opposite of what it was
		a.pressed.drawing = not a.pressed.drawing
		#Set counting to 0
		counting = 20

	#Set the first buttons image to 0
	a.test.setImage(0)

	#If the button is being hovered over
	if a.test.inBox(mousePos):
		#Set the image to the second one in the list
		a.test.setImage(1)

	#If the button is being pressed
	if a.test.pressed(mousePos, mouseButtons):
		#Set the image to the third image in the list
		a.test.setImage(2)

	#Update the class
	a.update()