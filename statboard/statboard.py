import pygame

class StatBoard:
    def __init__(self, agent_count: int):
        self.x = 10
        self.y = 10
        self.escape_count_t1 = 0
        self.burn_count_t1 = 0
        self.crush_count_t1 = 0
        self.escape_count_t2 = 0
        self.burn_count_t2 = 0
        self.crush_count_t2 = 0
        self.remaining_count = agent_count
        self.color = (255, 255, 255)
        self.font = pygame.font.Font('freesansbold.ttf', 20)

    def show(self):
        return self.font.render(f'T1 Escape: {self.escape_count_t1}, T1 Crush: {self.crush_count_t1}, T1 Burn: {self.burn_count_t1} T2 Escape: {self.escape_count_t2}, T2 Crush: {self.crush_count_t2}, T2 Burn: {self.burn_count_t2}, Remaining: {self.remaining_count}',
        True, self.color)
