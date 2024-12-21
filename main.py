import sys
import pygame
from constants import screen
from machine import Machine
from player import Player
from zone import Zone

def main():
    player = Player(30, 30, 5, (255, 255, 255))
    up = Zone('up')
    down = Zone('down')
    left = Zone('left')
    right = Zone('right')
    machine = Machine(10)

    pygame.init()
    pygame.display.set_caption("Exit zones")
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # Moving the player
        if keys[pygame.K_a]:
            player.x -= player.speed
        if keys[pygame.K_d]:
            player.x += player.speed
        if keys[pygame.K_w]:
            player.y -= player.speed
        if keys[pygame.K_s]:
            player.y += player.speed

        # Moving the zones
        up.move()
        down.move()
        left.move()
        right.move()

        # Transfer player across zones
        player.transfer(left, right, up, down)

        machine.bullet(player.x, player.y)

        # Drawing
        screen.fill((30, 30, 30))
        player.draw_me()
        up.draw_me()
        down.draw_me()
        left.draw_me()
        right.draw_me()
        machine.draw_me()
        pygame.draw.line(screen, (255, 255, 255), (0,0), (200, 200), 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
