import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ss_game):
        """Initialize statistics."""
        self.settings = ss_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # High score should never be reset.
        self.retrieve_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Creating / updating a file with the all time high score."""
        filename = "high_score.json"
        with open (filename, "w") as hs_file_object:
            json.dump(self.high_score, hs_file_object)

    def retrieve_high_score(self):
        """Retrieving the all time high score, except for 1st time players.
        1st time players will start with a 0 high score."""
        try:
            filename = "high_score.json"
            with open(filename) as hs_file_object:
                self.high_score = json.load(hs_file_object)
        except FileNotFoundError:
            self.high_score = 0

