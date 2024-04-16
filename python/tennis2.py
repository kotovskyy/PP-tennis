class TennisGame2:
    """
    Represents a tennis game between two players.
    """
    __score_names = ("Love", "Fifteen", "Thirty", "Forty")

    def __init__(self, player1Name, player2Name) -> None:
        """
        Initializes a new instance of the TennisGame2 class.

        #### Args:
            - `player1Name: str` -  The name of `player1`.
            - `player2Name: str` - The name of `player 2`.
        """
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1points = 0
        self.player2points = 0

    def P1Score(self) -> None:
        """
        Increases the score of `player1` by 1.
        """
        self.player1points += 1

    def P2Score(self) -> None:
        """
        Increases the score of `player2` by 1.
        """
        self.player2points += 1

    def won_point(self, playerName) -> None:
        """
        Updates the score based on the player who won the point.

        #### Args:
            - `playerName: str` - The name of the player who won the point.
        """
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def isGameOver(self) -> str | None:
        """
        Checks if the game is over and returns the winner's name.

        #### Returns:
            - `str` - The name of the winner if the game is over, otherwise None.
        """
        difference = self.player1points - self.player2points
        if difference >= 2:
            return f"Win for {self.player1Name}"
        elif difference <= -2:
            return f"Win for {self.player2Name}"

    def lowScores(self) -> str:
        """
        Returns the score when both players have less than 4 points.

        #### Returns:
            - `str` - The score in the format "Player1Score-Player2Score".
        """
        P1res = self.__score_names[self.player1points]
        P2res = self.__score_names[self.player2points]
        return P1res + "-" + P2res

    def equalScores(self) -> str:
        """
        Returns the score when both players have equal points.

        #### Returns:
            - `str` - The score in the format "Player1Score-All" or "Deuce".
        """
        return "Deuce" if (self.player1points > 2) else self.__score_names[self.player1points] + "-All"

    def playerAdvantage(self, difference) -> str:
        """
        Returns the score when one player has an advantage over the other.

        #### Args:
            - `difference: int` - The difference in points between the players.

        #### Returns:
            - `str` - The score in the format "Advantage PlayerName".
        """
        playername = self.player1Name if difference >= 0 else self.player2Name
        return f"Advantage {playername}"

    def score(self) -> str:
        """
        Returns the current score of the game.

        #### Returns:
            - `str` - The current score of the game.
        """
        if self.player1points >= 4 or self.player2points >= 4:
            result = self.isGameOver()
            if result != None:
                return result

        if self.player1points == self.player2points:
            return self.equalScores()
        elif self.player1points < 4 and self.player2points < 4:
            return self.lowScores()
        elif self.player1points >= 3 or self.player2points >= 3:
            return self.playerAdvantage(self.player1points - self.player2points)
