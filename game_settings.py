class GameSettings:

    def __init__(self):
        self.speed = 0.4

    def increase_speed(self):
        self.speed -= 0.02
