from __future__ import annotations
from typing import Callable, Generic, TypeVar, Tuple

T = TypeVar("T")


class Rule(Generic[T]):

    def __init__(self, priority: int):
        self.priority = priority

    def accept(self, luck: float, step: T) -> bool:
        return False

    def apply(self, step: T) -> T:
        return step


class TerminateRule(Rule):

    def __init__(self, criteria: Callable[[float, T], bool]):
        super().__init__(-1)
        self.criteria = criteria

    def accept(self, luck: float, step: T) -> bool:
        return self.criteria(luck, step)

    def apply(self, step: T) -> T:
        return 0


class ProbabilityRule(Rule):

    def __init__(self, luck_range: Tuple[float], operator: Callable[[T], T]):
        super().__init__(int(luck_range[0] * 100))
        self.luck_range = luck_range
        self.operator = operator

    def accept(self, luck: float, step: T) -> bool:
        if step is None:
            return False

        return self.luck_range[0] <= luck < self.luck_range[1]

    def apply(self, step: T) -> T:
        return self.operator(step)

    def __str__(self):
        return ""


class SimpleAddRule(ProbabilityRule):

    def __init__(self, luck_range: Tuple[float], to_add: float):
        super().__init__(luck_range, lambda x: x + to_add)


class SimpleSubRule(ProbabilityRule):

    def __init__(self, luck_range: Tuple[float], to_sub: float):
        super().__init__(luck_range, lambda x: x - to_sub)


class ProbabilityRuleGenerator(Generic[T]):

    def __init__(self):
        self.start = 0.0
        self.rules = []

    def new_rule(self, rule_class: type(ProbabilityRule), probability: float, *args) -> ProbabilityRuleGenerator:
        if self.start + probability > 1:
            raise ValueError(f"probability is too large. Max probability could be {1 - self.start}")

        luck_range = [self.start, self.start + probability]
        self.start += probability
        self.rules.append(rule_class(luck_range, *args))

        return self

    def __iter__(self):
        return self.rules.__iter__()
