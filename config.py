from enum import Enum

# TODO: Make this class-based for easier configuration

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
    if shape == "DoorAndU":
        return [(19, i) for i in range(20) if i not in [10]] + [(10, 11), (10, 14), (10,10), (11,10), (12,10), (13,10), (14, 10), (15, 10), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (15, 11), (15, 12), (15, 13), (15, 14)]
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
    if shape == 'concert':
        start_vals = [0, 14]
        return list(set((
                [(i, j) for i in range(7, 13) for j in range(7, 13)]
                + [(i, j) for x in start_vals for y in start_vals for i in range(x, x+6) for j in range(y, y+6)]
                + [(i, j) for x in start_vals for i in [8, 11] for j in range(x,x+6)]
        )))
    if shape == 'desks':
        def desk_clump(row, col):
            return [(row, col), (row + 1, col), (row + 1, col + 1), (row, col + 1)]
        return (
            [(9, 5), (10,5)]
            + desk_clump(9, 7)
            + desk_clump(9, 11)
            + desk_clump(9, 15)
            + desk_clump(6, 7)
            + desk_clump(6, 15)
            + desk_clump(12, 7)
            + desk_clump(12, 15)
        )

    if shape == 'u_hallway':
        return list(
            set(
                [(i, j) for j in range(3, 19) for i in [5, 14]]
                + [(i, 3) for i in range(5, 15)]
                + [(i, j) for j in range(5, 19) for i in [7, 12]]
                + [(i, 5) for i in range(7, 13)]
            )
        )
    if shape == 'classroom':
        return list(
            set(
                [(i, j) for j in range(3, 19) for i in [5, 14]]
                + [(i, j) for i in range(5, 15) for j in [3, 18]]
            )
            - {(14, 12)}
        )
    if shape == 'narrowing':
        # y, x
        return list(
            set(
                [(i, i // 2 + 10) for i in range(20)]
                + [(i, i // -2 + 10) for i in range(20)]
        )
        )
    if shape == 'Queue':
        return [(j, i) for i in range(20) for j in [17, 13] if i not in [18, 19]] + [(15, i) for i in range(20) if i not in [0, 1]] + [(18, 9)]
    if shape == '2Queues':
        return (
                [(j, 10) for j in range(13, 18)]
                + [(j, i) for i in range(11) for j in [17, 13] if i not in [0, 1]]
                + [(j, i) for i in range(11, 20) for j in [17, 13] if i not in [18, 19]]
                + [(15, i) for i in range(11) if i not in [8, 9]]
                + [(15, i) for i in range(11, 20) if i not in [11, 12]]
                #  + [(18, 9)]
        )  


def fire_pattern(shape):
    if shape == None:
        return []
    if shape == "Top3":
        return [(0, 19), (0, 0), (0, 10)]
    if shape == "TopCorners":
        return [(0, 19), (0, 0)]
    if shape == "Center":
        return [(10, 10)]
    if shape == "Bottom":
        return [(19, 10)]
    if shape == "classroom":
        return [(10, 12)]

def exit_pattern(shape):
    if shape == "BottomMiddle":
        return [(19, 10)]
    if shape == "2atBottom":
        return [(19, 5), (19, 15)]
    if shape == '4Doors':
        return [(19, 3), (19, 7), (19, 12), (19, 16)]
    if shape == '2Doors' or shape == '2DoorsEarlyChoke':
        return [(19, 5), (19, 14)]
    if shape == '4DoorsAround':
        return [(0, 5), (0, 15), (15, 0), (15, 19)]
    if shape == 'concert_sides':
        return [(9, 0), (10, 0), (9, 19), (10, 19)]
    if shape == 'classroom1door':
        return [(14 ,12)]
    if shape == 'u_hallway':
        return [(6, 18), (13, 18)]
    if shape == 'narrowing':
        return [(2, 10)]

def spawn_pattern(shape):
    if shape == "Random":
        return [(i, j) for i in range(20) for j in range(20)]
    if shape == "LeftThird":
        return (1000//3, 1000)
    if shape == "TopThird":
        return [(i, j) for i in range(20) for j in range(7)]
    if shape == "Concert":
        return list(set((
            [(i, j) for i in range(20) for j in range(20) if not (i in range(6, 14) and j in range(6, 14)) and not (j in range (8, 12))]
        )))
    if shape == 'classroom':
        def seats_for_desk_clump(row, col):
            return [(row, col-1), (row+1, col-1), (row, col+2), (row+1, col+2)]

        inverted = (
                [(9, 4)]
                + seats_for_desk_clump(9, 7)
                + seats_for_desk_clump(9, 11)
                + seats_for_desk_clump(9, 15)
                + seats_for_desk_clump(6, 7)
                + seats_for_desk_clump(6, 15)
                + seats_for_desk_clump(12, 7)
                + seats_for_desk_clump(12, 15)
        )

        print(inverted)
        final = [(b, a) for a, b in inverted]
        return final
    if shape == 'u_hallway':
        return [(4, j) for j in range(6, 14)]


# Test types
TESTS = {
    "concert_venue": {
        "tile_barriers": "concert",
        "tile_obstacles": None,
        "tile_exits": "concert_sides",
        "spawn_dimensions": "Concert",
        "tile_fires": "Bottom",
        "fire_spread_rate": 0.02,
        "test_type": "graph_over_time",
        "agent_speed_1_proportions": [0],
        "test_iterations": 1,
    },
    "classroom": {
        "tile_obstacles": "classroom",
        "tile_exits": "classroom1door",
        "tile_barriers": "desks",
        "test_type": "graph_over_time",
        "spawn_dimensions": "classroom",
        "one_agent_per_tile": True,
        "tile_fires": "classroom",
    },
    "u_hallway": {
        "tile_obstacles": "u_hallway",
        "spawn_dimensions": "u_hallway",
        "one_agent_per_tile": True,
        "tile_exits": "u_hallway",
    },
    "narrowing": {
        "tile_obstacles": "narrowing",
        "spawn_dimensions": "Random",
        "one_agent_per_tile": True,
        "tile_exits": "narrowing",
    },
    "fire3_randomdist_1door": {
        "tile_obstacles": "Door",
        "tile_exits": "BottomMiddle",
        "tile_fires": "Top3",
        "spawn_dimensions": "Random",
        "test_type": "proportion",
        "agent_speed_1_proportions": [0, 0.2, 0.4, 0.6, 0.8, 1],
        "test_iterations": 10,
        "agent_speed_1": 3,
        "agent_speed_2": 6,
        "time_on_exit": 10,
        "murder_modifier": 0.2,
    },
    "fire3_4skinnychoke_randomdist_1door": {
        "tile_obstacles": "DoorEarlyChoke",
        "tile_exits": "BottomMiddle",
        "tile_fires": "Top3",
        "spawn_dimensions": "Random",
        "test_type": "proportion",
        "agent_speed_1_proportions": [0, 0.2, 0.4, 0.6, 0.8, 1],
        "test_iterations": 10,
        "agent_speed_1": 3,
        "agent_speed_2": 6,
        "time_on_exit": 10,
        "murder_modifier": 0.2,
    },
    "fire3_randomdist_1door_with_u": {
        "tile_obstacles": "DoorAndU",
        "tile_exits": "BottomMiddle",
        "tile_fires": "Top3",
        "spawn_dimensions": "Random",
        "test_type": "proportion",
        "agent_speed_1_proportions": [0, 0.2, 0.4, 0.6, 0.8, 1],
        "test_iterations": 10,
        "agent_speed_1": 3,
        "agent_speed_2": 6,
        "time_on_exit": 10,
        "murder_modifier": 0.2,
    },

    "randomdist_1door_queue": {
        "tile_obstacles": "Door",
        "tile_exits": "BottomMiddle",
        # "tile_fires": "Top3",
        "tile_barriers": "Queue",
        "spawn_dimensions": "TopThird",
        "test_type": "proportion",
        "agent_speed_1_proportions": [0, 0.2, 0.4, 0.6, 0.8, 1],
        "test_iterations": 10,
        "agent_speed_1": 3,
        "agent_speed_2": 6,
        "time_on_exit": 10,
        "murder_modifier": 0.01,
    },
    "randomdist_1door_2queues": {
        "tile_obstacles": "Door",
        "tile_exits": "BottomMiddle",
        # "tile_fires": "Top3",
        "tile_barriers": "2Queues",
        "spawn_dimensions": "TopThird",
        "test_type": "proportion",
        "agent_speed_1_proportions": [0, 0.2, 0.4, 0.6, 0.8, 1],
        "test_iterations": 10,
        "agent_speed_1": 3,
        "agent_speed_2": 6,
        "time_on_exit": 10,
        "murder_modifier": 0.01,
    },
}

TEST_NAME = "fire3_4skinnychoke_randomdist_1door"  # 'fire3_4skinnychoke_randomdist_1door' #None #fire3_nochoke_randomdist_2door #None #'fire3_randomdist_1door' #'4choke' #'4chokenochokedist' # '3chokefat' #'4chokenochoke' #'4choke' #None #'4doors' #None #'door-block' #None #'door' #None#'middlefire' #None #'prop-2exit' #None #'proportion' #None #'capacity'
TEST = TESTS[TEST_NAME]
DISPLAY = True

# Constants #####################################################

PANIC = TEST.get("panic", 0.3)
MAX_DENSITY = TEST.get("max_density", 5)
FIRE_SPREAD_RATE = TEST.get("fire_spread_rate", 0.007)
AGENT_COUNT = TEST.get("agent_count", 300)
ONE_AGENT_PER_TILE = TEST.get("one_agent_per_tile", False)
AGENT_SPEED_1 = TEST.get("agent_speed_1", 3)
AGENT_SPEED_2 = TEST.get("agent_speed_2", 4)
TIME_ON_EXIT = TEST.get("time_on_exit", 5)
MURDER_MODIFIER = TEST.get("murder_modifier", 0.01)

BLACK = TEST.get("black", (0, 0, 0))
RED = TEST.get("red", (255, 0, 0))
FLOOR = TEST.get("floor", 50)

BLUE_MAN_HEAT_DROP = TEST.get("blue_man_heat_drop", 50)
PINK_MAN_HEAT_DROP = TEST.get("pink_man_heat_drop", 0)

AGENT_SPEED_1_PROPORTIONS = TEST.get("agent_speed_1_proportions", [0])
TEST_ITERATIONS = TEST.get("test_iterations", 1)
TEST_TYPE = TEST.get("test_type", 'graph_over_time')  # 'fire3_4skinnychoke_randomdist_1door' #None #fire3_nochoke_randomdist_2door #None #'fire3_randomdist_1door' #'4choke' #'4chokenochokedist' # '3chokefat' #'4chokenochoke' #'4choke' #None #'4doors' #None #'door-block' #None #'door' #None#'middlefire' #None #'prop-2exit' #None #'proportion' #None #'capacity'

SPAWN_DIMENSIONS = spawn_pattern(TEST.get("spawn_dimensions", "TopThird"))
TILE_OBSTACLES = obstacle_pattern(TEST.get("tile_obstacles", 'U'))
TILE_EXITS = exit_pattern(TEST.get("tile_exits", "2atBottom"))
TILE_FIRES = fire_pattern(TEST.get("tile_fires", None))
TILE_BARRIERS = obstacle_pattern(TEST.get("tile_barriers", None))
