class Plants:
    def __init__(self, type, color, size, daysToDoubling, x, y):
        self.type = type
        self.color = color
        self.size = size
        self.daysToDoubling = daysToDoubling
        self.doublingCycle = daysToDoubling
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.type} : {self.color} : {self.size} : {self.daysToDoubling} : ({self.x, self.y})"

    def grow(self):
        if self.daysToDoubling == 0:
            self.size += 1
            self.daysToDoubling = self.doublingCycle
        self.daysToDoubling -= 1
