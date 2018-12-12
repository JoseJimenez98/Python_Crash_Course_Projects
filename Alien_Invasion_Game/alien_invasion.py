import sys
import pygame

from settings import Settings
from ship import Ships
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Set the background color.
    bg_color = (230, 230, 230)

    # Make a ship.
    ship = Ships(screen)

    # Start the main loop for the game.
    running = True

    while running:
        
        # Watch for keyboard and mouse events.
        running = gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    pygame.quit()

run_game()