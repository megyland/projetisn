import pygame
from pygame.locals import *

# This class allows to enter text graphically in Pygame

class Textbox :

    def __init__(self, display, pos, wh, maxchars=-1, color=(255,255,255), bg=(0,0,0), font=pygame.font.get_default_font(), size=20) :

        """
        Init method of Textbox.
        display : Surface to put the textbox on
        pos : pos of the box, tuple (x,y)
        wh : width and height of the box in a tuple
        maxchars : maximum number of characters
        color : color of the text
        bg : background image
        font : font used to display text
        size : size of the font
        """

        self.disp     = display
        self.pos      = pos
        self.rect     = pygame.Rect(pos, wh)
        self.maxchars = maxchars
        self.font     = pygame.font.Font(font, size)
        self.bg       = bg
        self.color    = color

        self.text     = ""
        self.enter    = False

        pygame.draw.rect(self.disp, self.bg, self.rect)

    def processevents(self, evt) :
        """
        Browse through events and add text if a key was pressed
        """
        if evt.type == KEYDOWN :
            if evt.key == K_BACKSPACE :
                # Remove a char at the end
                self.text = self.text[:len(self.text)-1]
                self.update()
            elif evt.key == K_RETURN :
                self.enter = True
            elif len(self.text) < self.maxchars or self.maxchars == -1:
                # Check if the key is a letter/a number ([0-9a-zA-Z])
                # evt.key is the matching ASCII code
                isnumber    = evt.key >= 48 and evt.key <= 57
                isupperchar = evt.key >= 65 and evt.key <= 90
                islowerchar = evt.key >= 97 and evt.key <= 122

                if isnumber or isupperchar or islowerchar :
                # if evt.key < 127 :
                    self.text += evt.unicode
                    self.update()
                    
    def update(self) :
        label = self.font.render(self.text, True, self.color)

        pygame.draw.rect(self.disp, self.bg, self.rect)
        self.disp.blit(label, self.pos)

        pygame.display.update()

    def getenter(self) :
        return self.enter

    def gettext(self) :
        return self.text

    def reset(self) :
        self.text = ""
        self.enter = False
        self.update()
