import unittest
from player_stats import PlayerStats

class PlayerStub:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists

    def points(self):
        return self.goals + self.assists

class PlayerReaderStub:
    def get_players(self):
        return [
            PlayerStub("Player A", "FIN", "Team X", 20, 30),
            PlayerStub("Player B", "SWE", "Team Y", 25, 20),
            PlayerStub("Player C", "FIN", "Team X", 15, 25),
            PlayerStub("Player D", "USA", "Team Z", 10, 15),
            PlayerStub("Player E", "FIN", "Team Y", 30, 20),
        ]

class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.reader_stub = PlayerReaderStub()
        self.stats = PlayerStats(self.reader_stub)

    def test_top_scorers_by_nationality(self):
        top_finnish_players = self.stats.top_scorers_by_nationality("FIN")
        self.assertEqual(len(top_finnish_players), 3)
        self.assertEqual(top_finnish_players[0].name, "Player A")
        self.assertEqual(top_finnish_players[1].name, "Player E")
        self.assertEqual(top_finnish_players[2].name, "Player C")


    def test_top_goal_scorers(self):
        top_goal_scorers = self.stats.top_goal_scorers(2)
        self.assertEqual(len(top_goal_scorers), 2)
        self.assertEqual(top_goal_scorers[0].name, "Player E")
        self.assertEqual(top_goal_scorers[1].name, "Player B")

    def test_top_scorers_by_team(self):
        team_x_players = self.stats.top_scorers_by_team("Team X")
        self.assertEqual(len(team_x_players), 2)
        self.assertEqual(team_x_players[0].name, "Player A")
        self.assertEqual(team_x_players[1].name, "Player C")

if __name__ == "__main__":
    unittest.main()
