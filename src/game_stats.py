class GameStats:
    """Track the game statistics"""
    def __init__(self, ai_game, high_score):
        """Initialize Statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the game in an inactive state.
        self.game_active = False
        # High score should never be reset.
        self.high_score = high_score

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.score = 0
        self.level = 1
