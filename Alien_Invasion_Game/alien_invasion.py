# Install Pygame
# py -3.7 -m pip install pygame

# Remove errors of pylint not finding the pygame modules
# "python.linting.pylintArgs": [
#     "--extension-pkg-whitelist=pygame"
# ]

import sys

import pygame
from pygame.sprite import Group

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

    # Make a ship.
    ship = Ships(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    running = True

    while running:
        # Watch for keyboard and mouse events.
        running = gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        
        # Update Screen
        gf.update_screen(ai_settings, screen, ship, bullets)

    pygame.quit()

run_game()