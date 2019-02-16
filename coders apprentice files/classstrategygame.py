#Iterated Prisoner's Dilemna game demonstrating inheriting from class
#created by ikon beth from coders' apprentice
#DevCUyo100DaysOfCode

COOPERATE = "C"
DEFECT = "D"
ROUNDS = 100

class Strategy():
    def __init__(self, name = ""):
        self.name = name
        self.score = 0

    def choice(self):
        #should return DEFECT OR COOPERATE
        return NotImplemented
    def lastmove(self, mymove, opponentmove):
        #Gets passed the last move made, after a call of Choice()
        pass
    def incscore(self, n):
        self.score += n
strategy1 = Strategy()
strategy2 = Strategy()

for i in range(ROUNDS):
    c1 = strategy1.choice()
    c2 = strategy2.choice()
    if c1 == c2:
        strategy1.incscore(3 if c1 == COOPERATE else 1)
        strategy2.incscore(3 if c2 == COOPERATE else 1)
    else:
        strategy1.incscore(0 if c1 == COOPERATE else 6)
        strategy2.incscore(0 if c2 == COOPERATE else 6)
    strategy1.lastmove(c1,c2)
    strategy2.lastmove(c2,c1)

print("End score of ", strategy1.name, " is ", strategy1.score)
print("End score of ", strategy2.name, " is ", strategy2.score)

input("Exit:")
