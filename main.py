import sys, pygame
from pygame.locals import *

from env import *
import shooter
import blocks

# Ball Settings
"""
Main Loop
"""
blocks.load()
while True:
    # 60FPS
    clock.tick(60)

    #Exit if demanded
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if shooting:
        shooter.update_balls_pos()
        screen.fill((0,0,0))
        shooter.update_display()
        blocks.update_display()
        pygame.display.flip()
        if not shooter.balls_alive():
            shooting = False
            blocks.update_pos()
            blocks.load()
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if shooter_x > 0:
                shooter_x -= 2
        if keys[pygame.K_RIGHT]:
            if shooter_x < width:
                shooter_x += 2
        if keys[pygame.K_UP]:
            if shooter_y > 40:
                shooter_y -= 2
        if keys[pygame.K_DOWN]:
            if shooter_y < height:
                shooter_y += 2
        if keys[pygame.K_RETURN]:
            delta_y = abs(shooter_y-0)
            delta_x = shooter_x - width/2
            speed_x = BALL_INIT_FALLING_SPEED / delta_y * delta_x
            shooter.load(speed_x)
            shooting = True
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [width/2, 0], [shooter_x, shooter_y], 2)
        blocks.update_display()
        pygame.display.flip()
