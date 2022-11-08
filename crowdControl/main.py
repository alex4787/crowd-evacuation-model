import sys
import pygame
from random import *
from pygame.locals import *
from my_collections import Collections
from controller import Controller

def update_events(dt):
    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
def draw(screen, collections):
    screen.fill((0, 0, 0))
    for people in collections.people:
        pygame.draw.rect(screen, people.color, pygame.Rect(people.x, people.y, people.size, people.size))

    for exit in collections.exits:
        pygame.draw.rect(screen, exit.color, pygame.Rect(exit.x, exit.y, exit.size, exit.size)) 
    pygame.display.flip()

 
def runPyGame():
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
        update_events(dt)
        draw(screen, collections)
        controller.update()   
        dt = fpsClock.tick(fps)

#run the game
runPyGame()