import pygame
from pygame.sprite import Sprite

class Platform(Sprite):
    def __init__(self, bb_game):
        self.settings = bb_game.settings
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen_rect

        # create platform rect and set its initial position
        self.rect = pygame.Rect((0, 0), (self.settings.screen_width // self.settings.platform_xth_screen_width, self.settings.platform_height))

        # set platform initial attributes
        self.color = self.settings.platform_color
        self.speed = self.settings.platform_speed

        # store the platforms exact horizontal position
        self.x = self.rect.x

        # 1 if right; -1 if left; 0 if still
        self.move = 0

    def update(self):
        self.rect.x = self.x

    def draw_platform(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move_right(self):
        self.distance_moved = self.speed * self.settings.time_passed_seconds
        self.x += self.distance_moved

    def move_left(self):
        self.distance_moved = self.speed * self.settings.time_passed_seconds
        self.x -= self.distance_moved

    def stop_move(self):
        self.move = 0

class BottomPlatform(Platform):
    def __init__(self, bb_game):
        super().__init__(bb_game)
        self.rect.midbottom = (self.screen_rect.centerx, self.screen_rect.bottom - self.settings.platform_to_ground)
        self.x = self.rect.x

class TopPlatform(Platform):
    def __init__(self, bb_game):
        super().__init__(bb_game)
        self.rect.midtop = (self.screen_rect.centerx, self.settings.platform_to_ground)
        self.x = self.rect.x

