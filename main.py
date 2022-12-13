from mvc import View
from config import *

view = View()

if TEST_TYPE:
    for prop in AGENT_SPEED_1_PROPORTIONS:
        for i in range(TEST_ITERATIONS):
            view.runPyGame(TEST_TYPE, prop)
            print(f'{prop}, {i}\n')
else:
    view.runPyGame()
