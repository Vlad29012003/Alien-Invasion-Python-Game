import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and str its starting location"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect.
        self.image = pygame.image.load('images/ships.png')
        self.rect = self.image.get_rect()

        #Start each new ship at the botton center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Movement flag
        self.moving_right = False

    def update(self):
        """Update the ship position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the ship at it current location"""
        self.screen.blit(self.image, self.rect)