import pygame


class Materials:
    """A class to handle to material bars"""
    def __init__(self, ai_game, difficulty_level):
        """Initalize the resource bars and images"""
        self.LENGTH_EVENT = pygame.USEREVENT + 0
        pygame.time.set_timer(self.LENGTH_EVENT, 1000)

        self.DIFFICULTY_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.DIFFICULTY_EVENT, 3000)

        self.lengths = [320, 320, 320, 320, 320]
        # [0]=water, [1]=food, [2]=sanitary products, [3]=medicine, [4]=gear
        self.difficulty = [7, 4, 2, 3, 2]
        # [0]=water, [1]=food, [2]=sanitary products, [3]=medicine, [4]=gear
        self.difficulty_copy = self.difficulty[:]

        self.difficulty_level = difficulty_level

        self.screen = ai_game.screen
        self.WATER_IMG = pygame.transform.scale(pygame.image.load('resources/water.png'), (30, 30))
        self.FOOD_IMG = pygame.transform.scale(pygame.image.load('resources/fooditems.png'), (30, 30))
        self.PRODUCT_IMG = pygame.transform.scale(pygame.image.load('resources/toiletpaper.png'), (30, 30))
        self.MEDICINE_IMG = pygame.transform.scale(pygame.image.load('resources/meds.png'), (30, 30))
        self.GEAR_IMG = pygame.transform.scale(pygame.image.load('resources/tools.png'), (30, 30))
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.AQUA = (0, 255, 255)
        self.BLUE = (0, 0, 255)
        self.FUCHSIA = (255, 0, 255)
        self.GRAY = (128, 128, 128)
        self.GREEN = (0, 128, 0)
        self.LIME = (0, 255, 0)
        self.MAROON = (128, 0, 0)
        self.NAVY_BLUE = (0, 0, 128)
        self.OLIVE = (128, 128, 0)
        self.PURPLE = (128, 0, 128)
        self.RED = (255, 0, 0)
        self.SILVER = (192, 192, 192)
        self.TEAL = (0, 128, 128)
        self.YELLOW = (255, 255, 0)
        
    def blit_static(self):
        self.screen.blit(self.WATER_IMG, (640, 240))
        self.screen.blit(self.FOOD_IMG, (580, 240))
        self.screen.blit(self.PRODUCT_IMG, (520, 240))
        self.screen.blit(self.MEDICINE_IMG, (460, 240))
        self.screen.blit(self.GEAR_IMG, (400, 240))
        self.screen.blit(self.WATER_IMG, (360, 530))
        self.screen.blit(self.FOOD_IMG, (360, 570))
        self.screen.blit(self.PRODUCT_IMG, (360, 610))
        self.screen.blit(self.MEDICINE_IMG, (360, 650))
        self.screen.blit(self.GEAR_IMG, (360, 685))

        # Rectangle around the resource bars
        pygame.draw.rect(self.screen, (128, 128, 128), (345, 520, 400, 198), 4)

    def update(self):
        """Update the resource bars"""
        self.lengths[0] -= self.difficulty[0]
        self.lengths[1] -= self.difficulty[1]
        self.lengths[2] -= self.difficulty[2]
        self.lengths[3] -= self.difficulty[3]
        self.lengths[4] -= self.difficulty[4]

    def blit_rects(self):
        """Blit the rectangles to the screen after they have been updated"""
        pygame.draw.rect(self.screen, self.GREEN, (400, 540, self.lengths[0], 10))
        pygame.draw.rect(self.screen, self.GREEN, (400, 580, self.lengths[1], 10))
        pygame.draw.rect(self.screen, self.GREEN, (400, 620, self.lengths[2], 10))
        pygame.draw.rect(self.screen, self.GREEN, (400, 660, self.lengths[3], 10))
        pygame.draw.rect(self.screen, self.GREEN, (400, 695, self.lengths[4], 10))

    def reset_lengths(self):
        """Reset the lengths of the rectangle"""
        self.lengths = [320, 320, 320, 320, 320]

    def increase_difficulty(self):
        """Increase the difficulty as the game progresses"""
        self.difficulty = [x + self.difficulty_level for x in self.difficulty]

    def reset_difficulty(self):
        self.difficulty = self.difficulty_copy
