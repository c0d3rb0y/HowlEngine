from main import *
from v2ops import *
import random
import asyncio

global p_objs
p_objs = []

async def ParticleSystem(name, amount, sprite, x, y):
    global p_objs
    p_objs.append(name)
    onl = []
    for a in range(0, amount):
        onl.append(name+"_"+str(a))
        Sprite(sprite, name+"_"+str(a), x, y)
    i = 0
    randfactors = []
    for x in range(0, len(onl)):
        rfactr = random.randint(-10, 10)*0.5
        randfactors.append(rfactr)
    for x in range(0, 100):
        time.sleep(0.001)
        for n in onl:
            i += 1
            Move(n, GetCoords(n)[0]+randfactors[onl.index(n)], GetCoords(n)[1]-2)
    for n in onl:
        Remove(n)
    