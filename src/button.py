import pygame.font


class Button:

    def __init__(self, ai_game, msg):
        """Initialize button attributes"""
        pygame.font.init()
        myfont = pygame.font.SysFont('impact', 30)
        self.title_surface = myfont.render("Save the City: A Game About Being Prepared", False, (204, 0, 0))
        self.name_surface = myfont.render("Made by Andrew Bush", False, (204, 0, 0))

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw the message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.title_surface, (330, 55))
        self.screen.blit(self.name_surface, (440, 95))
