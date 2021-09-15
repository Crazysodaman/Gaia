import math
from Emotions import Emotions
from GaiaB import Singleton

emote = Emotions()


class ThingsToDo(Singleton):
    def __init__(self):
        self.dailysdone = 0
        self.monthlysdone = 0
        pass


class DailyGoals(ThingsToDo):
    def __init__(self):
        super(DailyGoals, self).__init__()

    def dailygoalcompleted(self, points):
        """
        :param points: reward for completed or failure to complete (1 or -1)
        :return:
        """
        emote.makehappysad(points)


class MonthlyGoals(ThingsToDo):
    def __init__(self):
        super(MonthlyGoals, self).__init__()


class YearlyGoals(ThingsToDo):
    def __init__(self):
        super(YearlyGoals, self).__init__()
    # TODO


if __name__ == '__main__':
    pass
