import random

from otree.api import (
    BaseConstants,
    BaseGroup,
    BasePlayer,
    BaseSubsession,
    Page,
    WaitPage,
    models,
)

doc = """
An encoding task made by me
"""

class C(BaseConstants):
    NAME_IN_URL = "encode"
    PLAYERS_PER_GROUP = 1
    NUM_ROUNDS = 1
    ENDOWMENT = 1
    PRIZE = 2
    COST_PER_TICKET = {1: 1, 2: 1}

class Subsession(BaseSubsession):
    is_paid = models.BooleanField()

    def setup(self):
        self.is_paid = (self.round_number == 1)
        self.group_randomly()
        for group in self.get_groups():
            group.setup()

class Player(BasePlayer):
    endowment = models.IntegerField()
    cost_per_ticket = models.IntegerField()
    tickets_purchased = models.IntegerField()    is_winner = models.BooleanField()
    earnings = models.IntegerField()

    def setup(self):
        self.endowment = C.ENDOWMENT
        self.cost_per_ticket = C.COST_PER_TICKET[self.id_in_group]

# PAGES
class Intro(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

