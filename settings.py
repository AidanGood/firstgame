'''
Author: Aidan Good
'''


class Settings:
    """Class to manage game settings"""

    def __init__(self):
        # Display settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)  # Black
        # Ship settings
        self.ship_speed = 4
        self.life_limit = 3
        # Rocket settings
        self.rocket_velocity = 0.75
        self.rocket_acceleration = 0.1
        self.rocket_width = 3
        self.rocket_height = 15
        self.rocket_color = (60, 60, 60)
        self.num_rockets = 5
        # Alien settings
        self.alien_velocity = 3
        self.alien_rate = 0.01  # Base: 0.01, anything below 0.05 seems good
        self.num_aliens = 6     # Base: 6, Maximum number of aliens on screen
        # Star settings
        self.star_velocity = 0.5
        self.star_rate = 0.007
