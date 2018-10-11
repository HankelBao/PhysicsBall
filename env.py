import pygame
# Constants
GRAVITY = 0.20
MAX_SPEED = 8
BALL_RADIUS = 10
BALL_INIT_FALLING_SPEED = 7.0
BLOCK_RADIUS = 15
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Global Settings
pygame.init()
size = width, height = 400, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
shooting = False
shooter_x = width/2
shooter_y = 60
