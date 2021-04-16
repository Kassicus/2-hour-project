import pygame
import data

class Bar(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.width = 310
        self.height = 35

        self.status_x = self.x + 5
        self.status_y = self.y + 5

        self.status_color = color

        self.status = 0

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(data.colors['gray'])

        self.rect = (self.x, self.y)

    def update(self):
        self.rect = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        pygame.draw.rect(surface, self.status_color, (self.status_x, self.status_y, self.status, 25))
