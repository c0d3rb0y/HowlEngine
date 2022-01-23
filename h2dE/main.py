import os
import pygame
from pygame.locals import *
import threading
import time
import colorama

global screen
global background
global objs
global run

global keysDown

objs = []
keysDown = []

class log():
    colorama.init()
    """Logging 4 HWL Engine"""
    def warn(msg):
        print(colorama.Fore.YELLOW + "[" + str(int(time.time())) + "] " + msg + colorama.Style.RESET)
    def log(msg):
        print("[" + str(int(time.time())) + "] " + msg)

def GetKeysDown():
    return keysDown

def GetRunning():
    return run

def script(path):
    """Runs a .py file. Can be any valid python, but accepts Howl Engine commands."""
    exec(open(path).read())

def text(txt, objName, x, y):
    """Creates a TextObject at the given coordinates."""
    global screen
    global background
    global objs
    
    font = pygame.font.Font(None, 36)
    rendered = font.render(txt, 1, (10, 10, 10))
    log.log("init textobj: " + objName)
    objs.append(["text", objName, rendered, x, y])

def getCoords(objName):
    global objs
    for obj in objs:
        if obj[1] == objName:
            x=obj[3]
            y=obj[4]
            break
    return [x, y]

def sprite(path, objName, x, y):
    """Creates a SpriteObject at the given coordinates."""
    global screen
    global background
    global objs
    
    log.log("init spriteobj: " + objName)
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
        log.warning("rotspr: WARN: Rotation bigger than 360!")
    global objs
    for x in objs:
        for y in x:
            if y == objName:
                x[2] = pygame.transform.rotate(x[2], rotation)
                log.log("rotate spr: " + objName)
                return
    log.warning("rotspr: could not find obj")

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
                log.log("sort obj: " + objName)
                return
    log.warning("COULD NOT SORT OBJECT " + objName)

def stop():
    """Stop application."""
    global run
    global objs
    run = 0
    objs = []

def remove(objName):
    """Remove object based on object name you initialized it as."""
    global screen
    global background
    global objs
    for x in objs:
        for y in x:
            if y == objName:
                objs.remove(x)
                log.log("yeet obj: " + objName)
                return
    log.warning("COULD NOT YEET OBJECT " + objName)



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
                quit()
        keys=pygame.key.get_pressed()
        try:
            keysDown.remove("r") 
        except:
            pass
        try:
            keysDown.remove("l") 
        except:
            pass
        try:
            keysDown.remove("u") 
        except:
            pass
        try:
            keysDown.remove("d") 
        except:
            pass
        if keys[K_LEFT]:
            keysDown.append("l")
        if keys[K_RIGHT]:
            keysDown.append("r")
        if keys[K_UP]:
            keysDown.append("u")
        if keys[K_DOWN]:
            keysDown.append("d")
        screen.blit(background, (0, 0))
        for x in objs:
            screen.blit(x[2], (x[3], x[4]))
        clock.tick(fps)
        pygame.display.flip()
        

    pygame.quit()

if __name__ == '__main__':
    script("h2dE/base_assets/script.py")

    
