import random
from abc import ABC, abstractmethod

from population.individual import Individual
from population.pair import Pair


class AbstractCrossover(ABC):
    @ abstractmethod
    def perform_crossover(self, individual1, individual2, crossover_rate):
        # Perform the crossover on two Individual's.
        # Returns a Pair of two Individual's.
        pass


class OnePointCrossover(AbstractCrossover):
    def perform_crossover(self, individual1, individual2, crossover_rate):
        solution_length = individual1.solution.__len__()
        if solution_length != individual2.solution.__len__():
            raise Exception("Crossover aborted: individuals solution strings are of different length!")

        crossover_point = random.randint(1, solution_length-1)
        crossed1 = Individual("{ind1_}{ind2_}".format(
            ind1_=individual1.solution[:crossover_point],  # first part of 1
            ind2_=individual2.solution[crossover_point:],  # second part of 2
        ))
        crossed2 = Individual("{ind2_}{ind1_}".format(
            ind2_=individual2.solution[:crossover_point],  # first part of 2
            ind1_=individual1.solution[crossover_point:],  # second part of 1
        ))
        return Pair(crossed1, crossed2)


class MultiPointCrossover(AbstractCrossover):
    def perform_crossover(self, individual1, individual2, crossover_rate):
        pass


class UniformCrossover(AbstractCrossover):
    def perform_crossover(self, individual1, individual2, crossover_rate):
        pass
