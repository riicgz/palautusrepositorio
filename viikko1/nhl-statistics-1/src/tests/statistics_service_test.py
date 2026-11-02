import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_team_palauttaa_oikean_joukkueen(self):
        players = self.stats.team("PIT")

        self.assertEqual(len(players), 1)

    def test_team_tuntematon_joukkue(self):
        players = self.stats.team("ABC")

        self.assertEqual(len(players), 0)

    def test_search_loytaa_pelaajan(self):
        player = self.stats.search("Lemieux")

        self.assertEqual(player.name, "Lemieux")

    def test_search_loytaa_pelaajan_osittaisella_nimella(self):
        player = self.stats.search("Lemi")

        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")

    def test_search_palauttaa_none_jos_pelaajaa_ei_loydy(self):
        player = self.stats.search("Kane")

        self.assertIsNone(player)

    def test_top_nollalla(self):
        players = self.stats.top(0)

        self.assertEqual(len(players), 1)
        self.assertEqual(players[0].name, "Gretzky")

    def test_top_liian_suuri_maara(self):
        with self.assertRaises(IndexError):
            self.stats.top(10)

    def test_top_palauttaa_parhaat_pelaajat(self):
        players = self.stats.top(2)

        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")