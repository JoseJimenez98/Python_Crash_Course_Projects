# Install Pygame
# py -3.7 -m pip install pygame

# Remove errors of pylint not finding the pygame modules
# "python.linting.pylintArgs": [
#     "--extension-pkg-whitelist=pygame"
# ]
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ships
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ships(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    running = True

    while running:
        # Watch for keyboard and mouse events.
        running = gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

    pygame.quit()

run_game()