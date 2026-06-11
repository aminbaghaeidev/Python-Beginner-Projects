class Score:
    def __init__(self):
        self.score = 100

    def reduce_score(self, penalty=10):
        """Decrease the score from 100 to 0 (if user try all the chances)"""
        self.score -= penalty
        self.score = max(self.score, 0)

    def show_score(self):
        """Will show the score"""
        return f"Score: {self.score}"