import math
import json
from Emotions import Emotions
from GaiaB import Singleton

emote = Emotions()


class ThingsToDo(Singleton):
    def __init__(self):
        self.dailysdone = 0
        self.monthlysdone = 0
        self.yearlysdone = 0
        pass

    def readdailysdone(self):
        return self.dailysdone

    def readmonthlysdone(self):
        return self.monthlysdone


class DailyGoals(ThingsToDo):
    def __init__(self):
        super(DailyGoals, self).__init__()

    def dailygoalcompleted(self, points):
        """
        :param points: reward for completed or failure to complete exp 1 for good or -1 for bad
        :return:
        """
        if points >= 0:
            self.dailysdone = self.dailysdone + 1
            if emote.readhappysad() >= 90 and emote.readcalmmad() >= 90:
                pass
            elif emote.readcalmmad() <= 50:
                emote.makehappysad(points)
            else:
                emote.makehappysad(points)
                emote.makecalmmad(points)
        elif points <= 0:
            if emote.readhappysad() <= 10 and emote.readcalmmad() <= 10:
                pass
            elif emote.readhappysad() <= 10:
                emote.makecalmmad(points)
            else:
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
