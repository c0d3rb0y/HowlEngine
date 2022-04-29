import os
import pygame
from pygame.locals import *
import threading
import time
import colorama
import sys
import random
import numpy as np

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
global ambient
global scriptsRunning
global clock
global illuminationList

ver = "2022.2"
scriptsRunning = 0
dirname = os.path.dirname(__file__)
objs = []
illuminationList = []
volume = 1.0
ambient = 25
lightingOn = True
run = False
showColliders = False


class log():
    """Logging 4 HWL Engine"""
    colorama.init()

    def warn(msg):
        """Howl Engine Logger - Warn"""
        print(colorama.Fore.YELLOW + "WARN" + colorama.Fore.LIGHTBLUE_EX + " [" + str(
            int(time.time())) + "] " + colorama.Fore.YELLOW + msg + colorama.Fore.WHITE)

    def log(msg):
        """Howl Engine Logger - Log"""
        print(colorama.Fore.LIGHTBLUE_EX + "[" + str(int(time.time())) + "] " + colorama.Fore.WHITE + msg)

    def error(msg):
        """Howl Engine Logger - Error"""
        print(colorama.Fore.RED + "ERROR" + " [" + str(int(time.time())) + "] " + msg + colorama.Fore.WHITE)
class particles():
    """Particle module of h2dE"""

    global p_objs
    p_objs = []

    def ParticleSystemNT(name, amount, sprite, x, y, xchange, tIme):
        """Creates a ParticleSystem at the given coordinates. Non-threaded. Please do not use."""
        global p_objs
        p_objs.append(name)
        onl = []
        for a in range(0, amount):
            onl.append(name + "_" + str(a))
            Sprite(sprite, name + "_" + str(a), x, y)
        i = 0
        randfactors = []
        rf2 = []
        for c in range(0, len(onl)):
            rfactr = random.randint(-1 * xchange, xchange) * 0.5
            rf2c = random.randint(5, 10) * 0.1
            rf2.append(rf2c)
            randfactors.append(rfactr)
        i = 0
        while (name in p_objs) and (tIme > i):
            for b in range(0, 100):
                time.sleep(0.001)
                for n in onl:
                    i += 1
                    if random.randint(0, 10) == 5:
                        Move(n, x, y)
                    else:
                        Move(n, GetCoords(n)[0] + randfactors[onl.index(n)], GetCoords(n)[1] - (2 * rf2[onl.index(n)]))
            for n in onl:
                Move(n, x, y)
            i += 1
        for n in onl:
            Remove(n)

    def ParticleSystem(name, amount, sprite, x, y, xchange, time):
        """Creates a ParticleSystem at the given coordinates. Threaded."""
        pthread = threading.Thread(particles.ParticleSystemNT(name, amount, sprite, x, y, xchange, time))
        pthread.start()

    def RemoveParticleSystem(name):
        """Removes a ParticleSystem by name."""
        global p_objs
        p_objs.remove(name)


class GameState():
    """List of strings for defining current state. Can be used on its own, or for scene sorting."""

    def __init__(self, current, all):
        if current in all:
            self.current = current
            self.all = all
        else:
            print("Failed to create GameState! Current state is not in provided list of states.")

    def setCurrent(self, state):
        if state in self.all:
            self.current = state
        else:
            print("Failed to set current state! State is not in provided list of states.")

    def getCurrent(self):
        return self.current

    def newState(self, state):
        self.all.append(state)

    def deleteState(self, state):
        self.all.remove(state)


class Scene():
    """Instantly loadable list of objects."""

    def __init__(self, name, objects):
        self.name = name
        self.objects = objects
        self.lastObjects = []

    def getName(self):
        return self.name

    def getObjects(self):
        return self.objects

    def getLastObjects(self):
        return self.lastObjects

    def lastObjectsToScene(self, name):
        return Scene(name, self.lastObjects)

    def load(self):
        self.lastObjects = objs
        ClearObjects()
        for x in self.objects:
            objs.append(x)


def ClearObjects():
    """Clears all objects"""
    global objs
    objs = []


def SetAmbient(val):
    """Set the ambient light."""
    global ambient
    ambient = val


def GetAmbient():
    """Returns ambient light. thank u copilot"""
    return ambient


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
    """Check if the program is running. It's here and I don't know why, but I'd rather write this description than delete it."""
    global run
    return run

def GetTime():
    """Get the current time in seconds. This is a float."""
    return pygame.time.get_ticks() / 1000.0

def GetCollision(obj1n, obj2n):
    """Check for collision between 2 objects (by name)"""
    global objs
    for obj in objs:
        if obj[1] == obj1n:
            x1 = obj[2].get_rect()
            x1.x = obj[3]
            x1.y = obj[4]
            break
    for obj in objs:
        if obj[1] == obj2n:
            x2 = obj[2].get_rect()
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
    sound.set_volume(volume)  # thanks copilot and overflow
    sound.play()


def Script(path):
    """Runs a .py file. Can be any valid python, but accepts Howl Engine commands."""
    global scriptsRunning
    scriptsRunning += 1
    exec("scrthrd" + str(scriptsRunning) + """ = threading.Thread(target=exec(open(\"""" + path + """\").read()))""")
    exec("scrthrd" + str(scriptsRunning) + ".daemon = True")
    exec("scrthrd" + str(scriptsRunning) + ".start()")


def ScriptNT(path):
    """For if some reason you need to run a script without threading."""
    exec(open(path).read())


def Text(txt, objName, x, y, color):
    """Creates a TextObject at the given coordinates."""
    global screen
    global background
    global objs
    pygame.font.init()

    font = pygame.font.Font(None, 36)
    rendered = font.render(txt, 1, color)
    log.log("init textobj: " + objName)
    objs.append(["text", objName, rendered, x, y])


def ReturnText(txt, objName, x, y, color):
    """Returns a TextObject with the given properties."""
    global screen
    global background
    global objs
    pygame.font.init()

    font = pygame.font.Font(None, 36)
    rendered = font.render(txt, 1, color)
    log.log("load textobj: " + objName)
    return ["text", objName, rendered, x, y]


def ReturnSprite(path, objName, x, y):
    """Returns a SpriteObject with the given properties."""
    global screen
    global background
    global objs
    log.log("load spriteobj: " + objName)
    return ["sprite", objName, pygame.image.load(path).convert_alpha(), x, y]


def GetCoords(objName):
    """Get coordinates of object by name."""
    global objs
    for obj in objs:
        if obj[1] == objName:
            x = obj[3]
            y = obj[4]
            break
    return [x, y]


def GetRunningScripts():
    """Returns the amount of scripts that are currently running. Copilot wrote this."""
    global scriptsRunning
    return scriptsRunning


def GetVolume():
    """Returns the volume of the audio. Good one copilot."""
    global volume
    return volume


def SetIcon(path):
    """Sets the icon of the window. Damn, copilot, I didn't even begin think of this one. Great job."""
    pygame.display.set_icon(pygame.image.load(path))


def Sprite(path, objName, x, y):
    """Creates a SpriteObject at the given coordinates."""
    global screen
    global background
    global objs

    log.log("init spriteobj: " + objName)
    objs.append(["sprite", objName, pygame.image.load(path).convert_alpha(), x, y])


def Move(objName, x, y):
    """Moves an object to the specified X and Y coordinates."""
    global objs

    for obj in objs:
        if obj[1] == objName:
            obj[3] = x
            obj[4] = y


def GetObjAmount():
    """Returns the amount of objects that are currently loaded."""
    global objs
    return len(objs)


def GetObj(objName):
    """Returns an object by name. Copilot wrote this. I don't know why."""
    global objs
    for obj in objs:
        if obj[1] == objName:
            return obj


def GetObjByIndex(index):
    """Returns an object by index in renderlist. I don't know who the hell would need such a thing, but guess what? Copilot decided it was time to make it."""
    global objs
    return objs[index]


def howlBlit(objName):
    """Blits a specific object by name. I don't know why you would use this, but I guess it's here."""
    global objs
    for obj in objs:
        if obj[1] == objName:
            screen.blit(obj[2], (obj[3], obj[4]))


def SetBackground(path):
    """Sets the background image, and also can cause that weird windows vista effect if it's not the right size... Thanks anyway, copilot."""
    global background
    global screen
    background = pygame.image.load(path)
    pygame.transform.scale(background, (screen.get_width(), screen.get_height()))


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


def SwapDebugLightingOn():
    """Flips the lighting mode, for debug reasons. Copilot wrote this."""
    global lightingOn
    lightingOn = not lightingOn


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


def GetDistance(obj1, obj2):
    """Returns the distance between two objects. From github copilot"""
    global objs
    for x in objs:
        for y in x:
            if y == obj1:
                x1 = x[3]
                y1 = x[4]
            if y == obj2:
                x2 = x[3]
                y2 = x[4]
    return pygame.math.Vector2(x1, y1).distance_to(pygame.math.Vector2(x2, y2))


def GetAngle(obj1, obj2):
    """Returns the angle between two objects. From github copilot"""
    global objs
    for x in objs:
        for y in x:
            if y == obj1:
                x1 = x[3]
                y1 = x[4]
            if y == obj2:
                x2 = x[3]
                y2 = x[4]
    return np.arctan2(y2 - y1, x2 - x1)


def GetAngleToMouse(objName):
    """Returns the angle between an object and the mouse. From copilot"""
    global mouseX
    global mouseY
    global objs
    for x in objs:
        for y in x:
            if y == objName:
                x1 = x[3]
                y1 = x[4]
    return np.arctan2(mouseY - y1, mouseX - x1)


def GetDistanceToMouse(objName):
    """Returns the distance between an object and the mouse. Thanks copilot"""
    global mouseX
    global mouseY
    global objs
    for x in objs:
        for y in x:
            if y == objName:
                x1 = x[3]
                y1 = x[4]
    return pygame.math.Vector2(x1, y1).distance_to(pygame.math.Vector2(mouseX, mouseY))


def SetBrightness(obj, brightness):
    global illuminationList
    complete = 0
    for x in illuminationList:
        if x[0] == obj:
            if x[1] == brightness:
                complete = 1
            else:
                x[1] = brightness
                complete = 1
                log.log("illum: " + obj + " set to " + str(brightness))
                break
    if complete == 0:
        illuminationList.append([obj, brightness])
        log.log("illum: Added " + obj + " to illumination list")


def GetDebugLightingEnabled():
    global lightingOn
    return lightingOn


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
        exec("scrthrd" + str(x) + "._stop()")
    initT._stop()
    sys.exit()


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
    return clock.get_time() / 1000.0


def Init(w, h, bg, fps):
    """init window, bg color format is a tuple btw. for examplez, 1920 1080 (0, 0, 0) 60 for 60fps black bg 1080p"""
    global initT
    initT = threading.Thread(target=InitNT, args=(w, h, bg, fps))
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
    global lightingOn
    global illuminationList
    global ambient
    global clock
    global ver
    global showColliders
    global run
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Howl Engine')
    clock = pygame.time.Clock()
    pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

    introbg = pygame.Surface(screen.get_size())
    introbg = introbg.convert()
    introbg.fill((0, 0, 0))
    ialpha = 0
    i = 0
    SetIcon(os.path.join(dirname, "base_assets/howl.png"))
    logo = pygame.image.load(os.path.join(dirname, "base_assets/howl.png"))
    etxt = pygame.font.Font(None, 36).render("Howl Engine " + ver, 1, (255, 255, 255))
    for x in range(0, fps * 5):
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
        screen.blit(logo, (w / 2 - (485 / 2), h / 2 - (540 / 2)))
        screen.blit(etxt, (w / 2 - (pygame.font.Font(None, 36).size("Howl Engine " + ver)[0] / 2), h - 40))
        clock.tick(fps)
        pygame.display.flip()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(bg)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    run = True
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                Stop()

        # important stuff (nonblit)
        keys = pygame.key.get_pressed()

        # start blitting
        try:
            screen.blit(background, (0, 0))
        except:
            bguls = background
            bguls.unlock()
            screen.blit(bguls, (0, 0))
            log.warn("blit: background is locked! how the high fructose corn syrup did you do that?")

        # obj blitting
        for x in objs:
            try:
                if lightingOn == True:
                    limage = x[2].copy()
                    limage.fill((ambient, ambient, ambient), special_flags=pygame.BLEND_RGB_ADD)
                    for e in illuminationList:
                        if x[1] in e:
                            limage.fill((e[1], e[1], e[1]), special_flags=pygame.BLEND_RGB_ADD)
                    screen.blit(limage, (x[3], x[4]))
                else:
                    screen.blit(x[2], (x[3], x[4]))
                if showColliders == True:
                    pygame.draw.rect(x[2], (0, 255, 0), (0, 0, x[2].get_size()[0], x[2].get_size()[1]), 3)
            except:
                log.warn("blit: " + x[1] + " was locked, or had some kind of blit error\n")
                uls = x[2]
                uls.unlock()
                screen.blit(uls, (x[3], x[4]))
                if showColliders == True:
                    pygame.draw.rect(x[2], (255, 255, 0), (0, 0, x[2].get_size()[0], x[2].get_size()[1]), 3)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
