import random

blocks = []

def load():
    for i in range(0, len(blocks)+1):
        create_random_block()

def create_random_block():
    x = random.randint(0, width-BLOCK_RADIUS*2)
    y = random.randint(height/2, height)
    n = random.randint(1,10)
    block = Block(x, y, BLOCK_RADIUS, n)
    if check_block_valid(block):
        blocks.append(block)
    else:
        create_random_block()

def check_block_valid(target_block):
    for block in blocks:
        dis_x = abs(block.center_x() - target_block.center_x())
        dis_y = abs(block.center_y() - target_block.center_y())
        dis_collision = BALL_RADIUS + BLOCK_RADIUS
        if dis_x < dis_collision and dis_y < dis_collision:
            return False
    return True

def collide(block):
    block.n -= 1
    if block.n <= 0:
        blocks.remove(block)

def update_pos():
    global blocks
    for block in blocks:
        block.y -= 0.2

def update_display():
    for block in blocks:
        block.display()

class Block():
    def __init__(self, x, y, r, n):
        self.x = x
        self.y = y
        self.r = r
        self.n = n

    def display(self):
        color = int(256 - self.n*25)
        pygame.draw.rect(screen, (255,color,color), [self.x,self.y,self.r*2,self.r*2])

    def left(self):
        return self.x

    def right(self):
        return self.x+self.r*2

    def top(self):
        return self.y

    def bottom(self):
        return self.y+self.r*2

    def center_x(self):
        return self.x + self.r

    def center_y(self):
        return self.y + self.r
