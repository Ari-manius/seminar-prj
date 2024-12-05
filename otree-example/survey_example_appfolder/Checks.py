import random

def random_number(x, y):
    '''
    method for random integers
    '''  
    rng = random.Random()
    number = rng.randint(x, y)
    return number

#screenout for everyone older than 40
def screenout_check(self):
    if self.player.age > 40:
        self.player.screenout = 1

#screenout if quota is already full 
def quota_check(self):
    #acces gender quotas dict
    gender_quotas = self.session.vars['gender_quotas']

    #store the selected gender 
    selected_gender = self.player.gender

    #if quota is full set boolean quota to 1
    if gender_quotas[selected_gender] >= 1:
        self.player.quota = 1  
    #if quota is not full increase the counter in the dict by the gender selected 
    else:
        gender_quotas[selected_gender] += 1