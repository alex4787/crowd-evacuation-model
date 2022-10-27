class Prey:
    def __init__(self, type, color, size, current_energy_level, spawning_time, x, y):
        self.type = type
        self.color = color
        self.size = size
        self.current_energy_level = current_energy_level
        self.spawning_time = spawning_time
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.type} : {self.color} : {self.size} : {self.current_energy_level} : {self.spawning_time} : ({self.x, self.y})"

    def grow(self):
        if self.spawning_time == 0:
            self.reprocreate()
        elif self.current_energy_level == 0:
            self.die()

        self.current_energy_level -= 1
        self.spawning_time -= 1

    # def reprocreate():

    # def die():