
from CODsim import *
from random import randint


def simple(num):
    sim = Sim(num)
    sim.run()
    sim.get_dist(destination='sampleruns/'+str(num)+'players'+str(randint(1, 10000)))


for i in 2*list(range(2, 5)):
    simple(10**i)
