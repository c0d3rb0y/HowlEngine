from main import *
from v2ops import *

Init(1280, 720, (49,73,117), 60)
while GetRunning() == False:
    time.sleep(0)

Sprite(os.path.join(dirname, "base_assets/dog.png"), "dogobj", 10, 10)
Text("Hi", "hiobj", 60, 50)
time.sleep(1)
while GetKeyDown(K_SPACE) == False:
    particles.ParticleSystem("ps", 100, os.path.join(dirname, "base_assets/test.bmp"), 640, 360, 10, 5)
    Rotate("hiobj", 90)
    MoveT("hiobj", 80, 70, 1)
    MoveT("dogobj", 30, 30, 1)
    time.sleep(3)
    ChangeOrder("dogobj", 2)
    Rotate("dogobj", -10)
    Sprite(os.path.join(dirname, "base_assets/test.bmp"), "testobj", 400, 300)
    Text("IM HERE NOW TOO HAHAHAHHAHAHAHAHHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHHAHAAHAHAHHAHAHAHAHHAHAHAHAHHA", "hahaobj", 320, 200)
    Remove("hiobj")
    Text("why tho", "bruhobj", 60, 50)
    time.sleep(0.1)
    Move("testobj", 350, 250)
    time.sleep(0.1)
    Move("testobj", 150, 150)
    time.sleep(0.1)
    Move("testobj", 450, 350)
    time.sleep(0.1)
    Move("testobj", 450, 150)
    time.sleep(0.1)
    Move("testobj", 400, 300)
    time.sleep(3)
    Remove("dogobj")
    Remove("bruhobj")
    Remove("testobj")
    Remove("hahaobj")
    Text("ok that was the engine test cool", "endtxt", 100, 180)
    time.sleep(5)
    if GetKeyDown(K_d):
        SetVolume(0.0)
        # debug flag
    Remove("endtxt")
    Text("now u can move this doge across de scren (arrow keys), except no touch smiley face", "end2txt", 100, 180)
    Sprite(os.path.join(dirname, "base_assets/test.bmp"), "randomthingy", 400, 300)
    Sprite(os.path.join(dirname, "base_assets/dogebread.png"), "dogebread", 100, 160)
    SetBrightness("randomthingy", 100)
    txtch = False
    break
i = 5
while GetRunning() == 1:
    r = False
    l = False
    u = False
    d = False
    if i == 5:
        ffdist = GetDistance("dogebread", "randomthingy")/20
        i = 0
    else:
        i+=1
    dTime = deltaTime()
    
    if GetDebugLightingEnabled():
        SetBrightness("dogebread", 70-(ffdist))

    if GetLMBDown():
        Move("randomthingy", GetMousePosition()[0], GetMousePosition()[1])
    
    if GetRMBDown():
        Move("randomthingy", 400, 300)

    if GetDebugLightingEnabled():
        if GetKeyDown(K_RIGHT) and (GetCoords("dogebread")[0] <= 1180):
            r = True
            Move("dogebread", GetCoords("dogebread")[0]+1*dTime, GetCoords("dogebread")[1])

        if GetKeyDown(K_LEFT) and (GetCoords("dogebread")[0] >= 0):
            l = True
            Move("dogebread", GetCoords("dogebread")[0]-1*dTime, GetCoords("dogebread")[1])    

        if GetKeyDown(K_UP) and (GetCoords("dogebread")[1] >= 000):
            u = True
            Move("dogebread", GetCoords("dogebread")[0], GetCoords("dogebread")[1]-1*dTime)

        if GetKeyDown(K_DOWN) and (GetCoords("dogebread")[1] <= 620):
            d = True
            Move("dogebread", GetCoords("dogebread")[0], GetCoords("dogebread")[1]+1*dTime)
    else:
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
    
    if GetKeyDown(K_d):
        SetDebugCollidersShown(True)
        # debug flag again because why not lol
    
    if GetKeyDown(K_l):
        SetBackground(os.path.join(dirname, "base_assets/dog.png"))
        # just another debug flag
    
    if GetKeyDown(K_1):
        PlayAudio(os.path.join(dirname, "base_assets/sigmamale.mp3"))
        while GetKeyDown(K_1):
            time.sleep(0)
    if GetKeyDown(K_2) and GetAmbient() > 10:
        SetAmbient(GetAmbient()-10)
        while GetKeyDown(K_2):
            time.sleep(0)
    if GetKeyDown(K_3) and GetAmbient() < 240:
        SetAmbient(GetAmbient()+10)
        while GetKeyDown(K_3):
            time.sleep(0)
        
    if GetKeyDown(K_4):
        SwapDebugLightingOn()
        while GetKeyDown(K_4):
            time.sleep(0)
        # debug flag again
    
    if GetCollision("dogebread", "randomthingy"):
        if GetDebugLightingEnabled():
            if r == True:
                Move("dogebread", GetCoords("dogebread")[0]-1*dTime, GetCoords("dogebread")[1])  
            if l == True:
                Move("dogebread", GetCoords("dogebread")[0]+1*dTime, GetCoords("dogebread")[1])   
            if u == True:
                Move("dogebread", GetCoords("dogebread")[0], GetCoords("dogebread")[1]+1*dTime)
            if d == True:
                Move("dogebread", GetCoords("dogebread")[0], GetCoords("dogebread")[1]-1*dTime)
        else:
            if r == True:
                Move("dogebread", GetCoords("dogebread")[0]-0.25*dTime, GetCoords("dogebread")[1])  
            if l == True:
                Move("dogebread", GetCoords("dogebread")[0]+0.25*dTime, GetCoords("dogebread")[1])   
            if u == True:
                Move("dogebread", GetCoords("dogebread")[0], GetCoords("dogebread")[1]+0.25*dTime)
            if d == True:
                Move("dogebread", GetCoords("dogebread")[0], GetCoords("dogebread")[1]-0.25*dTime)