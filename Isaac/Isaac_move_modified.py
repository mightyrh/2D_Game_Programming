from pico2d import *


running = None



class Isaac:

    PIXEL_PER_METER = (50.0 / 1.0)      # 50 pixel 1 meter
    RUN_SPEED_MPS = 5.0
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    head = None
    body = None

    LEFT_RUN, RIGHT_RUN, UP_RUN, DOWN_RUN, STAND = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = 480, 270
        self.total_frames = 0.0
        self.frame = 0
        self.head_frame = 0
        self.state = self.STAND
        self.speed = 0
        self.uspeed = 0
        self.body_and_head = load_image('body_and_head.png')

    def update(self, frame_time):
        self.distance = Isaac.RUN_SPEED_PPS * frame_time
        self.total_frames += Isaac.FRAMES_PER_ACTION * Isaac.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 10
        self.x = (self.x + frame_time * self.speed)
        self.y = (self.y + frame_time * self.uspeed)

    def draw(self):
        if self.state == self.LEFT_RUN:
            self.body_and_head.clip_draw((9 - self.frame) * 50, 50 * 1, 50, 50, self.x, self.y - 17, 60, 60)
            self.body_and_head.clip_draw(50 * 7, 0, 50, 50, self.x, self.y, 60, 60)
        elif self.state == self.RIGHT_RUN:
            self.body_and_head.clip_draw(self.frame * 50, 50 * 2, 50, 50, self.x, self.y - 17, 60, 60)
            self.body_and_head.clip_draw(50 * 2, 0, 50, 50, self.x, self.y, 60, 60)
        elif self.state == self.UP_RUN:
            self.body_and_head.clip_draw(self.frame * 50, 50 * 3, 50, 50, self.x, self.y - 17, 60, 60)
            self.body_and_head.clip_draw(50 * 4, 0, 50, 50, self.x, self.y, 60, 60)
        elif self.state == self.DOWN_RUN:
            self.body_and_head.clip_draw(self.frame * 50, 50 * 3, 50, 50, self.x, self.y - 17, 60, 60)
            self.body_and_head.clip_draw(50 * 0, 0, 50, 50, self.x, self.y, 60, 60)
        elif self.state == self.STAND:
            self.body_and_head.clip_draw(0, 50 * 3, 50, 50, self.x, self.y - 17, 60, 60)
            self.body_and_head.clip_draw(0, 0, 50, 50, self.x, self.y, 60, 60)

    def handle_event(self, event):
       if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                self.state = self.LEFT_RUN
                self.speed -= Isaac.RUN_SPEED_PPS
            elif event.key == SDLK_d:
                self.state = self.RIGHT_RUN
                self.speed += Isaac.RUN_SPEED_PPS
            elif event.key == SDLK_s:
                self.state = self.DOWN_RUN
                self.uspeed -= Isaac.RUN_SPEED_PPS
            elif event.key == SDLK_w:
                self.state = self.UP_RUN
                self.uspeed += Isaac.RUN_SPEED_PPS
       if event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                self.state = self.STAND
                self.speed += Isaac.RUN_SPEED_PPS
            elif event.key == SDLK_d:
                self.state = self.STAND
                self.speed -= Isaac.RUN_SPEED_PPS
            elif event.key == SDLK_s:
                self.state = self.STAND
                self.uspeed += Isaac.RUN_SPEED_PPS
            elif event.key == SDLK_w:
                self.state = self.STAND
                self.uspeed -= Isaac.RUN_SPEED_PPS
