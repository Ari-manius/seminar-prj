from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player

from survey_example_appfolder.Checks import screenout_check, quota_check

class Welcome(Page):
    form_model = Player
    form_fields = ['screen_height', 'screen_width']

class DemoPage(Page):
    form_model = Player
    form_fields = ['age' ,'gender']
    
    def before_next_page(self):
        self.group.counter += 1
        screenout_check(self)
        quota_check(self)
        self.player.participant_label = self.participant.label

class DemoPage1(Page):
    form_model = Player
    form_fields = []

    def vars_for_template(self):
        return {'participant_label': safe_json(self.participant.label),
                'screenout': safe_json(self.player.screenout),
                'quota': safe_json(self.player.quota)
                }

class DemoPage4_group1(Page):
    def is_displayed(self):
        return self.player.group_assignment == 0
    form_model = Player
    form_fields = ["goose"]

class DemoPage4_group2(Page):
    def is_displayed(self):
        return self.player.group_assignment == 1
    form_model = Player 
    form_fields = ["duck"]

class PopupQuestion(Page):
    form_model = Player
    form_fields = ['popout_question', 'popout_yes', 'popout_no', 'time_popout']

class EndPage(Page):
    #style: this is a good example of the style 'CamelCase' that one normally uses for classes
    form_model = Player
    def vars_for_template(self):
        return {"group_assignment": safe_json(self.player.group_assignment),
                'participant_label': safe_json(self.participant.label)
                }

#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                DemoPage,
                DemoPage1,
                DemoPage4_group1,
                DemoPage4_group2, 
                PopupQuestion,             
                EndPage]