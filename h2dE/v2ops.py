from main import *
import pygame
import time
import math
import threading

def move(objName, x, y, seconds):
    """Move object over time."""
    mt = threading.Thread(target=moveNONASYNC, args=(objName, x, y, seconds))
    mt.start()

def moveNONASYNC(objName, x, y, seconds):
    """please nono use"""
    i = 0
    for obj in objs:
        if obj[1] == objName:
            break
        i += 1
    dist = (x - (objs[i][3]), (y - objs[i][4]))
    xM = dist[0]/100
    yM = dist[1]/100
    for x in range(1, 100):
        time.sleep(0.01)
        objs[i][3] += xM
        objs[i][4] += yM