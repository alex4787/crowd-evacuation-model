import os
from gc import collect
import sys
import pygame
from random import *
from pygame.locals import *
from mvc import Collections, Controller
from statboard import StatBoard

from config import *

class View():
    def update_events(self, dt, paused):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return not paused
        return paused

    def draw(self, screen: pygame.Surface, collections: Collections, stats: StatBoard):
        screen.fill(BLACK)
        for row in collections.grid.tiles:
            for tile in row:
                pygame.draw.rect(screen, tile.tileColor(), tile)
                # uncomment below to see row/col numbers
                # screen.blit(
                #     pygame.font.Font('freesansbold.ttf', 16).render(
                #         f"{tile.y//FLOOR},{tile.x//FLOOR}",
                #         True,
                #         pygame.color.Color("deeppink")
                #     ),
                #     (tile.x, tile.y)
                # )
        for exit in collections.grid.exits:
            pygame.draw.rect(screen, exit.color, exit) 
        for person in collections.people:
            pygame.draw.rect(screen, person.color, person)

        screen.blit(stats.show(), (stats.x, stats.y))
        pygame.display.flip()

    
    def runPyGame(self, test: str = None, test_name: str = None, prop: float = 0.0, filename: str = None) -> None:
        pygame.init()

        fps = 60.0 if DISPLAY else 1000
        fpsClock = pygame.time.Clock()
        width, height = 1000, 1000

        screen = pygame.display.set_mode((width, height))

        collections = Collections(prop)
        stat_board = StatBoard(len(collections.people))
        controller = Controller(collections, width, height, stat_board)

        #Params for Capacity Tesing
        ticks_so_far = 0
        exit_count = len(collections.grid.exits)
        player_count = len(collections.people)
        paused = False


        dt = 1/fps

        while True:
        # Main game loop
            paused = self.update_events(dt, paused)

            while (not TEST_TYPE or stat_board.remaining_count > 0) and not paused:
                paused = self.update_events(dt, paused)
                if DISPLAY:
                    self.draw(screen, collections, stat_board)
                controller.update()
                dt = fpsClock.tick(fps)
                ticks_so_far+=1

                # if ticks_so_far == 1 and DISPLAY:
                #     paused = True

                # Every second
                if test == "graph_over_time" and (ticks_so_far % 60 == 0 or stat_board.remaining_count in [0, 1]):
                    f = open(filename, 'a')
                    crush_count = stat_board.crush_count_t1 + stat_board.crush_count_t2
                    burn_count = stat_board.burn_count_t1 + stat_board.burn_count_t2
                    escape_count = stat_board.escape_count_t1 + stat_board.escape_count_t2
                    f.write(f'{ticks_so_far} {crush_count} {burn_count} {escape_count}\n')
                    f.close()


            # Write data if test
            if test and not paused:
                if test == 'capacity':
                    f = open(filename, 'a')
                    f.write(f'{exit_count} {player_count} {ticks_so_far}\n')
                    f.close()
                if test == 'proportion':
                    f = open(filename, 'a')
                    f.write(f'{AGENT_SPEED_1} {AGENT_SPEED_2} {prop} {AGENT_COUNT} {stat_board.crush_count_t1} {stat_board.burn_count_t1} {stat_board.escape_count_t1} {stat_board.crush_count_t2} {stat_board.burn_count_t2} {stat_board.escape_count_t2}\n')
                    f.close()

                break
