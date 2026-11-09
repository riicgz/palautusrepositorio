# pylint: disable=too-few-public-methods
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        filtered_players = [player for player in players if player.nationality == nationality]

        filtered_players.sort(key=lambda player: player.points(), reverse=True)
        return filtered_players

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
            maalimäärän mukaan laskevassa järjestyksessä"""
        players = self.reader.get_players()

        players.sort(key=lambda player: player.goals, reverse=True)
        return players[:how_many]

    def top_scorers_by_team(self, team):
        """Palauttaa annetun joukkueen pelaajat
            pisteiden mukaan laskevassa järjestyksessä"""
        players = self.reader.get_players()
        team_players = [player for player in players if player.team == team]

        team_players.sort(key=lambda player: player.points(), reverse=True)
        return team_players
