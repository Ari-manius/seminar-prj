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

#import random for group assignment
import random 

author = 'Me'
doc = 'Test Survey for Seminar'

class Constants(BaseConstants):
    name_in_url = 'survey-test-seminar'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
     def creating_session(self):
        for p in self.get_players():
            p.group_assignment = random.Random().randint(0, 1)

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

    group_assignment = models.IntegerField(initial=-1)
    #this is the most important feature of this file. We can collect all the variables used on the html pages here

    duck = models.IntegerField(initial=-999, label="Please select the value that is most fitting:")

    goose = models.IntegerField(initial=-999, label="Please select the value that is most fitting:")

    #varibles for recording of screen width/height
    screen_height = models.IntegerField(initial=-999)
    screen_width = models.IntegerField(initial=-999)

    #Variables for  the popup questions
    popout_question = models.IntegerField(blank=True)
    popout_yes = models.StringField(blank=True)
    popout_no = models.StringField(blank=True)
    time_popout = models.StringField(initial='-999')