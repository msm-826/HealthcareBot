import random


class DataOut:

    def __init__(self) -> None:
        self.mayCall = ['Should I call the doctor?', 'Oh! May I call the doctor?', 'Do I want to call the doctor?', 'It\'s better to contact the doctor. May I?']
        self.howHelp = ['How may I help you sir?', 'At your service sir.', 'What are the help you needed sir?', 'What can i do for you?', 'How may I be of assistance']
        self.greetings = ['Greetings', 'Howdy', 'Hey Whats Up', 'Hey Am Here']
        self.more = ['Don\'t got hold of it. Can you describe again?', 'I don\'t get what you are trying to countinue. Can you please describe it once more.', 'Sorry! I don\'t get it!', 'Can you please repeat. Thank you!']



    def getMayCall(self):
        return random.choice(self.mayCall)
    
    def getHowHelp(self):
        return random.choice(self.howHelp)
    
    def getGreetings(self):
        return random.choice(self.greetings)
    
    def getMore(self):
        return random.choice(self.more)