from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    console = Console()
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22",
               "2022-23", "2023-24", "2024-25", "2025-26"]
    nationalities = ["USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO",
                     "FRA", "GBR", "SVK", "DEN", "NED", "AUT", "BLR",
                    "GER", "SUI", "NOR", "UZB", "LAT", "AUS"]
    season = Prompt.ask("Season", choices=seasons, default="2024-25")

    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = Prompt.ask("Nationality", choices=nationalities)
        players = stats.top_scorers_by_nationality(nationality)
        table = Table(title=f"Season {season} players form {nationality}")

        table.add_column("Released")
        table.add_column("Teams")
        table.add_column("goals", justify="right")
        table.add_column("assists", justify="right")
        table.add_column("points", justify="right")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals),
                          str(player.assists), str(player.points()))

        console.print(table)

if __name__ == "__main__":
    main()
