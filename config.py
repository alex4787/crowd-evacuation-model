def obstacle_pattern(shape):
    if shape == None:
        return []
    if shape == "U":
        return [(10, 11), (10, 14), (10,10), (11,10), (12,10), (13,10), (14, 10), (15, 10), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (15, 11), (15, 12), (15, 13), (15, 14)]
    if shape == "Square":
        return [(x,y) for x in range(1,5) for y in range(1,5)]
    if shape == "Bucket":
        return [
    (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7),
    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
    (7, 0), (7, 1), (7, 2), (7, 3), (7, 7), (7, 5), (7, 6), (7, 7),
    (10,10), (11,10), (12,10), (13,10), (14, 10), (15, 10),
    ]
    if shape == "Door":
        return [(19, 9), (19, 11)]

def fire_pattern(shape):
    if shape == None:
        return []
    if shape == "Top3":
        return [(0, 19), (0, 0), (0, 10)]
    if shape == "TopCorners":
        return [(0, 19), (0, 0)]
    if shape == "Center":
        return [(10, 10)]

def exit_pattern(shape):
    if shape == "BottomMiddle":
        return [(19, 10)]

def spawn_pattern(shape):
    if shape == "Random":
        return (1000, 1000)
    if shape == "LeftThird":
        return (1000//3, 1000)
    if shape == "TopThird":
        return (1000, 1000//3)



# Constants #####################################################

MAX_DENSITY = 5
FIRE_SPREAD_RATE = 0.01
AGENT_COUNT = 300
AGENT_SPEED_1 = 3
AGENT_SPEED_2 = 6
AGENT_SPEED_1_PROPORTIONS = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]
TIME_ON_EXIT = 10
SPAWN_DIMENSIONS = spawn_pattern("Random")

MURDER_MODIFIER = 0.05

BLACK = (0, 0, 0)
RED = (255, 0, 0)
FLOOR = 50

BLUE_MAN_HEAT_DROP = 50
PINK_MAN_HEAT_DROP = 0

TEST_ITERATIONS = 5
TEST_PROPORTION = 0
TEST_TYPE = None #'proportion' #None #'capacity'


TILE_OBSTACLES = obstacle_pattern(None)
TILE_EXITS = exit_pattern("BottomMiddle")
TILE_FIRES = fire_pattern("Top3")