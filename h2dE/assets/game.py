from main import *

runT = threading.Thread(target=Init, args=(1280, 720, (176,223,229), 60))
runT.start()

while GetRunning() == False:
    time.sleep(0)

Text("MONKE CLICKER", "title", 0, 0)
Text("A game where you click the monke, if u get 100 u wins", "description", 0, 37)
Text("Click anywhere to start", "inst", 0, 72)

lmb = GetLMBDown()
while GetLMBDown() == False:
    lmb = GetLMBDown()

Remove("title")
Remove("description")
Remove("inst")
score = 0
Text("('_') <- monke (because i didnt wanna download image)", "monke", 0, 0)
Text("Score: " + str(score), "scor", 0, 37)
while score < 100:
    if GetLMBDown():
        score += 1
        Remove("scor")
        Text("Score: " + str(score), "scor", 0, 37)
        while GetLMBDown():
            time.sleep(0)

Remove("monke")
Remove("scor")
Text("You winned. Up good", "a", 0, 0)