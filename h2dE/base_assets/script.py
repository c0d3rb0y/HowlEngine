import time
import threading
from main import *
import v2ops


runThread = threading.Thread(target=init, args=(640, 360, (49,73,117), 60))
runThread.start()

time.sleep(1)
sprite(os.path.join(dirname, "base_assets/dog.png"), "dogobj", 10, 10)
text("Hi", "hiobj", 60, 50)
time.sleep(1)
rotate("hiobj", 90)
v2ops.move("hiobj", 80, 70, 1)
v2ops.move("dogobj", 30, 30, 1)
time.sleep(3)
changeOrder("dogobj", 2)
rotate("dogobj", -10)
sprite(os.path.join(dirname, "base_assets/test.bmp"), "testobj", 400, 300)
text("IM HERE NOW TOO HAHAHAHHAHAHAHAHHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHHAHAAHAHAHHAHAHAHAHHAHAHAHAHHA", "hahaobj", 320, 200)
remove("hiobj")
text("why tho", "bruhobj", 60, 50)
time.sleep(0.1)
move("testobj", 350, 250)
time.sleep(0.1)
move("testobj", 150, 150)
time.sleep(0.1)
move("testobj", 450, 350)
time.sleep(0.1)
move("testobj", 450, 150)
time.sleep(0.1)
move("testobj", 400, 300)
time.sleep(3)
remove("dogobj")
remove("bruhobj")
remove("testobj")
remove("hahaobj")
text("ok that was the engine test cool", "endtxt", 100, 180)
time.sleep(5)
remove("endtxt")
text("now u can move this doge across de scren", "end2txt", 100, 180)
sprite(os.path.join(dirname, "base_assets/dogebread.png"), "dogebread", 100, 160)
while GetRunning() == 1:
    if GetKeyDown(K_RIGHT):
        move("dogebread", getCoords("dogebread")[0]+0.001, getCoords("dogebread")[1])

    if GetKeyDown(K_LEFT):
        move("dogebread", getCoords("dogebread")[0]-0.001, getCoords("dogebread")[1])
    
    if GetKeyDown(K_UP):
        move("dogebread", getCoords("dogebread")[0], getCoords("dogebread")[1]-0.001)

    if GetKeyDown(K_DOWN):
        move("dogebread", getCoords("dogebread")[0], getCoords("dogebread")[1]+0.001)
stop()
