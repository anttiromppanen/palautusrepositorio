from player_reader import PlayerReader
from sort_by import SortBy

def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists

def sort_selection(order_by):
    if (order_by == SortBy.GOALS): return sort_by_goals
    if (order_by == SortBy.ASSISTS): return sort_by_assists
    return sort_by_points

class Statistics:
    def __init__(self, reader):
        self.reader = reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by = SortBy.POINTS):
        selection = sort_selection(sort_by)

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=selection
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
