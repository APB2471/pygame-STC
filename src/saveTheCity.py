# Title: Secure the city: A game about being prepared
# Files: See resources
# Semester: 1st (2019)
#
# Author: Willow560
# Version: Release
import sys
import pygame
import shelve
# from time import sleep
from materials import Materials
from settings import Settings
from worker import Worker
from music import Music
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

WATER_RECT = pygame.Rect(640, 240, 30, 30)
FOOD_RECT = pygame.Rect(580, 240, 30, 30)
PRODUCT_RECT = pygame.Rect(520, 240, 30, 30)
MEDICINE_RECT = pygame.Rect(460, 240, 30, 30)
GEAR_RECT = pygame.Rect(400, 240, 30, 30)
RESIDENTIAL_RECT = pygame.Rect(875, 14, 143, 690)


class SaveTheCity:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.music = Music()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Save the City")
        self.statistics_image = pygame.image.load('resources/stats.png')

        # Reading the score from disk
        # d = shelve.open('resources/high_score')
        # score = d['saved_score']
        # Create an instance to store game statistics-
        # -and create a scoreboard.
        self.stats = GameStats(self, 0)
        self.sb = Scoreboard(self)

        self.materials = Materials(self, self.settings.difficulty_level)
        self.worker = Worker(self)

        # Cooldown for collecting resources
        self.last = pygame.time.get_ticks()
        self.cooldown = 0
        # List for obtained values
        self.obtained_list = [False, False, False, False, False]

        # Make the play button
        self.play_button = Button(self, "Play")

        self.show = None
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.worker.update()
                self.music.start_music()
            else:
                self.music.stop_music()

            self._update_screen()

    def _check_events(self):
        """Respond to keypress and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # d = shelve.open('resources/high_score')
                # d['saved_score'] = self.stats.high_score
                # d.close()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == self.materials.LENGTH_EVENT:
                if self.stats.game_active:  # Only updates if the game is active
                    self.materials.update()
            elif event.type == self.materials.DIFFICULTY_EVENT:
                if self.stats.game_active:
                    self.materials.increase_difficulty()
            elif event.type == self.settings.POINT_EVENT:
                if self.stats.game_active:
                    self.settings.increase_speed()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            # self.settings.initialize_dynamic_settings()
            # Reset the game statistics.
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.materials.reset_difficulty()
            self.materials.reset_lengths()
            self.stats.game_active = True
            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _start_game(self):
        """Start a new game after the player hits the p key"""
        # Reset the game statistics.
        if not self.stats.game_active:
            self.stats.reset_stats()
            self.materials.reset_lengths()
            self.stats.game_active = True
            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.worker.moving_right = True
        if event.key == pygame.K_LEFT:
            self.worker.moving_left = True
        if event.key == pygame.K_UP:
            self.worker.moving_up = True
        if event.key == pygame.K_DOWN:
            self.worker.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_p:
            self._start_game()
        if event.key == pygame.K_h:
            self.show = True
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.worker.moving_right = False
        if event.key == pygame.K_LEFT:
            self.worker.moving_left = False
        if event.key == pygame.K_UP:
            self.worker.moving_up = False
        if event.key == pygame.K_DOWN:
            self.worker.moving_down = False
        if event.key == pygame.K_h:
            self.show = False
    def _check_health(self):
        """Checks to see if any lengths are 0, and checks if the workers health is 0"""
        if min(self.materials.lengths) <= 0:
            for i in range(0, len(self.materials.lengths)):
                self.materials.lengths[i] = 0
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.settings.background, (0, 0))

        # Blit static images
        self.materials.blit_static()
        self._check_collision()
        self._check_resource()
        self.materials.blit_rects()
        self.worker.blitme()
        self._check_health()
        self.sb.level_update()
        # Draw the score and level information:
        self.sb.display_static_text()
        self.sb.show_score()

        if self.show:
            self.screen.blit(self.statistics_image, (380, 220))

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _check_collision(self):
        """Check for a collision between the player and the resource blocks and give the resource to the player"""
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            if not(any(self.obtained_list)):
                if self.worker.rect.colliderect(WATER_RECT):
                    self.obtained_list[0] = True
                    self.music.pop_sound_effect()
                if self.worker.rect.colliderect(FOOD_RECT):
                    self.obtained_list[1] = True
                    self.music.pop_sound_effect()
                if self.worker.rect.colliderect(PRODUCT_RECT):
                    self.obtained_list[2] = True
                    self.music.pop_sound_effect()
                if self.worker.rect.colliderect(MEDICINE_RECT):
                    self.obtained_list[3] = True
                    self.music.pop_sound_effect()
                if self.worker.rect.colliderect(GEAR_RECT):
                    self.obtained_list[4] = True
                    self.music.pop_sound_effect()

    def _check_resource(self):
        """Check to see if the player is touching the block, and if he has a resource"""
        if RESIDENTIAL_RECT.contains(self.worker.rect):
            if self.obtained_list[0]:
                self.obtained_list[0] = False
                self.music.thunk_sound_effect()
                if self.materials.lengths[0] <= 270:
                    self.materials.lengths[0] += 50
                else:
                    self.materials.lengths[0] = 320
                self.stats.score += self.settings.points_list[0]
                self.sb.prep_score()
                self.sb.check_high_score()

            if self.obtained_list[1]:
                self.obtained_list[1] = False
                self.music.thunk_sound_effect()
                if self.materials.lengths[1] <= 270:
                    self.materials.lengths[1] += 50
                else:
                    self.materials.lengths[1] = 320
                self.stats.score += self.settings.points_list[1]
                self.sb.prep_score()
                self.sb.check_high_score()

            if self.obtained_list[2]:
                self.obtained_list[2] = False
                self.music.thunk_sound_effect()
                if self.materials.lengths[2] <= 270:
                    self.materials.lengths[2] += 50
                else:
                    self.materials.lengths[2] = 320
                self.stats.score += self.settings.points_list[2]
                self.sb.prep_score()
                self.sb.check_high_score()

            if self.obtained_list[3]:
                self.obtained_list[3] = False
                self.music.thunk_sound_effect()
                if self.materials.lengths[3] <= 270:
                    self.materials.lengths[3] += 50
                else:
                    self.materials.lengths[3] = 320
                self.stats.score += self.settings.points_list[3]
                self.sb.prep_score()
                self.sb.check_high_score()

            if self.obtained_list[4]:
                self.obtained_list[4] = False
                self.music.thunk_sound_effect()
                if self.materials.lengths[4] <= 270:
                    self.materials.lengths[4] += 50
                else:
                    self.materials.lengths[4] = 320
                self.stats.score += self.settings.points_list[4]
                self.sb.prep_score()
                self.sb.check_high_score()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SaveTheCity()
    ai.run_game()
