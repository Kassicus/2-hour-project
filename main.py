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

        self.spawn_rate = 15

        self.score = fireball.kills

        self.score_font = pygame.font.Font('assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf', 32)
        self.score_text = pygame.font.Font.render(self.score_font, "Score: ", False, data.colors['black'])
        self.score_value = pygame.font.Font.render(self.score_font, str(self.score), False, data.colors['black'])

        self.game_over_font = pygame.font.Font('assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf', 64)
        self.game_over_text = pygame.font.Font.render(self.game_over_font, "Game Over!", False, data.colors['red'])

        self.gameover = False

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
        if not self.gameover:
            self.screen.fill(data.colors['white'])
            self.screen.blit(sky, (0, 0))
            self.screen.blit(ground, (0, 500))

            self.screen.blit(self.score_text, (480, 5))
            self.screen.blit(self.score_value, (680, 5))

            self.player_mana.draw(self.screen)
            self.player_health.draw(self.screen)

            enemy.enemies.draw(self.screen)

            self.player.draw(self.screen)

            fireball.fireballs.draw(self.screen)

    def update(self):
        if not self.gameover:
            self.player.update()

            fireball.fireballs.update()
            self.player_mana.status = int(self.player.mana * 3)
            self.player_health.status = int(self.player.health * 3)

            enemy.enemies.update()

            self.score = fireball.kills
            self.score_value = pygame.font.Font.render(self.score_font, str(self.score), False, data.colors['black'])

            self.spawn_enemy()

            if self.player.health <= 0:
                self.gameover = True
                game_over()

        pygame.display.update()
        #print(self.clock)
        self.clock.tick(30)

    def spawn_enemy(self):
        spawn_chance = random.randint(1, self.spawn_rate)
        if spawn_chance == 1:
            spawn_dir = random.choice(['left', 'right'])

            e = enemy.Enemy(spawn_dir)
            enemy.enemies.add(e)

def game_over():
    game.screen.blit(game.game_over_text, (200, 200))


game = Game(1000, 600, "Kill the Pigs")
game.start()

pygame.quit()
