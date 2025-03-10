class Stats:
    def __init__(self):
        self.__hits = 0
        self.__misses = 0
        self.__damage_done = 0
        self.__damage_taken = 0
        self.__criticalHits = 0
    
    @property
    def hits(self):
        return self.__hits

    @hits.setter
    def hits(self, value):
        self.__hits += value
    
#output from mainloop = result
#
#format result into stats
#stats new instance of the class every round
#instances in array
#print array and user chooses
#print info about the round of choice
