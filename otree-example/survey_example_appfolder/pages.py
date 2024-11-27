from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player

#This is the pages.py file. Here we structure how our pages and pagesequence function.
#Each page has its own class where you always specify form_model = Player as we have players for each page
#and we have the form_fields in a list which indicate the variables we have on that page. There will be
#more functionality added here but this is a good start. 

class Welcome(Page):
    form_model = Player
    form_fields = ['screen_height', 'screen_width']

class DemoPage(Page):
    form_model = Player
    form_fields = ['numeric_question', 
                   'float_question' , 
                   'opentext_question', 
                   'mc_question', 
                   'yes_no_question']

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
        '''this is another function by otree which allows you to "send" variables
        to html files if you need to access them from there'''
        return {"group_assignment": safe_json(self.player.group_assignment)}

#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                DemoPage,
                DemoPage4_group1,
                DemoPage4_group2, 
                PopupQuestion,             
                EndPage]