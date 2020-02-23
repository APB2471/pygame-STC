import pygame.font


class Scoreboard:
    """A class to report scoring information."""
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        # Initialize font
        pygame.font.init()
        self.myfont = pygame.font.SysFont('arialblack', 25)
        self.textsurface_hs = self.myfont.render('High Score:', False, (0, 0, 0))
        self.textsurface_s = self.myfont.render('Score:', False, (0, 0, 0))
        self.textsurface_l = self.myfont.render('Level:', False, (0, 0, 0))

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

        self.display_static_text()

    def display_static_text(self):
        """Displays accessory text."""
        self.screen.blit(self.textsurface_hs, (455, 13))
        self.screen.blit(self.textsurface_s, (1115, 15))
        self.screen.blit(self.textsurface_l, (1155, 60))

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score)
        score_str = "{:,}".format(rounded_score)  # Adds commas to format large numbers
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score)
        high_score_str = "{:,}".format(high_score)  # Adds commas to format large numbers
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color2)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level reached into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    def show_score(self):
        """Draw the scores and the level to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def check_high_score(self):
        """Check to see if there is a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def level_update(self):
        """Checks to see if the player has reached a certain score, and then updates the level"""
        if self.stats.score > 60:
            self.stats.level = 2
            self.prep_level()
        if self.stats.score > 120:
            self.stats.level = 3
            self.prep_level()
