class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader

    def top_scorers_by_nationality(self, nationality):
        filtered_players_by_nationality = [
            p for p in self.players if p.nationality == nationality
        ]

        players_sorted = sorted(
            filtered_players_by_nationality,
            key=lambda player: player.get_points(),
            reverse=True
        )

        return players_sorted
