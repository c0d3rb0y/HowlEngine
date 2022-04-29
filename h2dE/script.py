from main import *
from v2ops import *

Init(1280, 720, (49, 73, 117), 60)
while GetRunning() == False:
    time.sleep(0)
endscene = Scene("endscene", [
    ReturnText("now u can move this doge across de scren (arrow keys), except no touch smiley face", "end2txt", 100,
               180, (0, 30, 0)),
    ReturnSprite(os.path.join(dirname, "base_assets/test.bmp"), "randomthingy", 400, 300),
    ReturnSprite(os.path.join(dirname, "base_assets/dogebread.png"), "dogebread", 100, 160),
    ])
textbeforeend = Scene("textbeforeend",
                      [ReturnText("ok that was the engine test cool", "endtxt", 100, 180, (10, 10, 10))])
state = GameState("auto", ["auto", "interactive"])
SetTitle("h2dE demo - " + state.getCurrent())
Sprite(os.path.join(dirname, "base_assets/dog.png"), "dogobj", 10, 10)
Text("Hi", "hiobj", 60, 50, (10, 10, 10))
time.sleep(1)
particles.ParticleSystem("ps", 100, os.path.join(dirname, "base_assets/test.bmp"), 640, 360, 10, 5)
Rotate("hiobj", 90)
MoveT("hiobj", 80, 70, 1)
MoveT("dogobj", 30, 30, 1)
time.sleep(3)
ChangeOrder("dogobj", 2)
Rotate("dogobj", -10)
Sprite(os.path.join(dirname, "base_assets/test.bmp"), "testobj", 400, 300)
Text("IM HERE NOW TOO HAHAHAHHAHAHAHAHHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHHAHAAHAHAHHAHAHAHAHHAHAHAHAHHA", "hahaobj", 320,
     200, (10, 10, 10))
Remove("hiobj")
Text("why tho", "bruhobj", 60, 50, (10, 10, 10))
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
textbeforeend.load()
time.sleep(5)
if GetKeyDown(K_d):
    SetVolume(0.0)
    # debug flag
endscene.load()
MakeObjectLightInfluenced("dogebread", 0)
MakeObjectLightInfluenced("end2txt", 0)
MakeObjectLight("randomthingy", 100)
txtch = False
i = 0
state.setCurrent("interactive")
SetTitle("h2dE demo - " + state.getCurrent())
while GetRunning() == 1:
    r = False
    l = False
    u = False
    d = False
    dbc = GetCoords("dogebread")
    dTime = deltaTime()

    if GetLMBDown():
        Move("randomthingy", GetMousePosition()[0], GetMousePosition()[1])

    if GetRMBDown():
        Move("randomthingy", 400, 300)

    if GetKeyDown(K_RIGHT) and (dbc[0] <= 1180):
        r = True
        Move("dogebread", dbc[0] + 0.25 * dTime, dbc[1])

    if GetKeyDown(K_LEFT) and (dbc[0] >= 0):
        l = True
        Move("dogebread", dbc[0] - 0.25 * dTime, dbc[1])

    if GetKeyDown(K_UP) and (dbc[1] >= 000):
        u = True
        Move("dogebread", dbc[0], dbc[1] - 0.25 * dTime)

    if GetKeyDown(K_DOWN) and (dbc[1] <= 620):
        d = True
        Move("dogebread", dbc[0], dbc[1] + 0.25 * dTime)

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
        SetAmbient(GetAmbient() - 10)
        while GetKeyDown(K_2):
            time.sleep(0)
    if GetKeyDown(K_3) and GetAmbient() < 240:
        SetAmbient(GetAmbient() + 10)
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
                Move("dogebread", dbc[0] - 1 * dTime, dbc[1])
            if l == True:
                Move("dogebread", dbc[0] + 1 * dTime, dbc[1])
            if u == True:
                Move("dogebread", dbc[0], dbc[1] + 1 * dTime)
            if d == True:
                Move("dogebread", dbc[0], dbc[1] - 1 * dTime)
        else:
            if r == True:
                Move("dogebread", dbc[0] - 0.25 * dTime, dbc[1])
            if l == True:
                Move("dogebread", dbc[0] + 0.25 * dTime, dbc[1])
            if u == True:
                Move("dogebread", dbc[0], dbc[1] + 0.25 * dTime)
            if d == True:
                Move("dogebread", dbc[0], dbc[1] - 0.25 * dTime)