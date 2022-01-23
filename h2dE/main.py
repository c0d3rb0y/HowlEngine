import os
import pygame
from pygame.locals import *
import threading
import time
import logging

global screen
global background
global objs
global run
objs = []

def script(path):
    """Runs a .py file. Can be any valid python, but accepts Howl Engine commands."""
    scriptF = open(path, "r")
    lines = scriptF.readlines()
    i = 0
    while (i != len(lines)):
        for line in lines:
            i += 1
            exec(line)

def text(txt, objName, x, y):
    """Creates a TextObject at the given coordinates."""
    global screen
    global background
    global objs
    font = pygame.font.Font(None, 36)
    rendered = font.render(txt, 1, (10, 10, 10))
    print("init textobj: " + objName)
    objs.append(["text", objName, rendered, x, y])

def sprite(path, objName, x, y):
    """Creates a SpriteObject at the given coordinates."""
    global screen
    global background
    global objs
    print("init spriteobj: " + objName)
    objs.append(["sprite", objName, pygame.image.load(path), x, y])

def move(objName, x, y):
    """Moves an object to the specified X and Y coordinates."""
    global objs
    for obj in objs:
        if obj[1] == objName:
            obj[3]=x
            obj[4]=y

def getObjAmount():
    """Returns the amount of objects that are currently loaded."""
    global objs
    return len(objs)

def rotate(objName, rotation):
    """Rotates Sprite Objects."""
    if rotation >= 360:
        rotation = rotation - 360
        print("rotspr: WARN: Rotation bigger than 360!")
    global objs
    for x in objs:
        for y in x:
            if y == objName:
                x[2] = pygame.transform.rotate(x[2], rotation)
                print("rotate spr: " + objName)
                return
    print("rotspr: could not find obj")

def changeOrder(objName, pos):
    """Changes the ordering of the objects onscreen."""
    if pos > getObjAmount():
        print("order: FATALERR: Cannot move out of list!")
        return
    if pos < 0:
        print("order: FATALERR: Sort position cannot be negative!")
        return
    global objs
    for x in objs:
        for y in x:
            if y == objName:
                objs.insert(pos, x)
                objs.remove(x)
                print("sort obj: " + objName)
                return
    print("COULD NOT SORT OBJECT " + objName)

def stop():
    """Stop application."""
    global run
    global objs
    run = 0
    objs = []
    quit()

def remove(objName):
    """Remove object based on object name you initialized it as."""
    global screen
    global background
    global objs
    for x in objs:
        for y in x:
            if y == objName:
                objs.remove(x)
                print("yeet obj: " + objName)
                return
    print("COULD NOT YEET OBJECT " + objName)



def init(w, h, bg, fps):
    """Start up window N stuff! 
    bg color format is like this btw: (R, G, B)
    DO NOT FORGET PARENTHESES"""
    global screen
    global background
    global objs
    global run
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Howl Engine')
    clock = pygame.time.Clock()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(bg)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    run = 1

    while run == 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                stop()
        screen.blit(background, (0, 0))
        for x in objs:
            screen.blit(x[2], (x[3], x[4]))
        clock.tick(fps)
        pygame.display.flip()
        

    pygame.quit()

if __name__ == '__main__':
    script("h2dE/base_assets/script.py")

    
