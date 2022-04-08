import pygame
import random
pygame.init()

# Window & Customization
win = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Game")


class Square:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw_square(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def sqr_boundaries(self):
        if self.x >= 750:
            self.x = 750
        elif self.x <= 0:
            self.x = 0


class Enemy:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw_enemy(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def enemy_mov(self):
        if self.x < -50:
            self.x = random.randint(1000, 2000)
        else:
            self.x -= 10


def spawn_enemies(waves, lst_enemies):
    for x in range(waves):
        x = Enemy(25, 25, 300, 300)
        lst_enemies.append(x)
    for y in lst_enemies:
        y.draw_enemy(win)
        y.enemy_mov()


enemies = []
enemy_waves = 6
spawn_enemies(enemy_waves, enemies)

sqr1 = Square(50, 50, 100, 275)
# en1 = Enemy(25, 25, 800, 300)

jumping = False
jump_count = 10

# Clock
CLOCK = pygame.time.Clock()
count = 0
# Game Loop
run = True
while run:
    CLOCK.tick(60)
    win.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    count += 1
    print(count)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    # Enemies (draw)
    for enemy in enemies:
        enemy.draw_enemy(win)

    # Square (draw)
    sqr1.draw_square(win)

    # Movement keys for squares
    if keys[pygame.K_LEFT]:
        sqr1.x -= 20
    if keys[pygame.K_RIGHT]:
        sqr1.x += 20
    # Movement for enemy
    for enemy in enemies:
        enemy.enemy_mov()

    # Jumping functions for square
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            sqr1.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10

    # Square Boundaries
    sqr1.sqr_boundaries()

    # en1.draw_enemy(win)
    pygame.display.update()
