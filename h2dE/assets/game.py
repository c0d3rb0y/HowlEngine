from main import *
from v2ops import *
import random

runT = threading.Thread(target=Init, args=(1280, 720, (176,223,229), 60))
runT.start()

while GetRunning() == False:
    time.sleep(0)

while GetRunning() == True:
    Text("MONKE CLICKER", "title", 0, 0)
    Text("A game where you click the monke, if click the monke 50 times u wins", "description", 0, 37)
    Text("Click anywhere to start", "inst", 0, 72)

    lmb = GetLMBDown()
    while GetLMBDown() == False:
        lmb = GetLMBDown()


    Remove("title")
    Remove("description")
    Remove("inst")
    score = 0
    Text("click the monke", "monketxt", 0, 0)
    Text("Score: " + str(score), "scor", 0, 37)
    Sprite(os.path.join(dirname, "assets/monke.png"), "monke", 640, 100)
    while score < 50:
        if GetLMBDown() and GetTouchingMouse("monke"):
            score += 1
            Remove("scor")
            Text("Score: " + str(score), "scor", 0, 37)
            MoveT("monke", random.randrange(0, 1080), random.randrange(0, 520), 0.1)
            while GetLMBDown():
                time.sleep(0)

    Remove("monke")
    Remove("scor")
    Remove("monketxt")
    Text("You winned. Up good", "a", 0, 0)
    Text("Click to play again", "b", 0, 40)
    while GetLMBDown() == False:
        time.sleep(0)
    Remove("a")
    Remove("b")