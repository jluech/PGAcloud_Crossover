import logging

from crossover.crossers import OnePointCrossover, MultiPointCrossover, UniformCrossover
from utilities.utils import Crossers, forward_crosser


def apply_crossover(individual1, individual2):
    # Applies the chosen selection operator on the population and returns a list of pairs [{p1: x, p2: y}]
    logging.debug("Performing crossover on individuals:")
    logging.debug("{pop_}".format(
        pop_=individual1
    ))
    logging.debug("{pop_}".format(
        pop_=individual2
    ))

    crosser = get_crosser()
    return crosser.perform_crossover(individual1, individual2)


def get_crosser():
    crosser = forward_crosser()
    if crosser == Crossers.OnePoint:
        return OnePointCrossover()
    elif crosser == Crossers.MultiPoint:
        __crosser = MultiPointCrossover()
        raise Exception("MultiPointCrossover not implemented yet!")
    elif crosser == Crossers.Uniform:
        __crosser = UniformCrossover()
        raise Exception("UniformCrossover not implemented yet!")
    else:
        raise Exception("No valid Crosser defined!")
