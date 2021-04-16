import pygame
import data
import player

pygame.init()

class Game():
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(self.title)

        self.running = True
        self.clock = pygame.time.Clock()

        self.events = pygame.event.get()

        self.player = player.Player()

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player.move('left')
                    elif event.key == pygame.K_d:
                        self.player.move('right')

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.player.move('stop')

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(data.colors['white'])

        self.player.draw(self.screen)

    def update(self):
        self.player.update()

        pygame.display.update()
        self.clock.tick(30)

game = Game(1000, 600, "Kill the Pigs")
game.start()

pygame.quit()
