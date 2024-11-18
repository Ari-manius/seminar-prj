from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Me'
doc = 'Test Survey for Seminar'

class Constants(BaseConstants):
    name_in_url = 'survey-test-seminar'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    #we will only come to the group class when we look at advanced methods
    pass


class Player(BasePlayer):

    numeric_question = models.IntegerField()

    float_question = models.FloatField()

    opentext_question = models.TextField()
    
    mc_question = models.CharField(
        choices=(
            ('A', 'First Option'),
            ('B', 'Second Option'),
            ('C', 'Third Option'),
            ('D', 'Fourth Option'),
        ),
        default='A',  # Default option, if applicable
    )

    yes_no_question = models.BooleanField(default=False)
