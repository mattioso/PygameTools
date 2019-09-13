
import pygame, sys
from pygame.locals import *

class Aid(object):

	#Constructor to pass the variables to create the screen
	def __init__(self, width, height, backcolour=(70, 70, 70)):

		self.size = self.width, self.height = width, height
		self.clock = pygame.time.Clock()

		pygame.init()
		self.screen = pygame.display.set_mode(self.size)

		self.rectangles = []
		self.colour = backcolour

	#Define a function to add new rects to the instance
	def addRect(self, name, imgLoc="", width="", height=""):

		#Check to make sure at least one set of parameters needed for the creation of the rectangle is provided
		if imgLoc == "" and width == "" and height == "":
			raise Exception("Either a location or dimensions should be specified")

		#If the width and the height have been given
		if not width == "" and not height == "":
			setattr(self, name, Rectangle(width, height))
		
		#If the image location has been given
		else:
			setattr(self, name, Rectangle(image=pygame.image.load(imgLoc)))

		self.rectangles.append(name)

	#Define a function to run the commands the need running last in a game loop
	def closingCommands(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		self.clock.tick(60)
		pygame.display.update()

	def draw(self):

		self.screen.fill(self.colour)

		for rects in self.rectangles:
			if eval("self.{}".format(rects)).type == 0:
				self.screen.blit(eval("self.{}".format(rects)).image, eval("self.{}".format(rects)).rect)

			else:
				pygame.draw.rect(self.screen, eval("self.{}".format(rects)).colour, eval("self.{}".format(rects)).rect)

	def update(self):

		for rects in self.rectangles:
			eval("self.{}".format(rects)).update()

#Define a class to handle rectangles
class Rectangle(object):

	#Define the constructor
	def __init__(self, width="", height="", image=None, colour=(255, 0, 0)):

		#if an image has been passed
		if width == "" and height == "":
			self.image = image
			self.rect = self.image.get_rect()
			self.width = self.rect.width
			self.height = self.rect.height
			self.x = 0
			self.y = 0
			self.drawing = True
			self.type = 0

		#If a set of value have been given
		else:
			self.rect = Rect(0, 0, width, height)
			self.width = width
			self.height = height
			self.x = 0
			self.y = 0
			self.type = 1
			self.colour = colour
			self.drawing = True

	#Update the rect position to the x position
	def update(self):

		self.rect.x = self.x
		self.rect.y = self.y