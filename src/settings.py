import pygame


class Settings:
    """A class to store all settings for Save the City"""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (0, 84, 166)
        self.bg_color2 = (70, 70, 70)
        self.background = pygame.image.load('resources/GameBackground.png')

        # Ship settings
        self.worker_speed = 5
        # How quickly the game speeds up
        self.speedup_scale = 1
        # How quickly the point values increase
        self.score_scale = 1
        # Rate a which the blocks decrease in size minus the previous value
        self.difficulty_level = 1
        # Scoring
        self.points_list = [5, 4, 3, 2, 1]
        # [0]=water, [1]=food, [2]=sanitary products, [3]=medicine, [4]=gear
        # Create event to increase point values
        self.POINT_EVENT = pygame.USEREVENT + 3
        pygame.time.set_timer(self.POINT_EVENT, 5000)

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
    def increase_speed(self):
        """Increase speed settings and point values for resources"""
        self.points_list = [x + self.score_scale for x in self.points_list]
