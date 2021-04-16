import pygame
import fireball

LEFT = pygame.image.load('assets/player/player_left.png')
LEFT_BOB = pygame.image.load('assets/player/player_left_bob.png')
RIGHT = pygame.image.load('assets/player/player_right.png')
RIGHT_BOB = pygame.image.load('assets/player/player_right_bob.png')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x = 500
        self.y = 500

        self.velocity = 0
        self.speed = 8

        self.bob_timer = 10

        self.dir = ''

        self.image = LEFT

        self.rect = (self.x, self.y)

    def update(self):
        self.x += self.velocity

        self.rect = (self.x, self.y)

        self.bob()

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
        f = fireball.Fireball(self.x, self.y, self.dir)
        fireball.fireballs.add(f)

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
