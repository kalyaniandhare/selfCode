

class RestaurantSeatingArrangment:
    def __init__(self):
        
        print("No of table")
        no_of_table = int(input())
        print("Enter seats")
        no_of_seats_per_table = input()
        
        for i in no_of_seats_per_table:
            print(i, type(i))

        print("No of seats requested")
        no_of_seats_requested = int(input())
        print("Should they be in the same table: Say Y/N")
        same_table = raw_input()
        table_index = self.getRequestedSeatsForTable(no_of_seats_requested, same_table, no_of_seats_per_table)
        print(table_index, "!!!!!!!!!!!!")
        if table_index == -1:
            print("Not Possible")
        else:
            print("Table", table_index)

        def calculate(table, seats):
            get_list = []
            for i, val in enumerate(table):
                if val < seats:
                    get_list.append(val)
            

        def calculate_split_table_seats(self, table, seats):
            
            if seats > sum(table):
                return -1
            if len(table) <= 2 and seats < sum(table):
                print("Table 1, 2")
            else:
                if max(table) > seats:
                    return table.index(max(table))
                else:
                    #calculate(table, seats)

                
                
        def calculate_table_seats(self, table, seats):
            get_table_list = {}
            if seats > sum(table):
                return -1
            for i, val in enumerate(table):
                if val == seats:
                    print(val, seats)
                    return i
                if val > seats:
                    print(val, seats)
                    get_table_list[val] = i
            a = get_table_list[min(get_table_list)]
            return int(a)

        def getRequestedSeatsForTable(self, no_of_seats_requested, same_table, no_of_seats_per_table):
            if same_table == 'Y':
                return self.calculate_table_seats(no_of_seats_per_table, no_of_seats_requested)
            if same_table == 'N':
                self.calculate_split_table_seats(no_of_seats_per_table, no_of_seats_requested)
