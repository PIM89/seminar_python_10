class MinStat:
    def __init__(self):
        self.res_listt = []

    def add_number(self, elem):
        self.res_listt.append(elem)
        return self.res_listt
    
    def result(self):
        try: return min(self.res_listt)
        except: return None

class MaxStat:
    def __init__(self):
        self.res_listt = []

    def add_number(self, elem):
        self.res_listt.append(elem)
        return self.res_listt
    
    def result(self):
        try: return max(self.res_listt)
        except: return None

class AverageStat:
    def __init__(self):
        self.res_listt = []

    def add_number(self, elem):
        self.res_listt.append(elem)
        return self.res_listt
    
    def result(self):
        try: return sum(self.res_listt)/len(self.res_listt)
        except: return None


# Пример 1.
# values = [1, 2, 4, 5]
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

# Пример 2.
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# print(mins.result(), maxs.result(), average.result())

# Пример 3.
# values = [1, 0, 0]
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))