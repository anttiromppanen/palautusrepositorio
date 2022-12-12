from matchers import And, All, Or, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self):
        self.rakentaja = QueryPino()

    def playsIn(self, team):
        self.rakentaja.lisaa(PlaysIn(team))
        return self

    def hasAtLeast(self, amount, attr):
        self.rakentaja.lisaa(HasAtLeast(amount, attr))
        return self

    def hasFewerThan(self, amount, attr):
        self.rakentaja.lisaa(HasFewerThan(amount, attr))
        return self

    def oneOf(self, *matchers):
        self.rakentaja.lisaa(Or(*matchers))
        return self

    def build(self):
        self.rakentaja.lisaa(All())
        return And(*self.rakentaja.kayta_argumentit())

class QueryPino:
    def __init__(self):
        self.pino = []

    def lisaa(self, arg):
        self.pino.append(arg)
    
    def kayta_argumentit(self):
        palautettava_pino = self.pino
        self.pino = []
        return palautettava_pino