from enum import Enum
class State(Enum):
    FLY = 1.2
    CRAWL = 0.5

class Direction:
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

class Unit:
    def __init__(self, field):
        self.x = 0
        self.y = 0
        self.field = field
        self.speed = 1
        self.state = State

    def move(self, direction: Direction):

        if direction == Direction.UP:
            self.field.set_unit(y=self.y + self.speed, x=self.x, unit=self)
        elif direction == Direction.DOWN:
            self.field.set_unit(y=self.y-self.speed, x=self.x, unit=self)
        elif direction == Direction.LEFT:
            self.field.set_unit(y=self.y, x=self.x+self.speed, unit=self)
        elif direction == Direction.RIGHT:
            self.field.set_unit(y=self.y, x=self.x-self.speed, unit=self)


    def _get_speed(self):
        self.speed *= self.state.value
