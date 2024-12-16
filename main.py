import pygame
import sys

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
            if self.x == 0:
                self.dir = 1
            elif self.x == SCREEN_WIDTH - self.width:
                self.dir = -1
            self.x += self.speed * self.dir
        else: # left, right
            if self.y == 2:
                self.dir = 1
            elif self.y == 698: #screen_height - self.width:
                self.dir = -1
            self.y += self.speed * self.dir

    def draw_me(self):
        if self.position == 'up' or self.position == 'down':
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        else: # left, right
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.height, self.width))


class Player:
    def __init__(self, height, width, speed, color):
        self.height = height; self.width = width; self.speed = speed; self.color = color
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT // 2 - self.height // 2
    def transfer(self):
        # TODO finish left, right, down mechanisms
        if self.x < left.height:  # left
            if self.y >= 350 and (self.y + self.height) <= 450:
                self.x = SCREEN_WIDTH - 40
            else:
                self.x = left.height
        if self.x > SCREEN_WIDTH - right.height - player.width:  # right
            if self.y >= 350 and (self.y + self.height) <= 450:
                self.x = 10
            else:
                self.x = SCREEN_WIDTH - right.height - self.width
        if self.y < up.height:  # up
            if self.x >= up.x and (self.x + self.width) <= up.x + up.width:
                self.y = SCREEN_HEIGHT - 40
            else:
                self.y = up.height
        if self.y > SCREEN_HEIGHT - down.height - self.height:  # down
            if self.x >= 450 and (self.x + self.width) <= 550:
                self.y = 40
            else:
                self.y = SCREEN_HEIGHT - down.height - self.height

    def draw_me(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Exit zones")

clock = pygame.time.Clock()

up = Zone('up')
down = Zone('down')
left = Zone('left')
right = Zone('right')

player = Player(30, 30, 5, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # moving
    if keys[pygame.K_a]:
        player.x -= player.speed
    if keys[pygame.K_d]:
        player.x += player.speed
    if keys[pygame.K_w]:
        player.y -= player.speed
    if keys[pygame.K_s]:
        player.y += player.speed

    # zones moving
    up.move(); down.move(); left.move(); right.move()

    # transfer
    player.transfer()


    screen.fill((30, 30, 30))

    player.draw_me()
    up.draw_me(); down.draw_me(); left.draw_me(); right.draw_me()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()