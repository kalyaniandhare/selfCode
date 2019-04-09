import os, resource, sys

sys.setrecursionlimit(1000000000)
#os.system('ulimit -s unlimited; Dollar()')
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))


class Dollar():

    def get_data(self, value, amount):
        for i in range(0, value):
            if self.dollar >= self.final_value:
                return self.dollar, self.no_of_month 
            else:
                self.dollar += amount
                self.no_of_month += 1
        return self.dollar, self.no_of_month

    def get_final_value(self):
        self.dollar, self.no_of_month = self.get_data(self.month, self.amount_A)
        if self.dollar >= self.final_value:
            return self.no_of_month, self.dollar
        else:
            self.dollar, self.no_of_month = self.get_data(self.b, self.amount_B)
            self.b += 1
        return self.no_of_month, self.dollar
    
    def calculate(self):
        self.no_of_month, self.dollar = self.get_final_value()
        if self.dollar >= self.final_value:
            return self.no_of_month
        else:
            self.no_of_month = self.calculate()
            
        return self.no_of_month
    
    def get_values(self):
        for input_format in self.input_list:
            self.no_of_month = 0
            dollar, amount_A, month, amount_B, final_value = input_format.split(' ')
            self.dollar, self.amount_A, self.month, self.amount_B, self.final_value = int(dollar), int(amount_A), int(month), int(amount_B), int(final_value)
            no_of_month = self.calculate()
            self.get_ans.append(no_of_month)
    
    def __init__(self):
        self.no_of_test = int(raw_input())
        self.input_list = []
        self.get_ans = []
        self.b = 1
        for i in range(0, self.no_of_test):
            self.input_list.append(raw_input())
        
        self.get_values()
        
        for i in range(0, len(self.get_ans)):
            print(self.get_ans[i])
    


new = Dollar()
