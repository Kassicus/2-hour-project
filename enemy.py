import pygame

enemies = pygame.sprite.Group()

LEFT = pygame.image.load('assets/enemy/slime_left.png')
RIGHT = pygame.image.load('assets/enemy/slime_right.png')

class Enemy(pygame.sprite.Sprite):
    def __init__(self, dir):
        pygame.sprite.Sprite.__init__(self)

        self.x = -74
        self.y = 436

        self.speed = 5
        self.velocity = self.speed

        self.image = LEFT

        if dir == 'left':
            pass
        elif dir == 'right':
            self.x = 1010
            self.image = RIGHT
            self.velocity = -self.speed

        self.rect = (self.x, self.y)

    def update(self):
        self.x += self.velocity

        self.rect = (self.x, self.y)

        if self.x > 1100:
            self.kill()

        if self.x < -100:
            self.kill()
