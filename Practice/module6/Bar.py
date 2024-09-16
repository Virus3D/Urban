import arcade
from constant import *

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('Practice/module6/bar.png', 0.2)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH
        if self.right <= 0:
            self.center_x = 0
