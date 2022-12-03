from random import Random

from rules import *
from simulators import Simulator

START = 0
SIMULATOR_COUNT = 10
SIMULATOR_ITER_COUNT = 1000


def main():
    rules = ProbabilityRuleGenerator()
    rules.new_rule(SimpleAddRule, 0.5, 1)
    rules.new_rule(SimpleSubRule, 0.5, 1)

    seed = Random().random()
    random = Random(seed)
    print(f"seed = {seed}")

    simulators = [Simulator(START, rules, random) for _ in range(SIMULATOR_COUNT)]

    for simulator in simulators:
        for i in range(SIMULATOR_ITER_COUNT):
            simulator.simulate()

        print(f"{simulator.result}")


if __name__ == '__main__':
    main()
