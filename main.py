from mvc import View
from config import *
import os


def unique_filename(path: str) -> str:
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + "-" + str(counter) + extension
        counter += 1

    return path


view = View()

if TEST_TYPE:
    # Repeatedly run simulation over range of params for data collection
    filename = unique_filename(f"data/{TEST_NAME}.txt")
    print(filename)

    for prop in AGENT_SPEED_1_PROPORTIONS:
        for i in range(TEST_ITERATIONS):
            print(f'{prop}, {i}\n')
            view.runPyGame(TEST_TYPE, TEST_NAME, prop, filename)
else:
    # Run simulation as-is
    view.runPyGame()
