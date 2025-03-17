class Stats:
    def __init__(self):
        self.__hits = 0
        self.__misses = 0
        self.__damage_done = 0
        self.__damage_taken = 0
        self.__critical_hits = 0
        self.__damage_blocked = 0
    
    @property
    def hits(self):
        return self.__hits

    @hits.setter
    def hits(self, value):
        self.__hits = value

    @property
    def misses(self):
        return self.__misses

    @misses.setter
    def misses(self, value):
        self.__misses = value

    @property
    def damage_done(self):
        return self.__damage_done

    @damage_done.setter
    def damage_done(self, value):
        self.__damage_done = value

    @property
    def damage_taken(self):
        return self.__damage_taken

    @damage_taken.setter
    def damage_taken(self, value):
        self.__damage_taken = value

    @property
    def critical_hits(self):
        return self.__critical_hits

    @critical_hits.setter
    def critical_hits(self, value):
        self.__critical_hits = value
    
    @property
    def damage_blocked(self):
        return self.__damage_blocked

    @damage_blocked.setter
    def damage_blocked(self, value):
        self.__damage_blocked = value
    
    
#output from mainloop = result
#
#format result into stats
#stats new instance of the class every round
#instances in array
#print array and user chooses
#print info about the round of choice
