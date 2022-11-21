import requests
from player import Player


class PlayerReader:
    def __new__(self, url):
        self.url = url
        self.response = requests.get(url).json()
        self.players = self.get_players()

        return self.players

    @classmethod
    def get_players(self):
        players = []

        for player_dict in self.response:
            player = Player(
                player_dict["name"],
                player_dict["team"],
                player_dict["nationality"],
                player_dict["goals"],
                player_dict["assists"]
            )

            players.append(player)

        return players
