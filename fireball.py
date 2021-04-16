import pygame
import enemy

fireballs = pygame.sprite.Group()

LEFT = pygame.image.load('assets/projectiles/fireball_left.png')
RIGHT = pygame.image.load('assets/projectiles/fireball_right.png')

class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y, dir):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.speed = 32
        self.velocity = -self.speed

        self.image = LEFT

        if dir == 'left':
            self.image = LEFT
            self.velocity = -self.speed
        elif dir == 'right':
            self.image = RIGHT
            self.velocity = self.speed

        self.rect = (self.x, self.y)

    def update(self):
        self.x += self.velocity

        self.rect = (self.x, self.y)

        if self.x < -100:
            self.kill()

        if self.x > 1100:
            self.kill()

        self.check_collide()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def check_collide(self):
        for e in enemy.enemies:
            if self.x > e.x and self.x + 32 < e.x + 64:
                self.kill()
                e.kill()
