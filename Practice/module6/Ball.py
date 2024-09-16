import arcade
from constant import *

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('Practice/module6/ball.png', 0.05)
        self.change_x = 0.5
        self.change_y = 0.5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH or self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT or self.bottom <= 0:
            self.change_y = -self.change_y

