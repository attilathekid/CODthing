from random import shuffle
import matplotlib.pyplot as plt


class Player:
    alive = []

    def __init__(self):
        self.id = len(Player.alive)
        self.kills = 0
        Player.alive.append(self)


class Sim:
    def __init__(self, players):
        self.turns = 0
        self.all = [Player() for _ in range(players)]
        self.dist = None

    def turn(self):
        self.turns += 1
        shuffle(Player.alive)
        Player.alive[0].kills += 1
        del Player.alive[1]

    def run(self):
        while len(Player.alive) > 1:
            self.turn()

    def get_dist(self, destination='print'):
        plt.hist([x.kills for x in self.all])
        plt.title('Distribution of Kills')
        plt.xlabel('Kills Achieved')
        plt.ylabel('Number of Players')
        if destination=='print':
            plt.show()
        else:
            plt.savefig(destination)

