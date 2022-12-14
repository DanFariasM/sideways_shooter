class Settings:
    """A class to store all settings for Sideways Shooter."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        self.difficulty_level = "Normal"

        # How quickly the game speeds up.
        self.speedup_scale = 1.1

        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        if self.difficulty_level == "Normal":
            self.ship_limit = 3
            self.ship_speed = 1.5
            self.bullet_speed = 1.0
            self.alien_speed = 1.0
            self.alien_points = 50
        elif self.difficulty_level == "Easy":
            self.ship_limit = 5
            self.ship_speed = 0.75
            self.bullet_speed = 0.5
            self.alien_speed = 0.5
            self.alien_points = 10
        elif self.difficulty_level == "Hard":
            self.ship_limit = 2
            self.ship_speed = 3.0
            self.bullet_speed = 2.0
            self.alien_speed = 2.0
            self.alien_points = 150

        # Fleet direction of 1 represents down, -1 represents up.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
