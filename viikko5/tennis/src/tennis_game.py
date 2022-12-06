class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score = ""
        temporary_score = 0

        if self.player1_score == self.player2_score:
            score = self.draw(score)
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.player_points_over_four(score)
        else:
            score, temporary_score = self.print_points(score, temporary_score)

        return score

    def draw(self, score):
        if self.player1_score == 0:
            score = "Love-All"
        elif self.player1_score == 1:
            score = "Fifteen-All"
        elif self.player1_score == 2:
            score = "Thirty-All"
        elif self.player1_score == 3:
            score = "Forty-All"
        else:
            score = "Deuce"
        
        return score
    
    def player_points_over_four(self, score):
        minus_result = self.player1_score - self.player2_score

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        
        return score
    
    def print_points(self, score, temporary_score):
        for i in range(1, 3):
            if i == 1:
                temporary_score = self.player1_score
            else:
                score = score + "-"
                temporary_score = self.player2_score

            if temporary_score == 0:
                score = score + "Love"
            elif temporary_score == 1:
                score = score + "Fifteen"
            elif temporary_score == 2:
                score = score + "Thirty"
            elif temporary_score == 3:
                score = score + "Forty"
        
        return (score, temporary_score)