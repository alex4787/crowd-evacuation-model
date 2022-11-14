import pygame

class StatBoard:
    def __init__(self, agent_count: int):
        self.x = 300
        self.y = 100
        self.escape_count = 0
        self.death_count = 0
        self.remaining_count = agent_count
        self.color = (150, 150, 150)
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def show(self):
        return self.font.render(f'{self.escape_count} Escaped, {self.death_count} Dead, {self.remaining_count} TBD', True, self.color)
