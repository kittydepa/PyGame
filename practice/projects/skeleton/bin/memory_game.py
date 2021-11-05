'''
Memory Puzzle
http://inventwithpython.com/pygame
Released under a "Simplified BSD" license
'''

import random, pygame, sys
from pygame.locals import *


# It's better to set up global variable because it makes set up and the code more readable
FPS = 30 # the general speed of the program
WINDOWWIDTH = 640 # size of the game window's width in pixels
WINDOWHEIGHT = 480
REVEALSPEED = 8 # speed boxes' sliging reveals and covers
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10 # the number of columns of icons
BOARDHEIGHT = 7

# A 'sanity' check using assert, to make sure the board has an even number of boxes 
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0,   0)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

# In this case, it is better to use constant variables than strings. E.g., it can help detect typos later on
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."


def main():
    global FPSCLOCK, DISPLAYSURF # Because those in caps are global variables, they will be the same value even outside of this function
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    mousex = 0 # this is used to store x coordinate of mouse event
    mousey = 0 # this is used to store y coordinate of mouse event
    pygame.display.set_caption("Kitty's Memory Game")
    
    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)