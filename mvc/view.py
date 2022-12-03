from gc import collect
import sys
import pygame
from random import *
from pygame.locals import *
from mvc import Collections, Controller
from statboard import StatBoard

class View():
    def update_events(self, dt):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
    def draw(self, screen: pygame.Surface, collections: Collections, stats: StatBoard):
        screen.fill((0, 0, 0))
        for row in collections.grid.tiles:
            for tile in row:
                pygame.draw.rect(screen, tile.tileColor(), tile)
                # screen.blit(pygame.font.Font('freesansbold.ttf', 16).render(",".join(map(str, tile.exit_distance_map.values())), True, pygame.color.Color("deeppink")), (tile.x, tile.y))
        for exit in collections.exits:
            pygame.draw.rect(screen, exit.color, exit) 
        for person in collections.people:
            pygame.draw.rect(screen, person.color, person)

        screen.blit(stats.show(), (stats.x, stats.y))
        pygame.display.flip()

    
    def runPyGame(self, agent_count: int, floor: int) -> None:
        pygame.init()

        fps = 60.0
        fpsClock = pygame.time.Clock()
        width, height = 1000, 1000

        screen = pygame.display.set_mode((width, height))

        stat_board = StatBoard(agent_count)
        collections = Collections(width, height, floor, agent_count)
        controller = Controller(collections, width, height, stat_board)
        
        dt = 1/fps
        while True:
            self.update_events(dt)
            self.draw(screen, collections, stat_board)
            controller.update()   
            dt = fpsClock.tick(fps)
