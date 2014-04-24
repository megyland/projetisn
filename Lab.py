#-*- coding:utf-8 -*-

import os, sys, shutil, pygame
from pygame.locals import *

import main, utils, enemy
from constants import *

# Dimensions
W, H = 16*SQUARE+PANEL, 16*SQUARE

class Lab() :

    def __init__(self, filename, new=True) :

        if new :
            shutil.copyfile("lab.txt", os.path.join(CONFIG, filename))

        self.file = os.path.join(CONFIG, filename)

        with open(os.path.join(CONFIG, filename), "r") as f :
            self.level = int(f.readline())
            self.money = int(f.readline())
            dir = f.readline().strip("\n")
            self.lab = [ list(l) for l in f ]

        # Add Schrodinger
        print(dir, "truc")
        self.schrodinger = enemy.Enemy(self.lab, dir)

        # Create the window
        self.disp = pygame.display.set_mode( (W, H) )
        self.disp.fill(WHITE)

        self.running = True
        self.walking = False # True when Schrödinger walks
        self.clock = pygame.time.Clock()

        # Add elements and start main loop
        self.main() # main square
        self.panel() # side panel
        self.selectmode() # events for select mode

        self.loop()

    def loop(self) :

        while self.running :
            # Check events
            for evt in pygame.event.get() :
                if evt.type == QUIT :
                    self.running = False
                    main.App()
                elif evt.type == MOUSEMOTION :
                    self.onmousemove(evt.pos)
                elif evt.type == MOUSEBUTTONUP :
                    self.onclick(evt.pos)

            # Move Schrödinger
            if self.walking :
                x, y = self.schrodinger.move()
                print(x)
                print(y)
                self.main()
                self.disp.blit(IMG_SCHRODINGER, (x*SQUARE, y*SQUARE - 24))
                self.clock.tick(10)

            self.clock.tick(40) # limit fps to 40

    def panel(self) :
        """
        Set up the side panel
        """

        self.btn_traps = []
        x = 16*SQUARE+10
        y = 16
        for i in TRAPS :
            self.disp.blit(i[0], (x,y))

            name = utils.write(i[1], BLACK)
            price = utils.write(str(i[3]), GRAY)
            lines = utils.formattext(i[2], 35, BLACK, 15)

            self.disp.blit(name, (x+40,y))
            self.disp.blit(price, (x+275, y))

            i = 20
            for l in lines :
                self.disp.blit(l, (x+40, y+i))
                i += 15

            self.btn_traps.append( (x, y, 330, i+5) )

            y += 75

        self.disp.blit(IMG_LAB_QUIT, BTN_LAB_QUIT)
        self.disp.blit(IMG_LAB_START, BTN_LAB_START)

        self.updatepanel()

    def updatepanel(self) :
        x = 16*SQUARE+10

        pygame.draw.rect(self.disp, WHITE, (x, 0, 250, 16))

        level = utils.write("Level : " + str(self.level), GRAY, 13)
        money = utils.write("Money : " + str(self.money), GRAY, 13)

        self.disp.blit(level, (x, 0))
        self.disp.blit(money, (x+200, 0))

        pygame.display.update()
    
    def selectmode(self) :

        def onmousemove(pos) :
            if not self.walking :
                if utils.isinrect(pos, BTN_LAB_QUIT) :
                    self.disp.blit(IMG_LAB_QUIT_HOVER, BTN_LAB_QUIT)
                elif utils.isinrect(pos, BTN_LAB_START) :
                    self.disp.blit(IMG_LAB_START_HOVER, BTN_LAB_START)
                else :
                    self.disp.blit(IMG_LAB_QUIT, BTN_LAB_QUIT)
                    self.disp.blit(IMG_LAB_START, BTN_LAB_START)

            i = 0
            for t in self.btn_traps :
                if utils.isinrect(pos, t) :
                    if self.money >= TRAPS[i][3] :
                        pygame.draw.rect(self.disp, BLACK, t, 2)
                    else :
                        pygame.draw.rect(self.disp, RED, t, 2)
                else :
                    pygame.draw.rect(self.disp, WHITE, t, 2)

                i += 1

            pygame.display.update()

        def onclick(pos) :
            if not self.walking :
                if utils.isinrect(pos, BTN_LAB_QUIT) :
                    # Save the game and back to main menu
                    with open(self.file, "w") as f :
                        f.write(str(self.level) + "\n")
                        f.write(str(self.money) + "\n")
                        for l in self.lab : f.write(''.join(l))
                    self.running = False
                    main.App()

                elif utils.isinrect(pos, BTN_LAB_START) :
                    print("Starting Schrödinger !")
                    self.walking = True

                i = 0
                for t in self.btn_traps :
                    if utils.isinrect(pos, t) and self.money >= TRAPS[i][3] :
                        self.placemode(i)
                    i += 1

        self.onmousemove = onmousemove
        self.onclick = onclick

    def main(self) :
        """
        Set up elements for the main screen
        """

        # Floor :
        self.disp.blit(IMG_FLOOR, (0,0))

        # Other elements :
        y = 0
        for l in self.lab :
            x = 0
            for c in l :
                if c == '<' : self.disp.blit(IMG_TABLE_L, (x,y))
                elif c == '=' : self.disp.blit(IMG_TABLE_M, (x,y))
                elif c == '>' : self.disp.blit(IMG_TABLE_R, (x,y))
                elif c == 'c' : self.disp.blit(IMG_BOX, (x,y))
                elif not c.isspace() :
                    print(c)
                    i = x/32
                    if i <= 0 or not l[i-1] in ['<', '=', '>'] :
                        self.disp.blit(IMG_TABLE_L, (x,y))
                    elif i >= 15 or not l[i+1] in ['<', '=', '>'] :
                        self.disp.blit(IMG_TABLE_L, (x,y))
                    else :
                        self.disp.blit(IMG_TABLE_M, (x,y))

                    if c == '.' : self.disp.blit(IMG_SPEEDOMETER, (x,y))
                    elif c == ';' : self.disp.blit(IMG_ERROR, (x,y))
                    elif c == '?' : self.disp.blit(IMG_INTERESTING, (x,y))
                    elif c == '!' : self.disp.blit(IMG_FAILED, (x,y))
                    elif c == '*' : self.disp.blit(IMG_STARTFIRE, (x,y))
                    elif c == '4' : self.disp.blit(IMG_FIRE, (x,y))
                x += 32
            y += 32

        pygame.display.update()

    def placemode(self, i) :

        img_trap  = TRAPS[i][0]
        trapname  = TRAPS[i][1]
        trapmoney = TRAPS[i][3]
        trapchar  = TRAPS[i][4]

        pygame.draw.rect(self.disp, GREEN, self.btn_traps[i], 2)
        pygame.display.update()

        def onmousemove(pos) :
            if utils.isinrect(pos, (0, 0, 16*SQUARE, 16*SQUARE)) :
                self.main()
                x, y = int(pos[0]/SQUARE), int(pos[1]/SQUARE)
                if self.lab[y][x] in ["<", "=", ">"] :
                    self.disp.blit(img_trap, (x*SQUARE,y*SQUARE))

                pygame.display.update()

        def onclick(pos) :
            x, y = int(pos[0]/SQUARE), int(pos[1]/SQUARE)
            if self.lab[y][x] in ["<", "=", ">"] :
                self.money -= trapmoney
                self.lab[y][x] = trapchar

            self.updatepanel() # update money
            self.selectmode()

        self.onmousemove = onmousemove
        self.onclick = onclick
