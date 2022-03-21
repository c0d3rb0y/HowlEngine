from main import *
from v2ops import *
import random

global p_objs
p_objs = []

def ParticleSystem(name, amount, sprite, x, y):
    global p_objs
    p_objs.append(name)
    onl = []
    for x in range(0, amount):
        onl.append(name+"_"+str(x))
        Sprite(sprite, name+"_"+str(x), x, y)
    i = 0
    for n in onl:
        i += 1
        exec(name+"_thrd_"+str(i)+""" = threading.Thread(target=ParticleMove(\""""+n+"""\"))""")
        exec(name+"_thrd_"+str(i)+".daemon = True")
        exec(name+"_thrd_"+str(i)+".start()")

def ParticleMove(name):
    rfactr = random.randint(0, 25)*0.01
    for x in range(0, 100):
        time.sleep(0.01)
        dt = deltaTime()
        Move(name, GetCoords(name)[0]+(rfactr*dt), GetCoords(name)[1]+(1*dt))
    Remove(name)
    