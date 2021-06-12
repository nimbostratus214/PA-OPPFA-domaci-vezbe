from enum import Enum


class Community:
    def __init__(self, humans=[], relations={}):
        self.humans = humans
        self.relations = relations


class Infectivity(Enum):
    NotImmune = 0
    Infected = 1
    Immune = 2


class Human:
    """
    Human Node: A graph vertex (node) with data representing the current status of the human and their responsibility
    """

    def __init__(self, name=None, responsibility=None, status=Infectivity.NotImmune, risk_level=None):
        """
        Human constructor
        :param name - Name of the Individual
        :param responsibility - A integer value representing the responsibility of the Individual (Do they wash their
            hands regularly, wear masks and social distance)
        :param status - Current status of the Individual, are they Immune? Not Immune? Infected?
        :param risk_level - highest risk to get infected
        """
        self.name = name
        self.resp = responsibility
        self.status = status
        self.risk = risk_level
        self.source = None  # The person the Individual got the virus from

    def __str__(self):
        return "[ " + str(self.name) + " -> Rizik: " + str(self.risk) + "-> Izvor zaraze: " + str(self.source) + "-> Status: " + str(self.status) + " ->Resp: " + str(self.resp) + " ]"
