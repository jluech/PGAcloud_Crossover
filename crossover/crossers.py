import logging
import random
from abc import ABC, abstractmethod
from enum import Enum

from population.individual import Individual


class Crossers(Enum):
    OnePoint = "one_point",
    MultiPoint = "multi_point",
    Uniform = "uniform",


class AbstractCrossover(ABC):
    @ abstractmethod
    def perform_crossover(self, individual1, individual2, crossover_rate):
        # Perform the crossover on two Individual's.
        # Returns a Pair of two Individual's.
        pass


class OnePointCrossover(AbstractCrossover):
    def perform_crossover(self, individual1, individual2, crossover_rate):
        crossover_chance = random.randint(0, 100) / 100
        # logging.info("Crossover chance = " + str(crossover_chance))
        crossover_occurred = (crossover_rate >= crossover_chance)

        if crossover_occurred:
            solution_length = individual1.solution.__len__()
            if solution_length != individual2.solution.__len__():
                raise Exception("Crossover aborted: Individuals' solution strings are of different length!")

            logging.info("Crossover occurred between individuals {ind1_}  and  {ind2_}.".format(
                ind1_=individual1,
                ind2_=individual2,
            ))
            crossover_point = random.randint(1, solution_length-1)
            crossed1 = Individual("{ind1_}{ind2_}".format(
                ind1_=individual1.solution[:crossover_point],  # first part of 1
                ind2_=individual2.solution[crossover_point:],  # second part of 2
            ))
            crossed2 = Individual("{ind2_}{ind1_}".format(
                ind2_=individual2.solution[:crossover_point],  # first part of 2
                ind1_=individual1.solution[crossover_point:],  # second part of 1
            ))
            return [crossed1, crossed2]
        else:
            logging.info("Crossover did not occur between individuals {ind1_}  and  {ind2_}.".format(
                ind1_=individual1,
                ind2_=individual2,
            ))
            return [individual1, individual2]


class MultiPointCrossover(AbstractCrossover):
    def perform_crossover(self, individual1, individual2, crossover_rate):
        pass


class UniformCrossover(AbstractCrossover):
    def perform_crossover(self, individual1, individual2, crossover_rate):
        pass
