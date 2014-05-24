# -*-coding:utf-8-*-

import os, pygame

# Config directory
CONFIG = os.path.join( os.path.expanduser("~"), ".config", "schrodinger" )

# Dimensions

SQUARE = 32
PANEL  = 450 # width of the panel

# Colours

BLUE      = (7, 0, 20)
LIGHTBLUE = (0, 0, 118)
RED       = (200, 0, 0)
GREEN     = (0, 255, 0)
GRAY      = (150, 150, 150)
LIGHTGRAY = (230, 230, 230)
WHITE     = (255, 255, 255)
BLACK     = (0,0,0)

# Images

## Main menu
IMG_BACKGROUND      = pygame.image.load( os.path.join("img", "homescreen.png") )

IMG_NEWGAME         = pygame.image.load( os.path.join("img", "buttonNewGame.png") )
IMG_NEWGAME_HOVER   = pygame.image.load( os.path.join("img", "buttonNewGameHover.png") )
IMG_LOADGAME        = pygame.image.load( os.path.join("img", "buttonLoadGame.png") )
IMG_LOADGAME_HOVER  = pygame.image.load( os.path.join("img", "buttonLoadGameHover.png") )
IMG_QUIT            = pygame.image.load( os.path.join("img", "buttonQuit.png") )
IMG_QUIT_HOVER      = pygame.image.load( os.path.join("img", "buttonQuitHover.png") )
IMG_BACK            = pygame.image.load( os.path.join("img", "buttonBack.png") )
IMG_BACK_HOVER      = pygame.image.load( os.path.join("img", "buttonBackHover.png") )

## Lab
IMG_TABLE_L         = pygame.image.load( os.path.join("img", "tableL.png") )
IMG_TABLE_M         = pygame.image.load( os.path.join("img", "tableM.png") )
IMG_TABLE_R         = pygame.image.load( os.path.join("img", "tableR.png") )

IMG_BOX             = pygame.image.load( os.path.join("img", "box.png") )
IMG_SCHRODINGER     = pygame.image.load( os.path.join("img", "Schrodinger.png") )
IMG_SCHRODINGER_L   = pygame.image.load( os.path.join("img", "Schrodinger_Left.png") )
IMG_SCHRODINGER_R   = pygame.image.load( os.path.join("img", "Schrodinger_Right.png") )

IMG_LAB_QUIT        = pygame.image.load( os.path.join("img", "labquit.png") )
IMG_LAB_QUIT_HOVER  = pygame.image.load( os.path.join("img", "labquit_hover.png") )
IMG_LAB_START       = pygame.image.load( os.path.join("img", "buttonStart.png") )
IMG_LAB_START_HOVER = pygame.image.load( os.path.join("img", "buttonStartHover.png") )

IMG_WIN             = pygame.image.load( os.path.join("img", "win.png") )
IMG_LOOSE_ALIVE     = pygame.image.load( os.path.join("img", "loose_alive.png") )
IMG_LOOSE_DEAD      = pygame.image.load( os.path.join("img", "loose_dead.png") )

## Side panel

IMG_ERROR           = pygame.image.load( os.path.join("img", "error.png") )
IMG_INTERESTING     = pygame.image.load( os.path.join("img", "experiment.png") )
IMG_FAILED          = pygame.image.load( os.path.join("img", "failed.png") )
IMG_SPEEDOMETER     = pygame.image.load( os.path.join("img", "speedometer.png") )
IMG_STARTFIRE       = pygame.image.load( os.path.join("img", "startfire.png") )
IMG_FIRE            = pygame.image.load( os.path.join("img", "fire.png") )

# Traps
## Image, name, description, price
## u"string" allows pygame to use unicode
TRAPS = [ (IMG_INTERESTING, u"Interesting experiment", u"Schrödinger can't help but stop to watch it", 1000, '?'),
          (IMG_ERROR, u"Error", u"Schrödinger made a mistake, he must stop and correct it", 2000, ';'),
          (IMG_FAILED, u"Failed experiment", u"An experiment went wrong, Schrödinger stops to clean it up", 5000, '!'),
          (IMG_SPEEDOMETER, u"Speedometer", u"Tells Schrödinger his exact speed so that he no longer knows where he is", 20000, '.'),
          (IMG_STARTFIRE, u"Starting fire", u"An experiment went awfuly wrong and sets fire to the lab. Schrödinger must extinguish every flame, but you have to make sure the fire doesn't reach the kitten", 50000, '*') ]

# Button places

## Main menu
BTN_NEWGAME  = (219, 430, 402, 82)
BTN_LOADGAME = (219, 510, 402, 82)
BTN_QUIT     = (219, 590, 402, 82)
BTN_BACK     = (219, 676, 402, 82)

## Lab
BTN_LAB_QUIT  = (16*SQUARE+PANEL-16, 0, 16, 16)
BTN_LAB_START = (16*SQUARE+25, 16*SQUARE-85, 300, 64)
