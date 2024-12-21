import math

import pygame

from constants import screen, SCREEN_HEIGHT

# TODO finish mechanism

class Machine:
    def __init__(self, speed):
        self.speed = speed
        self.color = (255, 255, 255)
        self.width = 30
        self.height = 30
        self.lines = []
        self.ks = []

    def bullet(self, player_x, player_y):
        k = player_y / player_x
        if k not in self.ks:
            self.ks.append(k)
            self.lines.append([(20, SCREEN_HEIGHT - self.height)])
        for i in range(len(self.lines)):
            kk = self.ks[i]
            _line = self.lines[i]
            prev_c = [_line[len(_line) - 1][0], _line[len(_line) - 1][1]]
            self.lines[i].append((prev_c[0] + self.speed, prev_c[1] - kk * self.speed))

        for i in range(len(self.lines)):
            _line = self.lines[i]
            for j in range(1, len(_line)):
                c = _line[j]
                pygame.draw.line(screen, (255, 255, 0), (_line[j-1][0], _line[j-1][1]), (c[0], c[1]), 2)
                print((_line[j-1][0], _line[j-1][1]), (c[0], c[1]))

    def draw_me(self):
        pygame.draw.arc(screen, (255, 255, 255), [0, SCREEN_HEIGHT - self.height, self.width, self.height], math.radians(0), math.radians(90), 3)
        #pygame.draw.rect(screen, self.color, (0, SCREEN_HEIGHT - self.height, self.width, self.height))


class Line:
    def __init__(self, k, start_x, start_y, step):
        self.k = k
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = start_x
        self.end_y = start_y
        self.step = step

    def draw_me(self):
        self.end_x = self.end_x + self.step
        self.end_y = self.end_y - self.k * self.step
        pygame.draw.line(screen, (255, 255, 0), (self.start_x, self.start_y), (self.end_x, self.end_y))
