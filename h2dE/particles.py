from main import *
from v2ops import *
import random

global p_objs
p_objs = []

def ParticleSystem(name, amount, sprite, x, y, xchange, time):
    """Creates a ParticleSystem at the given coordinates. Threaded."""
    pthread = threading.Thread(ParticleSystemNT(name, amount, sprite, x, y, xchange, time))
    pthread.start()

def ParticleSystemNT(name, amount, sprite, x, y, xchange, tIme):
    """Creates a ParticleSystem at the given coordinates. Non-threaded. Please do not use."""
    global p_objs
    p_objs.append(name)
    onl = []
    for a in range(0, amount):
        onl.append(name+"_"+str(a))
        Sprite(sprite, name+"_"+str(a), x, y)
    i = 0
    randfactors = []
    rf2 = []
    for c in range(0, len(onl)):
            rfactr = random.randint(-1*xchange, xchange)*0.5
            rf2c = random.randint(5,10)*0.1
            rf2.append(rf2c)
            randfactors.append(rfactr)
    i = 0
    while (name in p_objs) and (tIme > i):
        for b in range(0, 100):
            time.sleep(0.001)
            for n in onl:
                i += 1
                if random.randint(0,10) == 5:
                    Move(n, x, y)
                else:
                    Move(n, GetCoords(n)[0]+randfactors[onl.index(n)], GetCoords(n)[1]-(2*rf2[onl.index(n)]))
        for n in onl:
            Move(n, x, y)
        i+=1
    for n in onl:
        Remove(n)

def RemoveParticleSystem(name):
    """Removes a ParticleSystem by name."""
    global p_objs
    p_objs.remove(name)