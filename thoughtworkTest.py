
class FindTable:

    def __init__(self):
        #print("in find table", self, dir(self))
        return
        
    def find_multiple_table(self):
        if self.seats_requested > sum(self.seats_per_table):
            return -1
        if len(self.seats_per_table) <= 2 and self.seats_requested < sum(self.seats_per_table):
            print("Table 1, 2")
        else:
            if max(self.seats_per_table) > self.seats_requested:
                return self.seats_per_table.index(max(self.seats_per_table))
                
    def find_single_table(self):
        get_table_list = {}
        if self.seats_requested > sum(self.seats_per_table):
            return -1
        else:
            for seat_index, seats in enumerate(self.seats_per_table):
                if seats == self.seats_requested:
                    return seat_index
                if seats > self.seats_requested:
                    get_table_list[seats] = seat_index

            get_index = get_table_list[min(get_table_list)]
            return int(get_index)
    
class GetRequirmentForBookTable:
    def __init__(self):
        print("No of table")
        self.no_of_table = int(input())
        print("Enter seats")
        self.seats_per_table = input()
        print("No of seats requested")
        self.seats_requested = int(input())
        print("Should they be in the same table: Say Y/N")
        self.same_table = raw_input()

class RestaurantSeatingArrangment(GetRequirmentForBookTable, FindTable):
    def __init__(self):
        GetRequirmentForBookTable.__init__(self)
        table_index = self.get_requested_seats_for_table(FindTable)
        if table_index == -1:
            print("Not Possible")
        else:
            print("Table", table_index)

    def get_requested_seats_for_table(self, FindTable):
        if self.same_table == 'Y':
            return FindTable.find_single_table(self)
        if self.same_table == 'N':
            return FindTable.find_multiple_table(self)
        
th = RestaurantSeatingArrangment()
