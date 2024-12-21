import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, screen

class Zone:
    def __init__(self, position):
        self.position = position
        self.width = 100
        self.height = 10
        self.speed = 3
        self.dir = -1
        self.color = (255, 100, 100)
        if position == 'up':
            self.x = SCREEN_WIDTH // 2 - self.width // 2
            self.y = 0
        elif position == 'down':
            self.x = SCREEN_WIDTH // 2 - self.width // 2
            self.y = SCREEN_HEIGHT - self.height
        elif position == 'left':
            self.x = 0
            self.y = SCREEN_HEIGHT // 2 - self.height // 2
        elif position == 'right':
            self.x = SCREEN_WIDTH - 10
            self.y = SCREEN_HEIGHT // 2 - self.height // 2

    def move(self):
        if self.position == 'up' or self.position == 'down':
            if self.x <= 0:
                self.dir = 1
            elif self.x >= SCREEN_WIDTH - self.width:
                self.dir = -1
            self.x += self.speed * self.dir
        else:  # left, right
            if self.y <= 2:
                self.dir = 1
            elif self.y >= SCREEN_HEIGHT - self.width:
                self.dir = -1
            self.y += self.speed * self.dir

    def draw_me(self):
        if self.position in ['up', 'down']:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        else:  # left, right
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.height, self.width))
