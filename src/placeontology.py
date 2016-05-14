

class ontology:
    def __init__(self) :
        #####depth=1#####
        self.root = ['dweller', 'time', 'space', 'activity', 'opinion']

        #####depth=2#####
        self.dweller = ['who', 'with']
        self.time = ['timestamp', 'year', 'month', 'day', 'hour', 'minute', 'seconds', 'Weekday', 'isWeekend', 'isHoliday', ]
        self.space = ['traffic', 'weather', 'temperature']
        self.activity = ['what', 'activity']
        self.opinion = ['mood']
        
        #####depth=3#####
    