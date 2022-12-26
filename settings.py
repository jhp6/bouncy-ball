#!/bin/python3

from pygame.locals import *

class Settings:
    def __init__(self):
        # General game settings
        self.game_title = "Bouncy Ball"

        # Screen settings
        self.screen_width = 0
        self.screen_height = 0
        self.screen_flags = FULLSCREEN
        # alternative screen settings
        # self.screen_width = number
        # self.screen_height = number
        # self.screen_flags = RESIZABLE

        # Background settings
        self.background_fill = (0, 0, 0) # Black

        # Platform settings
        self.platform_xth_screen_width = 5
        self.platform_height = 25
        self.platform_yth_screen_width = 0
        self.platform_to_ground = 50
        self.platform_speed = 300
        self.platform_color = (255, 255, 255) # White

        # Ball settings
        self.ball_color = (255, 255, 255) # White
        self.ball_radius = 15

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.time_passed_seconds = 0
        self.ball_speed = 1000
