from matchers import And, All, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, rakentaja = And()):
        self.rakentaja = rakentaja

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))

    def hasAtLeast(self, amount):
        pass

    def hasFewerThan(self, amount):
        pass

    def build(self):
        return self.rakentaja