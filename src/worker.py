import pygame

grey = (128, 128, 128)


class Worker:
    """A class to manage the FEMA worker."""
    def __init__(self, ai_game):
        """Initialize the worker and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the worker image and its rect.
        self.image = pygame.transform.scale(pygame.image.load('resources/worker.png'), (30, 70))
        self.rect = self.image.get_rect()
        self.rect_box = pygame.Rect(345, 520, 400, 198)

        # Start the worker at the left middle portion of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the worker's horizontal and vertical positions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        """Update the worker position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.worker_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.worker_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.worker_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.worker_speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the worker at his current location."""
        self.screen.blit(self.image, self.rect)
