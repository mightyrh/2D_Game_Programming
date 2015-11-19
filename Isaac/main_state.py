from pico2d import *

import game_framework

from Isaac_move_modified import Isaac
from room import Room

name = "main_state"

isaac = None
room = None

def create_world():
    global isaac, room
    isaac = Isaac()
    room = Room()

def destroy_world():
    global isaac, room

    del(isaac)
    del(room)

def enter():
    open_canvas(960, 550)
    game_framework.reset_time()
    create_world()

def exit():
    destroy_world()
    close_canvas()

def update(frame_time):
    isaac.update(frame_time)

def draw(frame_time):
    clear_canvas()
    room.draw()
    isaac.draw()
    update_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
            else:
                isaac.handle_event(event)

def pause():
    pass
def resume():
    pass