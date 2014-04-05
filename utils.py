#-*- coding:utf-8 -*-

import pygame
from pygame.locals import *

def isinrect(pos, rect) :
    """
    pos is a tuple (x, y)
    rect is a tuple (x, y, width, height)
    returns True if pos is in the rect
    """

    return pos[0] > rect[0] and pos[1] > rect[1] and pos[0] < rect[0]+rect[2] and pos[1] < rect[1]+rect[3]

def write(text, color=(255, 255, 255), size=20) :
    """
    Returns a label
    """

    font = pygame.font.get_default_font()
    renderer = pygame.font.Font(font, size)

    return renderer.render(text, True, color)
