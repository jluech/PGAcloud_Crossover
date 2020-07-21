from abc import ABC, abstractmethod


class AbstractCrossover(ABC):
    @ abstractmethod
    def perform_crossover(self, individual1, individual2):
        # Perform the crossover on two Individual's.
        # Returns a Pair of two Individual's.
        pass


class OnePointCrossover(AbstractCrossover):
    def perform_crossover(self, individual1, individual2):
        pass


class MultiPointCrossover(AbstractCrossover):
    def perform_crossover(self, individual1, individual2):
        pass


class UniformCrossover(AbstractCrossover):
    def perform_crossover(self, individual1, individual2):
        pass
