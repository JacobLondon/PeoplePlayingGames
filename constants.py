import pygame

class Color(object):

    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    blue = (0,0,255)
    green = (0,255,0)

    background = black
    foreground = white

    button = (130,130,130)
    hover = (200,200,255)

class Dir(object):

    right = 2
    left = 3
    down = 1
    up = -1

class Font(object):
    pygame.font.init()
    standard = pygame.font.SysFont('Sans MS', 20)
    menu = pygame.font.SysFont('Sans MS', 60)
    button = pygame.font.SysFont('Sans MS', 40)

class Anchor(object):
    northwest = 0
    northeast = 1
    southeast = 2
    southwest = 3
    center = 4

class Mouse(object):
    l_click = 1
    m_click = 2
    r_click = 3
    s_up = 4
    s_down = 5
