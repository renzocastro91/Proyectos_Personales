class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def add_score(self, points):
        self.score += points
    
    def get_score(self):
        return self.score


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.game_over = False
    
    def add_score(self, player):
        if self.game_over:
            return
        
        if player == self.player1:
            other_player = self.player2
        else:
            other_player = self.player1
        
        if player.get_score() == 40 and other_player.get_score() < 40:
            # player wins the game
            self.game_over = True
        elif player.get_score() == 40 and other_player.get_score() == 40:
            # deuce
            player.add_score(10)
        elif player.get_score() == 50 and other_player.get_score() == 40:
            # player wins the game after advantage
            self.game_over = True
        else:
            player.add_score(15)
    
    def get_winner(self):
        if self.player1.get_score() > self.player2.get_score():
            return self.player1
        elif self.player2.get_score() > self.player1.get_score():
            return self.player2
        else:
            return None
    
    
class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.games_player1 = 0
        self.games_player2 = 0
        self.match_over = False
    
    def add_score(self, player):
        if self.match_over:
            return
        
        if player == self.player1:
            other_player = self.player2
        else:
            other_player = self.player1
        
        game = Game(player, other_player)
        while not game.game_over:
            game.add_score(player)
        winner = game.get_winner()
        if winner == self.player1:
            self.games_player1 += 1
        elif winner == self.player2:
            self.games_player2 += 1
        
        if self.games_player1 >= 3 and self.games_player1 >= self.games_player2 + 2:
            self.match_over = True
        elif self.games_player2 >= 3 and self.games_player2 >= self.games_player1 + 2:
            self.match_over = True
    
    def get_winner(self):
        if self.games_player1 > self.games_player2:
            return self.player1
        elif self.games_player2 > self.games_player1:
            return self.player2
        else:
            return None
    
    def get_score(self):
        return f"{self.player1.get_score()}-{self.player2.get_score()} {self.games_player1}-{self.games_player2}"
