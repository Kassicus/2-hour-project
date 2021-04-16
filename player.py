import pygame
import fireball
import random
import enemy

LEFT = pygame.image.load('assets/player/player_left.png')
LEFT_BOB = pygame.image.load('assets/player/player_left_bob.png')
RIGHT = pygame.image.load('assets/player/player_right.png')
RIGHT_BOB = pygame.image.load('assets/player/player_right_bob.png')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x = 500
        self.y = 436

        self.velocity = 0
        self.speed = 8

        self.mana = 100
        self.health = 100

        self.bob_timer = 10

        self.dir = ''

        self.image = LEFT

        self.rect = (self.x, self.y)

    def update(self):
        self.x += self.velocity

        self.rect = (self.x, self.y)

        self.bob()

        self.restore_mana()

        self.check_collide()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move(self, dir):
        if dir == 'left':
            self.velocity = -self.speed
            self.image = LEFT
            self.dir = dir
        elif dir == 'right':
            self.velocity = self.speed
            self.image = RIGHT
            self.dir = dir
        elif dir == 'stop':
            self.velocity = 0

    def shoot(self):
        if self.mana > 5:
            f = fireball.Fireball(self.x, self.y, self.dir)
            fireball.fireballs.add(f)
            self.mana -= 5

    def bob(self):
        self.bob_timer -= 1

        if self.bob_timer == 0:
            if self.image == LEFT:
                self.image = LEFT_BOB
            elif self.image == LEFT_BOB:
                self.image = LEFT
            elif self.image == RIGHT:
                self.image = RIGHT_BOB
            elif self.image == RIGHT_BOB:
                self.image = RIGHT

            self.bob_timer = 10

    def restore_mana(self):
        if self.mana < 100:
            restore = random.randint(1, 3)
            if restore == 1:
                self.mana += 1

    def check_collide(self):
        for e in enemy.enemies:
            if e.x < self.x < e.x + 64:
                e.kill()
                self.health -= 10
