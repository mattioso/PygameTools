
from Main import *

a = Aid(600, 600)
a.addRect("imageTest", imgLoc="res/Player.png")
a.addRect("drawTest", width=200, height=200)

while 1:
	a.draw()

	a.drawTest.x +=1
	a.drawTest.y += 1

	a.update()
	a.closingCommands()
