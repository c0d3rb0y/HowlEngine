import os
import pygame
from pygame.locals import *
import threading
import time
import colorama
import playsound
import sys

global dirname
global screen
global background
global objs
global ver
global run
global keys
global initT
global volume
global showColliders
global scriptsRunning
global clock


ver = "2022.2"
scriptsRunning = 0
dirname = os.path.dirname(__file__)
objs = []
volume = 1.0
run = False
showColliders = False

class log():
    """Logging 4 HWL Engine"""
    colorama.init()
    def warn(msg):
        """Howl Engine Logger - Warn"""
        print(colorama.Fore.YELLOW +"WARN"+colorama.Fore.LIGHTBLUE_EX +" [" + str(int(time.time())) + "] "  + colorama.Fore.YELLOW +  msg + colorama.Fore.WHITE)
    def log(msg):
        """Howl Engine Logger - Log"""
        print(colorama.Fore.LIGHTBLUE_EX + "[" + str(int(time.time())) + "] "  + colorama.Fore.WHITE + msg)

def GetMousePosition():
    """returns x, y tuple"""
    mx, my = pygame.mouse.get_pos()
    return (mx, my)

def GetDebugCollidersShown():
    """more debug shit i needed, not really useful in games"""
    global showColliders
    return showColliders

def SetDebugCollidersShown(setto):
    """debug shit"""
    global showColliders
    showColliders = setto

def GetLMBDown():
    """idk, What do you think it does? returns bool"""
    return pygame.mouse.get_pressed()[0]

def GetRMBDown():
    """idk, What do you think it does? returns bool"""
    return pygame.mouse.get_pressed()[2]

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

def GetTouchingMouse(name):
    """The name explains this pretty well. Returns bool"""
    global objs
    for obj in objs:
        if obj[1] == name:
            x1 = obj[2].get_rect()
            x1.x = obj[3]
            x1.y = obj[4]
            break
    return x1.collidepoint(pygame.mouse.get_pos())

def PlayAudio(path):
    """Play audio file by path."""
    global volume
    sound = pygame.mixer.Sound(path)
    sound.set_volume(volume)   # Now plays at 90% of full volume.
    sound.play()
    

def Script(path):
    """Runs a .py file. Can be any valid python, but accepts Howl Engine commands."""
    global scriptsRunning
    scriptsRunning += 1
    exec("scrthrd"+str(scriptsRunning)+""" = threading.Thread(target=exec(open(\""""+path+"""\").read()))""")
    exec("scrthrd"+str(scriptsRunning)+".daemon = True")
    exec("scrthrd"+str(scriptsRunning)+".start()")

def ScriptNT(path):
    """For if some reason you need to run a script without threading."""
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
    global scriptsRunning
    global objs
    global initT
    run = 0
    objs = []
    pygame.display.quit()
    pygame.quit()
    for x in range(0, scriptsRunning):
        exec("scrthrd"+str(x)+"._stop()")
    initT._stop()
    sys.exit()
    quit()

def SetVolume(vol):
    """Set the volume of audio files."""
    global volume
    volume = vol


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

def deltaTime():
    """Multiply your movement by this for smooth."""
    global clock
    return clock.get_time()/1000.0

def Init(w, h , bg, fps):
    """init window, bg color format is a tuple btw. for examplez, 1920 1080 (0, 0, 0) 60 for 60fps black bg 1080p"""
    global initT
    initT = threading.Thread(target=InitNT, args=(w,h,bg,fps))
    initT.daemon = True
    initT.start()

def SetTitle(title):
    """Set the title of the window."""
    pygame.display.set_caption(title)

def InitNT(w, h, bg, fps):
    """Non-threaded init. DON'T USE THIS"""
    global screen
    global background
    global objs
    global keys
    global clock
    global ver
    global showColliders
    global run
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Howl Engine')
    clock = pygame.time.Clock()

    introbg = pygame.Surface(screen.get_size())
    introbg = introbg.convert()
    introbg.fill((0, 0, 0))
    ialpha = 0
    i = 0
    logo = pygame.image.load(os.path.join(dirname, "base_assets/howl.png"))
    etxt = pygame.font.Font(None, 36).render("Howl Engine " + ver, 1, (255, 255, 255))
    for x in range(0, fps*5):
        i += 1
        if i < 60:
            ialpha += 4.25
        if i > 240:
            ialpha -= 4.25
        for event in pygame.event.get():
            if event.type == QUIT:
                Stop()
        
        logo.set_alpha(ialpha)
        etxt.set_alpha(ialpha)

        screen.blit(introbg, (0, 0))
        screen.blit(logo, (w/2-(485/2), h/2-(540/2)))
        screen.blit(etxt, (w/2-(pygame.font.Font(None, 36).size("Howl Engine " + ver)[0]/2),h-40))
        clock.tick(fps)
        pygame.display.flip()
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
        
        #important stuff (nonblit)
        keys=pygame.key.get_pressed()
        
        
        #start blitting
        screen.blit(background, (0, 0))

        #obj blitting
        for x in objs:
            try:
                screen.blit(x[2], (x[3], x[4]))
                if showColliders == True:
                    pygame.draw.rect(x[2], (0, 255, 0), (0, 0, x[2].get_size()[0], x[2].get_size()[1]), 3)
            except:
                log.warn("blit: "+x[1]+" was locked, or had some kind of blit error\n")
                uls = x[2]
                uls.unlock()
                screen.blit(uls, (x[3], x[4]))
                if showColliders == True:
                    pygame.draw.rect(x[2], (255, 255, 0), (0, 0, x[2].get_size()[0], x[2].get_size()[1]), 3)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
if __name__ == '__main__':
    Script(os.path.join(dirname, "base_assets/script.py"))