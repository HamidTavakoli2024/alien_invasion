from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never be reset.
        
        self.high_score = 0
        self.level = 1
        self._read_high_score()
 
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        
    
    def _read_high_score(self):
        try:
            self.path = Path('high_score.txt')
            self.high_score = int(self.path.read_text())
        except FileNotFoundError:
            pass