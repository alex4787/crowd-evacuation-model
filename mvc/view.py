from gc import collect
import sys
import pygame
from random import *
from pygame.locals import *
from mvc import Collections, Controller

class View():
    def update_events(self, dt):
        # Go through events that are passed to the script by the window.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
    def draw(self, screen, collections: Collections):
        screen.fill((0, 0, 0))
        for fire in collections.fires:
            pygame.draw.rect(screen, fire.color, fire)
        for exit in collections.exits:
            pygame.draw.rect(screen, exit.color, exit) 
        for person in collections.people:
            pygame.draw.rect(screen, person.color, person)

        pygame.display.flip()

    
    def runPyGame(self):
        pygame.init()

        fps = 60.0
        fpsClock = pygame.time.Clock()
    
        # Set up the window.
        width, height = 1000, 1000
        screen = pygame.display.set_mode((width, height))

        #put in static stuff
        collections = Collections(width, height)
        controller = Controller(collections, width, height)
        
        # Main game loop.
        dt = 1/fps # dt is the time since last frame.
        while True:
            self.update_events(dt)
            self.draw(screen, collections)
            controller.update()   
            dt = fpsClock.tick(fps)
