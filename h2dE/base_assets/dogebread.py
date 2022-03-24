from main import *


while GetRunning() == True:
    dTime = deltaTime()
    
    if GetKeyDown(K_RIGHT) and (GetCoords("dogebread")[0] <= 1180):
        r = True
        Move("dogebread", GetCoords("dogebread")[0]+0.25*dTime, GetCoords("dogebread")[1])

    if GetKeyDown(K_LEFT) and (GetCoords("dogebread")[0] >= 0):
        l = True
        Move("dogebread", GetCoords("dogebread")[0]-0.25*dTime, GetCoords("dogebread")[1])    

    if GetKeyDown(K_UP) and (GetCoords("dogebread")[1] >= 000):
        u = True
        Move("dogebread", GetCoords("dogebread")[0], GetCoords("dogebread")[1]-0.25*dTime)

    if GetKeyDown(K_DOWN) and (GetCoords("dogebread")[1] <= 620):
        d = True
        Move("dogebread", GetCoords("dogebread")[0], GetCoords("dogebread")[1]+0.25*dTime)