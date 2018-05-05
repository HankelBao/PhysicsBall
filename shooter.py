from env import *
import blocks
import random 

balls = []
number_of_balls = 1
tick = 0
activate_id = 0

def load(speed_x):
    global number_of_balls, balls, tick
    balls = []
    for i in range(0, number_of_balls):
        ball = Ball(width/2, BALL_RADIUS, BALL_RADIUS, speed_x, BALL_INIT_FALLING_SPEED, i*10)
        balls.append(ball)
    number_of_balls += 1
    tick = 0


def update_balls_pos():
    global tick, balls
    tick += 1
    for ball in balls:
        if tick > ball.activate_tick and ball.alive:
            ball.speed.exp_gravity(GRAVITY, MAX_SPEED)
            if ball.left() < 0:
                ball.speed.rightward()
            if ball.right() > width:
                ball.speed.leftward()
            if ball.bottom() > height:
                ball.die()
            if ball.top() < 0:
                ball.speed.downward()

            for block in blocks.blocks:
                dis_x = abs(block.center_x() - ball.center_x())
                dis_y = abs(block.center_y() - ball.center_y())
                dis_collision = BALL_RADIUS + BLOCK_RADIUS
                if dis_x < dis_collision and dis_y < dis_collision:
                    if abs(dis_x-dis_collision) < abs(dis_y-dis_collision):
                        # Collision in x coordination
                        if block.center_x() < ball.center_x():
                            ball.speed.rightward()
                        if block.center_x() > ball.center_x():
                            ball.speed.leftward()
                    else:
                        if block.center_y() < ball.center_y():
                            ball.speed.downward()
                        if block.center_y() > ball.center_y():
                            ball.speed.upward()
                    blocks.collide(block)
            pygame.display.set_caption(str(ball.speed.x)+","+str(ball.speed.y))
            ball.move()

def update_display():
    global balls
    for ball in balls:
        if ball.alive:
            ball.display()

def balls_alive():
    global balls
    for ball in balls:
        if ball.alive:
            return True
    return False

class Ball():
    def __init__(self, x, y, r, speed_x, speed_y, t):
        self.x = x
        self.y = y
        self.r = r
        self.speed = Speed(speed_x, speed_y)
        self.activate_tick = t
        self.alive = True

    def move(self):
        self.x += self.speed.x
        self.y += self.speed.y

    def die(self):
        self.alive = False

    def display(self):
        pos = [int(self.x), int(self.y)]
        pygame.draw.circle(screen, WHITE, pos, self.r)

    def left(self):
        return self.x-self.r

    def right(self):
        return self.x+self.r

    def top(self):
        return self.y-self.r

    def bottom(self):
        return self.y+self.r

    def center_x(self):
        return self.x

    def center_y(self):
        return self.y

class Speed():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def exp_gravity(self, gravity, max_speed):
        if self.y < max_speed:
            self.y += gravity
        else:
            self.y = max_speed

    def x_hit(self):
        self.x = -self.x

    def leftward(self):
        self.x = -abs(self.x)

    def rightward(self):
        self.x = abs(self.x)

    def upward(self):
        self.y = -abs(self.y)
        self.x += random.randint(-10, 10)/10

    def downward(self):
        self.y = abs(self.y)

    def y_hit(self):
        self.y = -self.y
