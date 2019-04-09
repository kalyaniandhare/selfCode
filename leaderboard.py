class LeaderBorad():
    """
    This class perform stack operation.
    """

    def calculate_minute_data(self):

        if len(self.name_list):
            minute = self.get_data[self.name_list[0]]['minute']
        else:
            return -1
            
        first_name = ''
        for name in self.name_list:
            if minute >= self.get_data[name]['minute']:
                minute = self.get_data[name]['minute']
                first_name = name

        if first_name:
            del self.get_data[first_name]
            self.name_list.remove(first_name)
        return first_name if first_name else -1

    def calculate_score_data(self):

        score = 0
        first_name = ''
        for name in self.name_list:
            
            if score < self.get_data[name]['score']:
                score = self.get_data[name]['score']
                first_name = name

        if first_name:
            del self.get_data[first_name]
            self.name_list.remove(first_name)
        return first_name if first_name else -1

    
    def calculate_data(self):
        final_list = []
        for d in range(0, len(self.name_list)):
            name = self.calculate_score_data()
            mname = self.calculate_minute_data()
            final_list.append(name)
            final_list.append(mname)


        for i in range(0, len(self.score)):
            if -1 in final_list:
                final_list.remove(-1) 

        print(final_list)
        
    def __init__(self):
        self.get_data = {}
        #no_of_input = raw_input().strip().split(' ')
        no_of_input = raw_input()
        self.name_list = []
        self.score = []
        for i in range(0, int(no_of_input)):
            name, minute = raw_input().strip().split(' ')
            if name not in self.get_data.keys():
                self.name_list.append(name)
                self.score.append(name)
                self.get_data[name] = {'minute': int(minute), 'score': 100}
                #get_data['score'] = 100 
            else:
                self.get_data[name]['minute'] += int(minute)
                self.get_data[name]['score'] += 100


        self.calculate_data()

        
LeaderBorad()
