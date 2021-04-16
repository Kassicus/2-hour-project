import pygame

LEFT = pygame.image.load('assets/player/player_left.png')
RIGHT = pygame.image.load('assets/player/player_right.png')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x = 500
        self.y = 500
        self.width = 32
        self.height = 32

        self.velocity = 0
        self.speed = 8

        self.image = LEFT

        self.rect = (self.x, self.y)

    def update(self):
        self.x += self.velocity

        self.rect = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move(self, dir):
        if dir == 'left':
            self.velocity = -self.speed
            self.image = LEFT
        elif dir == 'right':
            self.velocity = self.speed
            self.image = RIGHT
        elif dir == 'stop':
            self.velocity = 0
