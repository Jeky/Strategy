from typing import List

from rules import SimpleAddRule, SimpleSubRule, Rule

# how much you have at beginning
CASH = 100
# iteration times
ITER_COUNT = 10 ** 6
# rules
RULES = [
    SimpleAddRule(0.4, 5),
    SimpleSubRule(0.6, 5),
]


def simulate(rules: List[Rule]) -> List[float]:
    pass
