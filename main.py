from mvc import View
from config import *

view = View()

if TEST_TYPE:
    for i in range(TEST_ITERATIONS):
        view.runPyGame(TEST_TYPE)
else:
    view.runPyGame()
