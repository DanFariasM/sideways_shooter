import pygame

class Ship:
    """a class to manage the ship."""

    def __init__(self, ss_game):
        """Initialize the ship and set its starting position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the left of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's vertical postion.
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's y value, not the rect.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update rect object from self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
