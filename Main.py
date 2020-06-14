import matplotlib.pyplot as plt
import random


class die:
    start = 1
    stop = 6

    def __init__(self, sta, sto):
        if sta > sto:
            raise Exception("Start is greater than stop")

        self.start = sta
        self.stop = sto

    def roll(self):
        return random.randint(self.start, self.stop)

class multiroll:
    dice = []

    start = 1
    stop = 6
    numDice = 0
    numKeep = -1
    keepHighest = True
    addition = 0


    def __init__(self, start, stop, numD, numK = -1, keepH = True, addition = 0):
        self.start = start
        self.stop = stop
        self.numDice = numD
        self.numKeep = numD if numK == -1 else numK
        self.keepHighest = keepH
        self.addition = addition
        for i in range(self.numDice):
            self.dice.append(die(start, stop))

    def roll(self):
        rolls = []
        for die in self.dice:
            rolls.append(die.roll() + self.addition)

        rolls.sort(reverse = self.keepHighest)

        return rolls[:self.numKeep]

    def minRoll(self):
        return self.numKeep * (self.start + self.addition)

    def maxRoll(self):
        return self.numKeep * (self.stop + self.addition)






random.seed()



numRolls = 100000



mroll = multiroll(1, 6, 5, numK = 3, keepH = True, addition = 0)

totalRolls = {}
for i in range(mroll.minRoll(), mroll.maxRoll() + 1):
    totalRolls[i] = 0

for i in range(numRolls):
    totalRolls[sum(mroll.roll())] += 1

averageRoll = 0
for key, value in totalRolls.items():
    averageRoll += key * value

averageRoll /= numRolls

print('Average roll: ' + str(averageRoll))

percentageRolls = {}
for key, value in totalRolls.items():
    percentageRolls[key] = value / numRolls

plt.bar(range(len(percentageRolls)), list(percentageRolls.values()), align='center')
plt.xticks(range(len(percentageRolls)), list(percentageRolls.keys()))
plt.show()


