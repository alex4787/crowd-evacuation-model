def obstacle_pattern(shape):
    if shape == None:
        return []
    if shape == "U":
        return [(10, 11), (10, 14), (10,10), (11,10), (12,10), (13,10), (14, 10), (15, 10), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (15, 11), (15, 12), (15, 13), (15, 14)]
    if shape == "Square":
        return [(x+12,y+8) for x in range(1,6) for y in range(1,4)]
    if shape == "Bucket":
        return [
    (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7),
    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
    (7, 0), (7, 1), (7, 2), (7, 3), (7, 7), (7, 5), (7, 6), (7, 7),
    (10,10), (11,10), (12,10), (13,10), (14, 10), (15, 10),
    ]
    if shape == "Door":
        return [(19, i) for i in range(20) if i not in [10]] 
    if shape == "DoorEarlyChoke":
        return [(19, i) for i in range(20) if i not in [10]] + [(10, i) for i in range(20) if i not in [3, 7, 12, 16]]
    if shape == '4Doors':
        return [(19, 2), (19, 4), (19, 6), (19, 8), (19, 11), (19, 13), (19, 15), (19, 17)]
    if shape == '2Doors':
        return [(19, i) for i in range(20) if i not in [5, 14]]
    if shape == '2DoorsEarlyChoke':
        return [(19, i) for i in range(20) if i not in [5, 14]] + [(10, i) for i in range(20) if i not in [3, 7, 12, 16]]
    if shape == '2DoorsEarlyChokeFat':
        return [(19, i) for i in range(20) if i not in [5, 14]] + [(10, i) for i in range(20) if i not in [4, 3, 9, 10, 16, 15]]

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
    if shape == "2atBottom":
        return [(19, 5), (19, 15)]
    if shape == '4Doors':
        return [(19, 3), (19, 7), (19, 12), (19, 16)]
    if shape == '2Doors' or shape == '2DoorsEarlyChoke':
        return [(19, 5), (19, 14)]

def spawn_pattern(shape):
    if shape == "Random":
        return (1000, 1000)
    if shape == "LeftThird":
        return (1000//3, 1000)
    if shape == "TopThird":
        return (1000, 1000//3)



# Constants #####################################################

PANIC = 0.3
MAX_DENSITY = 5
FIRE_SPREAD_RATE = 0.007
AGENT_COUNT = 1
AGENT_SPEED_1 = 3
AGENT_SPEED_2 = 4
TIME_ON_EXIT = 10
MURDER_MODIFIER = 0.2

BLACK = (0, 0, 0)
RED = (255, 0, 0)
FLOOR = 50

BLUE_MAN_HEAT_DROP = 50
PINK_MAN_HEAT_DROP = 0

AGENT_SPEED_1_PROPORTIONS = [0, .2, .4, .6, .8, 1]
TEST_ITERATIONS = 8
TEST_TYPE = None #'fire3_4skinnychoke_randomdist_1door' #None #fire3_nochoke_randomdist_2door #None #'fire3_randomdist_1door' #'4choke' #'4chokenochokedist' # '3chokefat' #'4chokenochoke' #'4choke' #None #'4doors' #None #'door-block' #None #'door' #None#'middlefire' #None #'prop-2exit' #None #'proportion' #None #'capacity'

SPAWN_DIMENSIONS = spawn_pattern("Random")
TILE_OBSTACLES = obstacle_pattern('DoorEarlyChoke') #+ obstacle_pattern('U')
TILE_EXITS = exit_pattern("BottomMiddle")
TILE_FIRES = fire_pattern("Top3")
