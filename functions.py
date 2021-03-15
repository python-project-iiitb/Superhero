import math
import pygame
from pygame import mixer


def sh(x, y, sh_img, screen):
    screen.blit(sh_img, (x, y))


def fire(x, y, f_img, screen):
    screen.blit(f_img, (x, y))

def shoot(x,y,b_img,screen):
    screen.blit(b_img,(x,y))

def coin(x, y, c_image, screen):
    screen.blit(c_image, (x, y))

# num * num * num * num ---> bool  (type signature)


def fire_out(s_x, s_y, f_x, f_y):
    d = math.sqrt(pow(s_x - f_x, 2) + pow(s_y - f_y, 2))
    if (d < 20):
        return True
    else:
        return False
def bullet_out(s_x,s_y,b_x,b_y):
    d = math.sqrt(pow(s_x - b_x, 2) + pow(s_y - b_y, 2))
    if (d < 20):
        return True
    else:
        return False

# num * num * num * num * num * num ---> bool


def line_out(x1, y1, x2, y2, sh_x, sh_y):
    m = (y2 - y1) / (x2 - x1)
    d = -1 * ((m * sh_x) - (sh_y) + (y1 - m * x1)) / \
        math.sqrt(1 + m * m)  # line eq is m*x-y+(y1-m*x1)
    if (sh_x > x1 and sh_x < x2):
        if (d < (3) and d > -50):
            return True
        else:
            return False

# num * num * num * num ---> bool


def drag_out(xs, ys, xd, yd):
    d = math.sqrt(pow(xs - xd, 2) + pow(ys - yd, 2))
    if (d < 90):
        return True
    else:
        return False

def gunman_out(xs, ys, xg, yg):
    d = math.sqrt(pow(xs - xg, 2) + pow(ys - yg, 2))
    if (d < 90):
        return True
    else:
        return False
    

# num * num * num * num ---> bool


def collect(c_x, c_y, s_x, s_y):
    d = math.sqrt(pow((c_x - s_x), 2) + pow((c_y - s_y), 2))
    if (d < 35):
        mixer.init()
        coin_sound = mixer.Sound("coins.wav")  # coins sound
        coin_sound.play()
        c_x = 2000
        c_y = 2000
        return True
    else:
        return False

# num * num ---> bool


def cactus_out(sh_img_x, sh_img_y):
    if ((sh_img_x == 20 and sh_img_y >= 0) or (sh_img_x == 1140 and sh_img_y >= 0)):
        return True
    else:
        return False
