#!/usr/bin/python2
#-*- coding:utf-8 -*-

import os, sys, pygame
from pygame.locals import *

import Textbox, Lab, utils
from constants import *

pygame.init()

# Create the config directory if it doesn't exist
if not os.path.exists(CONFIG) :
    os.makedirs(CONFIG)

# Dimensions
W, H         = 512, 512

# Play music
pygame.mixer.music.load( os.path.join("sound", "music.ogg") )
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1) # play forever

class App :

    def __init__(self) :

        # Create a new window
        self.disp = pygame.display.set_mode( (512, 512) )
        pygame.display.set_caption("Schrödinger's cat")

        # Clock
        self.clock = pygame.time.Clock()

        # Running
        self.running = True

        # Add elements and events
        self.main()

        # Start the main loop
        self.loop()

    def loop(self) :

        while self.running :
            # Check events
            for evt in pygame.event.get() :
                if evt.type == QUIT : # If the window is closed
                    pygame.quit()
                    sys.exit()
                elif evt.type == MOUSEMOTION :
                    self.onmousemove(evt.pos)
                elif evt.type == MOUSEBUTTONUP :
                    self.onmouseclick(evt.pos)

                # Update checkboxes
                for i in self.textboxes :
                    i.processevents(evt)
                    if i.getenter() :
                        self.onentered(i)

            self.clock.tick(40) # limit framerate to 40fps

    def main(self) :
        """
        Set up elements and events for the main screen
        """

        # Add background
        self.disp.blit(IMG_BACKGROUND, (0,0)) # (last parameter isn't an owl)

        # Add buttons
        self.disp.blit(IMG_NEWGAME, BTN_NEWGAME)
        self.disp.blit(IMG_LOADGAME, BTN_LOADGAME)
        self.disp.blit(IMG_QUIT, BTN_QUIT)

        # No textbox here
        self.textboxes = []

        # Events
        def onmousemove(pos) :
            """
            Checks if the mouse is over a button, and changes its appearance
            accordingly.
            """

            if utils.isinrect(pos, BTN_NEWGAME) :
                self.disp.blit(IMG_NEWGAME_HOVER, BTN_NEWGAME)
            elif utils.isinrect(pos, BTN_LOADGAME) :
                self.disp.blit(IMG_LOADGAME_HOVER, BTN_LOADGAME)
            elif utils.isinrect(pos, BTN_QUIT) :
                self.disp.blit(IMG_QUIT_HOVER, BTN_QUIT)
            else :
                self.disp.blit(IMG_NEWGAME, BTN_NEWGAME)
                self.disp.blit(IMG_LOADGAME, BTN_LOADGAME)
                self.disp.blit(IMG_QUIT, BTN_QUIT)

            pygame.display.update()

        def onmouseclick(pos) :
            """
            Triggers the function bound to each button if clicked
            """

            if utils.isinrect(pos, BTN_NEWGAME) :
                self.newgame()
            elif utils.isinrect(pos, BTN_LOADGAME) :
                self.loadgame()
            elif utils.isinrect(pos, BTN_QUIT) :
                pygame.quit()
                sys.exit()

        self.onmousemove = onmousemove
        self.onmouseclick = onmouseclick

        # Actually display everything
        pygame.display.update()

    def newgame(self) :
        """
        Set up elements and events for a new game
        """

        # Add background
        self.disp.blit(IMG_BACKGROUND, (0,0))

        # Prompt
        prompt = utils.write("Enter the new game's name :")
        self.disp.blit(prompt, (120, 250))

        # Add a textbox
        name = Textbox.Textbox(self.disp, (120, 300), (275, 40), 10, WHITE, BLUE)
        self.textboxes.append(name)

        # Back to main
        self.disp.blit(IMG_BACK, BTN_BACK)

        # Events

        def onmousemove(pos) :
            if utils.isinrect(pos, BTN_BACK) :
                self.disp.blit(IMG_BACK_HOVER, BTN_BACK)
            else :
                self.disp.blit(IMG_BACK, BTN_BACK)

            pygame.display.update()

        def onmouseclick(pos) :
            if utils.isinrect(pos, BTN_BACK) :
                self.main()

        def onentered(textbox) :
            games = [ f for f in os.listdir(CONFIG) if f.endswith(".save") ]
            filename = textbox.gettext() + ".save"
            if filename in games :
                label = utils.write("This name already exists !", RED)
                self.disp.blit(label, (131, 350))
                textbox.reset()
            else :
                self.running = False
                l = Lab.Lab(filename)

        self.onmousemove = onmousemove
        self.onmouseclick = onmouseclick
        self.onentered = onentered

        pygame.display.update()

    def loadgame(self) :
        """
        Set up elements and events to load a game
        """

        games = [ f for f in os.listdir(CONFIG) if f.endswith(".save") ]
        if games == [] : # if there is no loaded game
            label = utils.write("There is no saved game !", RED)
            self.disp.blit(label, (131, 400))
            pygame.display.update()
            return

        # Add background
        self.disp.blit(IMG_BACKGROUND, (0,0))

        # Add "back" button
        self.disp.blit(IMG_BACK, BTN_BACK)

        # Display a button for each game
        self.btn_games = []
        pos = (0, 300)
        i = 0
        for g in games :
            label = utils.write(g.replace(".save", ""), WHITE, 17)

            if (i+1)%3 == 0 :
                pos = (350, 300+(i/3)*30, 100, 20)
            elif (i+1)%2 != 0 :
                pos = (200, 300+(i/3)*30, 100, 20)
            else :
                pos = (50, 300+(i/3)*30, 100, 20)

            self.disp.blit(label, pos)
            self.btn_games.append(pos)

            i += 1

        # Events
        def onmousemove(pos) :
            if utils.isinrect(pos, BTN_BACK) :
                self.disp.blit(IMG_BACK_HOVER, BTN_BACK)
            else :
                self.disp.blit(IMG_BACK, BTN_BACK)

                i = 0
                for btn in self.btn_games :
                    pygame.draw.rect(self.disp, BLUE, btn)

                    games = [ f for f in os.listdir(CONFIG) if f.endswith(".save") ]
                    if utils.isinrect(pos, btn) :
                        label = utils.write(games[i].replace(".save", ""), LIGHTBLUE, 17)
                    else :
                        label = utils.write(games[i].replace(".save", ""), WHITE, 17)

                    self.disp.blit(label, btn)
                    i += 1

            pygame.display.update()

        def onmouseclick(pos) :
            if utils.isinrect(pos, BTN_BACK) :
                self.main()
                return

            i = 0
            for btn in self.btn_games :
                if utils.isinrect(pos, btn) :
                    # Will load game later
                    games = [ f for f in os.listdir(CONFIG) if f.endswith(".save") ]
                    self.running = False
                    Lab.Lab(games[i], False)

                i += 1

        self.onmousemove = onmousemove
        self.onmouseclick = onmouseclick

        pygame.display.update()

if __name__ == "__main__" :
    app = App()
