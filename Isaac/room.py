from pico2d import *

class Room:
    def __init__(self):
        Room.ROOM_CAVE1 = load_image('cave1.png')

    def draw(self):
        self.ROOM_CAVE1.clip_draw(0, 0, 850, 550, 480, 275)
