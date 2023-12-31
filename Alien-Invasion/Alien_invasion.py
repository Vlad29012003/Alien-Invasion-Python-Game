import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assests and behaviors"""

    def __init__(self):
        """Intialize the game, and create game resourses"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)) 
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

        #Set the background color.
        self.bg_color = (230,230,230)

    def run_game(self):
        """Starts the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            #Redraw the screen during each pass through the loop
           
    def _check_events(self):
        """Respond to keypresses and mouse event"""
         # Watch for keyboard and mouse events.
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #Move the ship to the right
                        self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False

    
    def _update_screen(self):
        """update images on the screen, and flip to the new screen"""
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #Make the most recently deawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    #Make a gemw instance, and run the game
    ai = AlienInvasion()
    ai.run_game()