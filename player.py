import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, screen

class Player:
    def __init__(self, height, width, speed, color):
        self.height = height
        self.width = width
        self.speed = speed
        self.color = color
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT // 2 - self.height // 2

    def transfer(self, left, right, up, down):
        if self.x < left.height:  # left
            if self.y > left.y and (self.y + self.height) < (left.y + left.width):
                self.x = SCREEN_WIDTH - 40
            else:
                self.x = left.height
        if self.x > SCREEN_WIDTH - right.height - self.width:  # right
            if self.y > right.y and (self.y + self.height) < (right.y + right.width):
                self.x = 40
            else:
                self.x = SCREEN_WIDTH - right.height - self.width
        if self.y < up.height:  # up
            if self.x > up.x and (self.x + self.width) < up.x + up.width:
                self.y = SCREEN_HEIGHT - 40
            else:
                self.y = up.height
        if self.y > SCREEN_HEIGHT - down.height - self.height:  # down
            if self.x > down.x and (self.x + self.width) < down.x + down.width:
                self.y = 30
            else:
                self.y = SCREEN_HEIGHT - down.height - self.height

    def draw_me(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
