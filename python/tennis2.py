# -*- coding: utf-8 -*-

class TennisGame2:
    __score_names = ("Love", "Fifteen", "Thirty", "Forty")
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def gameOver(self) -> str:
        difference = self.p1points-self.p2points
        if difference >= 2: 
            return f"Win for {self.player1Name}"
        elif difference <= -2: 
            return f"Win for {self.player2Name}"
        
    def lowScores(self):
        P1res = self.__score_names[self.p1points]
        P2res = self.__score_names[self.p2points]
        return P1res + "-" + P2res
    
    def equalScores(self):
        return "Deuce" if (self.p1points > 2) else self.__score_names[self.p1points] + "-All"
    
    def playerAdvantage(self, playername):
        return f"Advantage {playername}"
    
    def score(self):
        if self.p1points>=4 or self.p2points >= 4:
            result = self.gameOver()
            if result != None: 
                return result
            
        result = ""
        
        if (self.p1points < 4 and self.p2points < 4):
            result = self.lowScores()
        
        if self.p1points == self.p2points:
            result = self.equalScores()

        if (self.p1points > self.p2points and self.p2points >= 3):
            result = self.playerAdvantage(self.player1Name)

        if (self.p2points > self.p1points and self.p1points >= 3):
            result = self.playerAdvantage(self.player2Name)
            
        return result

    def P1Score(self):
        self.p1points +=1

    def P2Score(self):
        self.p2points +=1
