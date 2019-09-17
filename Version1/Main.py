
import pygame, sys
#Pyaame locals for the keyclicks
from pygame.locals import *

#The main class of the object
class Aid(object):

	#Constructor to pass the variables to create the screen
	def __init__(self, width, height, backcolour=(70, 70, 70)):

		#Set the size of the screen
		self.size = self.width, self.height = width, height
		#Set the pygame clock up to limit fps
		self.clock = pygame.time.Clock()

		#Initialize the pygame module
		pygame.init()
		#Set the screen to a pygame display with the size given
		self.screen = pygame.display.set_mode(self.size)

		#Create an array to hold the names of the rectangles added
		self.rectangles = []

		#Set the colour to the given colour
		self.colour = backcolour

	#Define a function to add new rects to the instance
	def addRect(self, name, imgLoc="", width="", height="", colour=(255, 0, 0), layer=0):

		#Check to make sure at least one set of parameters needed for the creation of the rectangle is provided
		if imgLoc == "" and width == "" and height == "":
			raise Exception("Either a location or dimensions should be specified")

		#If the width and the height have been given
		if not width == "" and not height == "":
			setattr(self, name, Rectangle(width=width, height=height, colour=colour))
		
		#If the image location has been given
		else:
			setattr(self, name, Rectangle(image=pygame.image.load(imgLoc)))

		#Try to add the rectangle to the correct layer list inside of the rectangles list
		try:
			self.rectangles[layer].append(name)
		#If that list doens't exist
		except:
			#Start a while loop
			while 1:
				#Try to add the layer in again
				try:
					self.rectangles[layer].append(name)
					#If the name is added, break out of the loop
					break
				except:
					#If the layer list is not pressent, add another list to rectangles
					self.rectangles.append([])

	#Define a function to run the commands the need running last in a game loop
	def closingCommands(self):

		#If the x is pressed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		#Use the pygame clock function to limit the to 60 fps
		self.clock.tick(60)
		#Update the display
		pygame.display.update()

	def draw(self):

		#Fill the screen with colour
		self.screen.fill(self.colour)

		#For every rectangle in rectangles array
		for rects in self.rectangles:
			#Iterate through the layers, so the game is drawn in the desired order
			for layers in rects:
				#Check if the rectangle wants to be drawn
				if eval("self.{}".format(layers)).drawing:
					#If the rectangle has an image to draw
					if eval("self.{}".format(layers)).type == 0:
						#Draw the image
						self.screen.blit(eval("self.{}".format(layers)).image, eval("self.{}".format(layers)).rect)
					#If the rectangle has no image
					else:
						#Draw a block coloured rectangle
						pygame.draw.rect(self.screen, eval("self.{}".format(layers)).colour, eval("self.{}".format(layers)).rect)

	#Define an update function
	def update(self):

		#Iterate through the rectangles in the rectangle array
		for rects in self.rectangles:
			#Go through the layers
			for layers in rects:
				#Update every rectangle given
				eval("self.{}".format(layers)).update()

		#Run the draw function
		self.draw()
		#Run the closing commands function
		self.closingCommands()

	#Return the pressed keys
	def getKeys(self):
		return pygame.key.get_pressed()

#Define a class to handle rectangles
class Rectangle(object):

	#Define the constructor
	def __init__(self, width="", height="", image=None, colour=(255, 0, 0)):

		#if an image has been passed
		if width == "" and height == "":
			#Set the image to the image given
			self.image = image
			#Get a rectangle of the image
			self.rect = self.image.get_rect()
			#Set the width and height variables to the width and height of the rectangle
			self.width = self.rect.width
			self.height = self.rect.height
			#Set the type to 0
			self.type = 0

		#If a set of value have been given
		else:
			#Set up the rectangle manually
			self.rect = Rect(0, 0, width, height)
			#Set the width and height variables to the values given
			self.width = width
			self.height = height
			#Set the type to 1
			self.type = 1
			#Set the colour to the given colour
			self.colour = colour

		#Set up speed variables
		self.speed = [0, 0]
		#Set x and y to 0
		self.x = 0
		self.y = 0
		#Set a variable that can be turned off to make the rectangle not draw
		self.drawing = True

	#Update the rect
	def update(self):

		#Add the speed variables to the x and y
		self.x += self.speed[0]
		self.y += self.speed[1]

		#Update the rect positions 
		self.rect.x = self.x
		self.rect.y = self.y

	#Create a collide function
	def collide(self, Rectangle):

		return self.rect.colliderect(Rectangle.rect)

