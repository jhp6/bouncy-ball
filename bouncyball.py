#!/bin/python3

import pygame
from pygame.locals import *
from sys import exit

from settings import Settings
from platform import BottomPlatform, TopPlatform
from ball import Ball

class BouncyBall:
    """Overall class to manage main assets and behavior."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), self.settings.screen_flags, vsync=True)
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        self.settings.screen_width = self.screen_width
        self.settings.screen_height = self.screen_height
        pygame.display.set_caption(self.settings.game_title)

        self.bottom_platform = BottomPlatform(self)
        self.top_platform = TopPlatform(self)
        self.ball = Ball(self)

        self.game_active = True # change to false after mapping a key to start the game

        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            self.settings.time_passed_seconds = self.clock.tick() / 1000
            self._check_events()

            if self.game_active:
                self.bottom_platform.update()
                self.top_platform.update()
                self._update_ball()

            self._update_screen()

    def _check_events(self):
        self._check_key_pressed_events()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit()

    def _check_key_pressed_events(self):
        self.key_pressed = pygame.key.get_pressed()

        # Map left and right arrow for platform movement
        if self.key_pressed[K_LEFT]:
            self.bottom_platform.move_left()
        elif self.key_pressed[K_RIGHT]:
            self.bottom_platform.move_right()
        # Map a to left and e to right
        if self.key_pressed[K_a]:
            self.top_platform.move_left()
        elif self.key_pressed[K_e]:
            self.top_platform.move_right()

    def _update_ball(self):
        self.ball.update()
        centerx, centery = self.ball.center
        self._check_will_hit_screen_edge(centerx, centery)
        self._check_platform_collisions(centerx, centery)

    def _check_platform_collisions(self, centerx, centery):
        # temporary
        if self.bottom_platform.rect.collidepoint(centerx, centery + self.ball.radius):
            self.ball.bounce_bottom()
        elif self.top_platform.rect.collidepoint(centerx, centery - self.ball.radius):
            self.ball.bounce_top()

    def _check_will_hit_screen_edge(self, centerx, centery):
        edge = self.ball.screen_edge_to_check
        if edge == 1:
            right = centerx + self.ball.radius
            self._check_right_screen_edge(right)
        elif edge == 2:
            top = centery - self.ball.radius
            self._check_top_screen_edge(top)
        elif edge == 3:
            left = centerx - self.ball.radius
            self._check_left_screen_edge(left)
        elif edge == 4:
            bottom = centery + self.ball.radius
            self._check_bottom_screen_edge(bottom)
    def _check_right_screen_edge(self, right):
        """Check if the ball hit the right edge of the screen and bounce if it does."""
        if right >= self.screen_width:
            self.ball.bounce_right()
    def _check_top_screen_edge(self, top):
        """Check if the ball hit the top edge of the screen and bounce if it does."""
        if top <= 0:
            self.ball.bounce_top()
    def _check_left_screen_edge(self, left):
        """Check if the ball hit the left edge of the screen and bounce if it does."""
        if left <= 0:
            self.ball.bounce_left()
    def _check_bottom_screen_edge(self, bottom):
        """Check if the ball hit the right edge of the screen and bounce if it does."""
        if bottom >= self.screen_height:
            self.ball.bounce_bottom()

    def _update_screen(self):
        self.screen.fill(self.settings.background_fill)
        self.bottom_platform.draw_platform()
        self.top_platform.draw_platform()
        self.ball.draw_ball()
        pygame.display.update()

if __name__ == "__main__":
    bb_game = BouncyBall()
    bb_game.run_game()
