from main import *
from v2ops import *

runT = threading.Thread(target=Init, args=(1280, 720, (49,73,117), 60))
runT.start()


Sprite(os.path.join(dirname, "base_assets/dog.png"), "dogobj", 10, 10)
Text("Hi", "hiobj", 60, 50)
time.sleep(1)
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
Remove("endtxt")
Text("now u can Move this doge across de scren", "end2txt", 100, 180)
Text("not touching random thingy", "end3txt", 100, 220)
Sprite(os.path.join(dirname, "base_assets/test.bmp"), "randomthingy", 400, 300)
Sprite(os.path.join(dirname, "base_assets/dogebread.png"), "dogebread", 100, 160)
txtch = False
PlayAudio(os.path.join(dirname, "base_assets/sigmamale.mp3"))
while GetRunning() == 1:
    col = GetCollision("dogebread", "randomthingy")
    if col and txtch == False:
        Remove("end3txt")
        txtch = True
    else:
        if txtch and col == False:
            Text("not touching random thingy", "end3txt", 100, 220)
            txtch = False
    if GetKeyDown(K_RIGHT):
        Move("dogebread", GetCoords("dogebread")[0]+0.005, GetCoords("dogebread")[1])
    if GetKeyDown(K_LEFT):
        Move("dogebread", GetCoords("dogebread")[0]-0.005, GetCoords("dogebread")[1])        
    if GetKeyDown(K_UP):
        Move("dogebread", GetCoords("dogebread")[0], GetCoords("dogebread")[1]-0.005)

    if GetKeyDown(K_DOWN):
        Move("dogebread", GetCoords("dogebread")[0], GetCoords("dogebread")[1]+0.005)