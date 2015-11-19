import sys
sys.path.append('../LabsAll/Labs')
from pico2d import *

import game_framework

running = None



class Isaac:

    PIXEL_PER_METER = (50.0 / 1.0)      # 50 pixel 1 meter
    RUN_SPEED_MPS = 1.0
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    head = None
    body = None

    LEFT_RUN, RIGHT_RUN, UP_RUN, DOWN_RUN, LEFT_STAND, RIGHT_STAND, UP_STAND, DOWN_STAND = 0, 1, 2, 3, 4, 5, 6, 7
    def __init__(self):
        self.x, self.y = 480, 270
        self.total_frames = 0.0
        self.left_run_frame, self.right_run_frame, self.up_run_frame, self.down_run_frame
        self.state = DOWN_STAND
        if body == None:
            Isaac.body = load_image('resources\graghpics\resources\gfx\characters\costumes\costume_000_basicbody.png')
        if head == None:
            Isaac.Isaac = load_image('resources\graghpics\resources\gfx\characters\costumes\heads.png')

    def update(self, frame_time):
        distance = Isaac.RUN_SPEED_PPS * frame_time
        self.total_frames += 1.0
        self.frame = (self.frame + 1) % 10

    def draw(self):
        if self.state == LEFT_RUN:
            self.body.clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y, 50, 50)
            pass
        elif self.state == RIGHT_RUN:
            self.body.clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y, 50, 50)
            pass
        elif self.state == UP_RUN:
            pass
        elif self.state == DOWN_RUN:
            pass
        elif self.state == LEFT_STAND:
            pass
        elif self.state == RIGHT_STAND:
            pass
        elif self.state == UP_STAND:
            pass
        elif self.state == DOWN_STAND:
            pass
def handle_events():
    global running, time_start
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            pass