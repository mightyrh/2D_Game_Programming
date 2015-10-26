import sys
sys.path.append('../LabsAll/Labs')
from pico2d import *

import game_framework
import time
# game object class here
running = None
time_start, time_end = 0,0
class Map:
    def __init__(self):
        Map.MAP_CAVE1 = load_image('cave1.png')

    def draw(self):
        self.MAP_CAVE1.clip_draw(0, 0, 800, 600, 400, 300)

class Tear:
class Isaac:

    LEFT_RUN, RIGHT_RUN, UP_RUN, DOWN_RUN, LEFT_STAND, RIGHT_STAND, UP_STAND, DOWN_STAND = 0, 1, 2, 3, 4, 5, 6, 7

    def handle_left_run(self):
        self.Lframe = (self.Lframe + 1) % 10
        if self.x > 100:
            self.x -= 8

    def handle_right_run(self):
        self.Rframe = (self.Rframe + 1) % 10
        if self.x < 800 - 100:
            self.x += 8

    def handle_up_run(self):
        self.Uframe = (self.Uframe + 1) % 10
        if self.y < 600 - 100:
            self.y += 8

    def handle_down_run(self):
        self.Dframe = (self.Dframe + 1) % 10
        if self.y > 130:
            self.y -= 8

    def handle_stand(self):

        pass

    handle_state = {
                    LEFT_RUN: handle_left_run,
                    RIGHT_RUN: handle_right_run,
                    UP_RUN: handle_up_run,
                    DOWN_RUN: handle_down_run,
                    LEFT_STAND: handle_stand,
                    RIGHT_STAND: handle_stand,
                    UP_STAND: handle_stand,
                    DOWN_STAND: handle_stand
}

    def fire_tear(self):
        global time_start, time_end
        if isaac.fireDir == 1:
            time_end = time.time()
            if (time_end - time_start) % 1000 == 0:
                isaac.fire = True
        elif isaac.fireDir == 2:
            time_end = time.time()
            if (time_end - time_start) % 1000 == 0:
                isaac.fire = True
        elif isaac.fireDir == 3:
            time_end = time.time()
            if (time_end - time_start) % 1000 == 0:
                isaac.fire = True
        elif isaac.fireDir == 4:
            time_end = time.time()
            if (time_end - time_start) % 1000 == 0:
                isaac.fire = True

    def updateS(self):
        self.handle_state[self.state](self)
        pass

    def __init__(self):
        self.x, self.y = 400,400
        self.Lframe, self.Rframe, self.Uframe, self.Dframe = 0,0,0,0
        self.state = self.DOWN_STAND    # 이동 state 이동방향이 어딘지 알려줌
        self.fire = False
        self.fireDir = 0           # 눈물 방향 0 = 발사 x
        self.fire_rate = 1000      # 공속 1초에 한번 발사

        Isaac.S_image = load_image('character_001_isaac.png')
        Isaac.H_image = load_image('heads.png')
        Isaac.L_image = load_image('left_move.png')
        Isaac.R_image = load_image('right_move.png')
        Isaac.UD_image = load_image('front_move.png')


    def draw(self):

        if self.state == self.RIGHT_RUN:
            self.R_image.clip_draw(self.Rframe * 50, 0, 50, 50, self.x, self.y - 15)
            self.H_image.clip_draw(50 * 2, 0, 50, 50, self.x, self.y)
        elif self.state == self.LEFT_RUN:
            self.L_image.clip_draw((9 - self.Lframe) * 50, 0, 50, 50, self.x, self.y - 15)
            self.H_image.clip_draw(50 * 7, 0, 50, 50, self.x, self.y)
        elif self.state == self.UP_RUN:
            self.UD_image.clip_draw(self.Uframe * 50, 0, 50, 50, self.x, self.y - 15)
            self.H_image.clip_draw(50 * 4, 0, 50, 50, self.x, self.y)
        elif self.state == self.DOWN_RUN:
            self.UD_image.clip_draw(self.Dframe * 50, 0, 50, 50, self.x, self.y - 15)
            self.H_image.clip_draw(50 * 0, 0, 50, 50, self.x, self.y)
        elif self.state == self.LEFT_STAND:
            self.L_image.clip_draw(3 * 50, 2 * 50, 50, 50, self.x, self.y - 15)
            self.H_image.clip_draw(50 * 7, 0, 50, 50, self.x, self.y)
        elif self.state == self.RIGHT_STAND:
            self.R_image.clip_draw(6 * 50, 0, 50, 50, self.x, self.y - 15)
            self.H_image.clip_draw(50 * 2, 0, 50, 50, self.x, self.y)
        elif self.state == self.UP_STAND:
            self.UD_image.clip_draw(0, 0, 50, 50, self.x, self.y - 15)
            self.H_image.clip_draw(50 * 4, 0, 50, 50, self.x, self.y)
        elif self.state == self.DOWN_STAND:
            self.UD_image.clip_draw(0, 0, 50, 50, self.x, self.y - 15)
            self.H_image.clip_draw(50 * 0, 0, 50, 50, self.x, self.y)
def enter():
    global isaac, map
    open_canvas()
    isaac = Isaac()
    map = Map()

def exit():
    global isaac, map
    del(isaac, map)
    close_canvas()

def update():
    clear_canvas()
    isaac.updateS()
    map.draw()
    isaac.draw()
    update_canvas()
    delay(0.05)         # 이부분은 나중에 없애고 타이머로 하는게 나을거같다

def draw():
    map.draw()
    isaac.draw()

def handle_events():
    global running, time_start
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            isaac.state = isaac.LEFT_RUN
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            isaac.state = isaac.RIGHT_RUN
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            isaac.state = isaac.DOWN_RUN
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            isaac.state = isaac.UP_RUN
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            isaac.fireDir = 1
            time_start = time.time()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            isaac.fireDir = 2
            time_start = time.time()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            isaac.fireDir = 3
            time_start = time.time()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            isaac.fireDir = 4
            time_start = time.time()
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            isaac.fireDir = 0
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            isaac.fireDir = 0
        elif event.type == SDL_KEYUP and event.key == SDLK_UP:
            isaac.fireDir = 0
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            isaac.fireDir = 0
        else:
            if isaac.state == isaac.LEFT_STAND:
                isaac.state = isaac.LEFT_STAND
            elif isaac.state == isaac.RIGHT_STAND:
                isaac.state = isaac.RIGHT_STAND
            elif isaac.state == isaac.UP_STAND:
                isaac.state = isaac.UP_STAND
            elif isaac.state == isaac.DOWN_STAND:
                isaac.state = isaac.DOWN_STAND

def pause():
    pass
def resume():
    pass