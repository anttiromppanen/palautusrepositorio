from statistics import Statistics
from player_reader import PlayerReader
from sort_by import SortBy

def main():
    stats = Statistics(PlayerReader())
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)

if __name__ == "__main__":
    main()
