#!/bin/python3

import pygame
from pygame.sprite import Sprite

import random
import math

class Ball(Sprite):
    def __init__(self, bb_game):
        self.settings = bb_game.settings
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen_rect
        self.screen_height = self.settings.screen_height
        self.screen_width = self.settings.screen_width

        # set ball attributes
        self.color = self.settings.ball_color
        self.center = self.screen_rect.center
        self.radius = self.settings.ball_radius
        self.width = 0 # fill circle
        # movement attributes
        self.speed = self.settings.ball_speed
        self.y_speed = 0
        self.x_speed = 0
        self.angle = 0

        # store the exact horizontal and vertical position of the ball
        self.x, self.y = self.center

        self.initialize_dynamic_settings()

    def update(self):
        self.distance_moved_x = self.settings.time_passed_seconds * self.x_speed
        self.distance_moved_y = self.settings.time_passed_seconds * self.y_speed

        self.x += self.distance_moved_x
        self.y += self.distance_moved_y

        self.center = (self.x, self.y)

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)

    def initialize_dynamic_settings(self):
        self.quadrant, self.angle = divmod(random.randint(0, 359) +  90, 90)
        self.compute_speeds()

    def compute_speeds(self):
        self.x_speed = math.cos(math.radians(self.angle)) * self.speed
        self.y_speed = math.sin(math.radians(self.angle)) * self.speed
        # change the speeds to the right sign
        # if 1, then leave
        if self.quadrant == 1:
            self.y_speed *= -1
        if self.quadrant == 2:
            self.x_speed, self.y_speed = -self.y_speed, -self.x_speed
        elif self.quadrant == 3:
            self.x_speed *= -1
        elif self.quadrant == 4:
            self.x_speed, self.y_speed = self.y_speed, self.x_speed

        self._compute_screen_edge_to_check()

    def _compute_screen_edge_to_check(self):
        # 1 if right; 2 if top; 3 if left; 4 if bottom
        centerx, centery = self.center
        lefttop = math.degrees(math.atan(centery/centerx))
        leftbottom = math.degrees(math.atan((self.screen_height-centery)/centerx))
        topleft = 90 - lefttop
        topright = math.degrees(math.atan((self.screen_width-centerx)/centery))
        righttop = 90 - topright
        rightbottom = math.degrees(math.atan((self.screen_height-centery)/(self.screen_width-centerx)))
        bottomright = 90 - rightbottom
        bottomleft = 90 - leftbottom
        top = topleft + topright
        bottom = bottomright + bottomleft
        right = righttop + rightbottom
        left = lefttop + leftbottom
        degrees = righttop
        true_angle = self.angle + (self.quadrant - 1) * 90
        if true_angle <= degrees:
            self.screen_edge_to_check = 1
            return
        degrees += top
        if true_angle <= degrees:
            self.screen_edge_to_check = 2
            return
        degrees += left
        if true_angle <= degrees:
            self.screen_edge_to_check = 3
            return
        degrees += bottom
        if true_angle <= degrees:
            self.screen_edge_to_check = 4
            return
        self.screen_edge_to_check = 1

    def change_angle(self, quadrant, angle):
        """Change angle when ball bounces on a platform."""

    def bounce_right(self):
        self.angle = 90 - self.angle
        if self.y_speed < 0:
            self.quadrant = 2
        else:
            self.quadrant = 3
        self.compute_speeds()
    def bounce_top(self):
        self.angle = 90 - self.angle
        if self.x_speed > 0:
            self.quadrant = 4
        else:
            self.quadrant = 3
        self.compute_speeds()
    def bounce_left(self):
        self.angle = 90 - self.angle
        if self.y_speed < 0:
            self.quadrant = 1
        else:
            self.quadrant = 4
        self.compute_speeds()
    def bounce_bottom(self):
        self.angle = 90 - self.angle
        if self.x_speed > 0:
            self.quadrant = 1
        else:
            self.quadrant = 2
        self.quadrant
        self.compute_speeds()

