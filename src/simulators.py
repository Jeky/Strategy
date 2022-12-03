from random import Random
from typing import TypeVar, Iterable

from rules import Rule

T = TypeVar('T')


class NoRuleFoundError(Exception):
    pass


class Simulator(object):

    def __init__(self, init_step: T, rules: Iterable[Rule[T]], random_generator: Random = None):
        self.step = init_step
        self.rules = sorted(rules, key=lambda r: r.priority)
        if random_generator:
            self.random_generator = random_generator
        else:
            self.random_generator = Random()

    def simulate(self):
        last_step = self.result
        luck = self.random_generator.random()

        for rule in self.rules:
            if rule.accept(luck, last_step):
                new_step = rule.apply(last_step)
                self.update_step(new_step)
                return

        raise NoRuleFoundError(f"no rule found for luck = {luck}, step = {last_step}")

    @property
    def result(self):
        return self.step

    def update_step(self, new_step: T):
        self.step = new_step