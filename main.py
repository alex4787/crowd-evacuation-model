import sys
import pygame
from random import *
from pygame.locals import *
from game_objects.boardstate import BoardState


 
def update(dt):
    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() # Opposite of pygame.init
            sys.exit()
    
def draw(screen, boardstate):
    screen.fill((0, 0, 0)) # Fill the screen with black.
    for plant in boardstate.plants:
        pygame.draw.rect(screen, plant.color, pygame.Rect(plant.x, plant.y, plant.size, plant.size))
    for prey in boardstate.preys:
        pygame.draw.rect(screen, prey.color, pygame.Rect(prey.x, prey.y, prey.size, prey.size))
    pygame.display.flip()

 
def runPyGame():
    pygame.init()

    fps = 60.0
    fpsClock = pygame.time.Clock()
  
    # Set up the window.
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    #put in static stuff
    boardState = BoardState(width, height)
    
    # Main game loop.
    dt = 1/fps # dt is the time since last frame.
    while True: # Loop forever!
        update(dt) # You can update/draw here, I've just moved the code for neatness.
        draw(screen, boardState)
        boardState.update()
        
        dt = fpsClock.tick(fps)

#---------------------------------------SETUP STUFF------------------------------#

#run the game
runPyGame()