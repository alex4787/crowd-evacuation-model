from gc import collect
import sys
import pygame
from random import *
from pygame.locals import *
from mvc import Collections, Controller
from statboard import StatBoard

from config import *

class View():
    def update_events(self, dt):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
    def draw(self, screen: pygame.Surface, collections: Collections, stats: StatBoard):
        screen.fill(BLACK)
        for row in collections.grid.tiles:
            for tile in row:
                pygame.draw.rect(screen, tile.tileColor(), tile)
                #screen.blit(pygame.font.Font('freesansbold.ttf', 16).render(",".join(map(str, tile.exit_distance_map.values())), True, pygame.color.Color("deeppink")), (tile.x, tile.y))
        for exit in collections.grid.exits:
            pygame.draw.rect(screen, exit.color, exit) 
        for person in collections.people:
            pygame.draw.rect(screen, person.color, person)

        screen.blit(stats.show(), (stats.x, stats.y))
        pygame.display.flip()

    
    def runPyGame(self, test: str = None, prop: float = 0.0) -> None:
        pygame.init()

        fps = 60.0
        fpsClock = pygame.time.Clock()
        width, height = 1000, 1000

        screen = pygame.display.set_mode((width, height))

        stat_board = StatBoard(AGENT_COUNT)
        collections = Collections(prop)
        controller = Controller(collections, width, height, stat_board)

        #Params for Capacity Tesing
        ticks_so_far = 0
        exit_count = len(collections.grid.exits)
        player_count = len(collections.people)


        dt = 1/fps
        while not TEST_TYPE or stat_board.remaining_count > 0: ## just to trigger tests
            self.update_events(dt)
            self.draw(screen, collections, stat_board)
            controller.update()   
            dt = fpsClock.tick(fps)
            ticks_so_far+=1

        if test:
            if test == 'capacity':
                f = open("data/capacity-real.txt", 'a')
                f.write(f'{exit_count} {player_count} {ticks_so_far}\n')
                f.close()
            if test == 'proportion':
                f = open("data/speed-proportion-real.txt", 'a')
                f.write(f'{AGENT_SPEED_1} {AGENT_SPEED_2} {prop} {AGENT_COUNT} {stat_board.crush_count_t1} {stat_board.burn_count_t1} {stat_board.escape_count_t1} {stat_board.crush_count_t2} {stat_board.burn_count_t2} {stat_board.escape_count_t2}\n')
                f.close()
            if test == 'prop-2exit':
                f = open("data/speed-prop-2exit-real.txt", 'a')
                f.write(f'{AGENT_SPEED_1} {AGENT_SPEED_2} {prop} {AGENT_COUNT} {stat_board.crush_count_t1} {stat_board.burn_count_t1} {stat_board.escape_count_t1} {stat_board.crush_count_t2} {stat_board.burn_count_t2} {stat_board.escape_count_t2}\n')
                f.close()
            if test == 'middlefire':
                f = open("data/middlefire-real.txt", 'a')
                f.write(f'{AGENT_SPEED_1} {AGENT_SPEED_2} {prop} {AGENT_COUNT} {stat_board.crush_count_t1} {stat_board.burn_count_t1} {stat_board.escape_count_t1} {stat_board.crush_count_t2} {stat_board.burn_count_t2} {stat_board.escape_count_t2}\n')
                f.close()
            if test == 'door':
                f = open("data/door-real.txt", 'a')
                f.write(f'{AGENT_SPEED_1} {AGENT_SPEED_2} {prop} {AGENT_COUNT} {stat_board.crush_count_t1} {stat_board.burn_count_t1} {stat_board.escape_count_t1} {stat_board.crush_count_t2} {stat_board.burn_count_t2} {stat_board.escape_count_t2}\n')
                f.close()
            if test == 'door-block':
                f = open("data/door-block-real.txt", 'a')
                f.write(f'{AGENT_SPEED_1} {AGENT_SPEED_2} {prop} {AGENT_COUNT} {stat_board.crush_count_t1} {stat_board.burn_count_t1} {stat_board.escape_count_t1} {stat_board.crush_count_t2} {stat_board.burn_count_t2} {stat_board.escape_count_t2}\n')
                f.close()
            if test == '4doors':
                f = open("data/4Doors-real.txt", 'a')
                f.write(f'{AGENT_SPEED_1} {AGENT_SPEED_2} {prop} {AGENT_COUNT} {stat_board.crush_count_t1} {stat_board.burn_count_t1} {stat_board.escape_count_t1} {stat_board.crush_count_t2} {stat_board.burn_count_t2} {stat_board.escape_count_t2}\n')
                f.close()
            if test == '4choke':
                f = open("data/4choke-real.txt", 'a')
                f.write(f'{AGENT_SPEED_1} {AGENT_SPEED_2} {prop} {AGENT_COUNT} {stat_board.crush_count_t1} {stat_board.burn_count_t1} {stat_board.escape_count_t1} {stat_board.crush_count_t2} {stat_board.burn_count_t2} {stat_board.escape_count_t2}\n')
                f.close()
            if test == '4chokenochoke':
                f = open("data/4choke-nochoke-real.txt", 'a')
                f.write(f'{AGENT_SPEED_1} {AGENT_SPEED_2} {prop} {AGENT_COUNT} {stat_board.crush_count_t1} {stat_board.burn_count_t1} {stat_board.escape_count_t1} {stat_board.crush_count_t2} {stat_board.burn_count_t2} {stat_board.escape_count_t2}\n')
                f.close()
            if test == '3chokefat':
                f = open("data/3choke-fat.txt", 'a')
                f.write(f'{AGENT_SPEED_1} {AGENT_SPEED_2} {prop} {AGENT_COUNT} {stat_board.crush_count_t1} {stat_board.burn_count_t1} {stat_board.escape_count_t1} {stat_board.crush_count_t2} {stat_board.burn_count_t2} {stat_board.escape_count_t2}\n')
                f.close()
            if test == '4chokenochokedist':
                f = open("data/4choke-nochoke-dist-real.txt", 'a')
                f.write(f'{AGENT_SPEED_1} {AGENT_SPEED_2} {prop} {AGENT_COUNT} {stat_board.crush_count_t1} {stat_board.burn_count_t1} {stat_board.escape_count_t1} {stat_board.crush_count_t2} {stat_board.burn_count_t2} {stat_board.escape_count_t2}\n')
                f.close()


