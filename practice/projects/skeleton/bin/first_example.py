"""
First example in "Making Games"
CLI vs GUI in PyGame
"""

import pygame, sys
from pygame.locals import *

pygame.init() # Need to call this every time you use pygame, else you will get an error 
DISPLAYSURF = pygame.display.set_mode((480, 320)) # This returns as a pygame.surface object - will be explained later on in the book. Also, need to set these dimensions as a tuple, not just plain intergers. That's why there are two sets of ()
pygame.display.set_caption("Kitty's Super Cute Game")
while True: #main game loop
    for event in pygame.event.get(): # To iterate over the list of Event objects that was returned by pygame.event.get()
        if event.type == QUIT: # This checks to see if the event object is equal to QUIT
            pygame.quit()
            sys.exit()
    pygame.display.update()