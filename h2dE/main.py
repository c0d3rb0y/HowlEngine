import os
import pygame
from pygame.locals import *
import threading
import time
import colorama
import tracemalloc
import playsound
import asyncio

global dirname
global screen
global background
global objs
global locktick
global run
global keys
global scriptsRunning

tracemalloc.start()

scriptsRunning = 0
dirname = os.path.dirname(__file__)
objs = []
run = False

class log():
    """Logging 4 HWL Engine"""
    colorama.init()
    def warn(msg):
        """Howl Engine Logger - Warn"""
        print(colorama.Fore.YELLOW +"WARN"+colorama.Fore.LIGHTBLUE_EX +" [" + str(int(time.time())) + "] "  + colorama.Fore.YELLOW +  msg + colorama.Fore.WHITE)
    def log(msg):
        """Howl Engine Logger - Log"""
        print(colorama.Fore.LIGHTBLUE_EX + "[" + str(int(time.time())) + "] "  + colorama.Fore.WHITE + msg)

def GetKeyDown(key):
    """Check if a key is down (pygame key format, i.e. K_LEFT for left arrow)"""
    if keys[key]:
        return True
    else:
        return False

def GetRunning():
    global run
    """Check if the program is running. It's here and I don't know why, but I'd rather write this description than delete it."""
    return run

def GetCollision(obj1n, obj2n):
    """Check for collision between 2 objects (by name)"""
    global objs
    for obj in objs:
        if obj[1] == obj1n:
            x1=obj[2].get_rect()
            x1.x = obj[3]
            x1.y = obj[4]
            break
    for obj in objs:
        if obj[1] == obj2n:
            x2=obj[2].get_rect()
            x2.x = obj[3]
            x2.y = obj[4]
            break
    return pygame.Rect.colliderect(x1, x2)

def PlayAudio(path):
    """Play audio file by path."""
    playsound.playsound(path, False)
    

def Script(path):
    """Runs a .py file. Can be any valid python, but accepts Howl Engine commands."""
    global scriptsRunning
    exec("scrthrd"+str(scriptsRunning)+""" = threading.Thread(target=exec(open(\""""+path+"""\").read()))""")
    exec("scrthrd"+str(scriptsRunning)+".daemon = True")
    exec("scrthrd"+str(scriptsRunning)+".start()")
    scriptsRunning += 1

def ScriptNT(path):
    exec(open(path).read())

def Text(txt, objName, x, y):
    """Creates a TextObject at the given coordinates."""
    global screen
    global background
    global objs
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    rendered = font.render(txt, 1, (10, 10, 10))
    log.log("init textobj: " + objName)
    objs.append(["text", objName, rendered, x, y])

def GetCoords(objName):
    """Get coordinates of object by name."""
    global objs
    for obj in objs:
        if obj[1] == objName:
            x=obj[3]
            y=obj[4]
            break
    return [x, y]

def Sprite(path, objName, x, y):
    """Creates a SpriteObject at the given coordinates."""
    global screen
    global background
    global objs
    
    log.log("init spriteobj: " + objName)
    objs.append(["sprite", objName, pygame.image.load(path), x, y])

def Move(objName, x, y):
    """Moves an object to the specified X and Y coordinates."""
    global objs
    for obj in objs:
        if obj[1] == objName:
            obj[3]=x
            obj[4]=y

def GetObjAmount():
    """Returns the amount of objects that are currently loaded."""
    global objs
    return len(objs)

def Rotate(objName, rotation):
    """Rotates Sprite Objects."""
    if rotation >= 360:
        rotation = rotation - 360
        log.warn("rotspr: WARN: Rotation bigger than 360! Subtracting (attempt minimization)")
    global objs
    for x in objs:
        for y in x:
            if y == objName:
                x[2] = pygame.transform.rotate(x[2], rotation)
                log.log("rotate spr: " + objName)
                return
    log.warn("rotspr: could not find obj")

def ChangeOrder(objName, pos):
    """Changes the ordering of the objects onscreen."""
    if pos > GetObjAmount():
        log.warn("order: Cannot move out of list!")
        return
    if pos < 0:
        log.warn("order: Sort position cannot be negative!")
        return
    global objs
    for x in objs:
        for y in x:
            if y == objName:
                objs.insert(pos, x)
                objs.remove(x)
                log.log("sort obj: " + objName)
                return
    log.warn("COULD NOT SORT OBJECT " + objName)

def Stop():
    """Stop application."""
    global run
    global objs
    run = 0
    objs = []
    pygame.display.quit()
    pygame.quit()
    quit()

def Remove(objName):
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
    log.warn("COULD NOT YEET OBJECT " + objName)



def Init(w, h, bg, fps):
    """init window, bg color format is a tuple btw. for examplez, 1920 1080 (0, 0, 0) 60 for 60fps black bg 1080p"""
    global screen
    global background
    global objs
    global keys
    global run
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Howl Engine')
    clock = pygame.time.Clock()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(bg)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    run = True
    while run == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                Stop()
        keys=pygame.key.get_pressed()
        screen.blit(background, (0, 0))
        for x in objs:
            screen.blit(x[2], (x[3], x[4]))
        clock.tick(fps)
        pygame.display.flip()
        

    pygame.quit()
if __name__ == '__main__':
    Script(os.path.join(dirname, "base_assets/script.py"))
    
