import pygame
import data
import player
import fireball
import ui
import enemy
import random

pygame.init()

ground = pygame.image.load('assets/terrain/ground.png')
sky = pygame.image.load('assets/terrain/skybox.png')

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

        self.player_mana = ui.Bar(5, 5, data.colors['purple'])
        self.player_health = ui.Bar(5, 45, data.colors['red'])

        self.spawn_rate = 20

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

                    if event.key == pygame.K_SPACE:
                        self.player.shoot()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.player.move('stop')

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(data.colors['white'])
        self.screen.blit(sky, (0, 0))
        self.screen.blit(ground, (0, 500))

        self.player_mana.draw(self.screen)
        self.player_health.draw(self.screen)

        enemy.enemies.draw(self.screen)

        self.player.draw(self.screen)

        fireball.fireballs.draw(self.screen)

    def update(self):
        self.player.update()

        fireball.fireballs.update()
        self.player_mana.status = int(self.player.mana * 3)
        self.player_health.status = int(self.player.health * 3)

        enemy.enemies.update()

        self.spawn_enemy()

        pygame.display.update()
        self.clock.tick(30)

    def spawn_enemy(self):
        spawn_chance = random.randint(1, self.spawn_rate)
        if spawn_chance == 1:
            spawn_dir = random.choice(['left', 'right'])

            e = enemy.Enemy(spawn_dir)
            enemy.enemies.add(e)



game = Game(1000, 600, "Kill the Pigs")
game.start()

pygame.quit()
