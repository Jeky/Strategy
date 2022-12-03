from typing import Callable


class Rule(object):

    def __init__(self, probability: float, operator: Callable[[float], float]):
        self.probability = probability
        self.operator = operator


class SimpleAddRule(Rule):

    def __init__(self, probability: float, to_add: float):
        super().__init__(probability, lambda x: x + to_add)


class SimpleSubRule(Rule):

    def __init__(self, probability: float, to_sub: float):
        super().__init__(probability, lambda x: x - to_sub)
