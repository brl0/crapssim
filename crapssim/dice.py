import typing

from numpy import random as r


class Dice:
    """
    Simulate the rolling of a dice

    Attributes
    ----------
    n_rolls : int
        Number of rolls for the dice
    result : array, shape = [2]
        Most recent outcome of the roll of two dice
    total : int
        Sum of dice outcome

    """

    def __init__(self) -> None:
        self.result: typing.Iterable[int] | None = None
        self.n_rolls: int = 0

    def roll(self) -> None:
        self.n_rolls += 1
        self.result = r.randint(1, 7, size=2).tolist()

    def fixed_roll(self, outcome: typing.Iterable[int]) -> None:
        self.n_rolls += 1
        self.result = outcome

    def fixed_total(self, total: int) -> None:
        if not total:
            self.result = None
            return
        m = min(total - 1, 7)
        if m > 1:
            d1 = r.randint(1, m)
        else:
            d1 = 1
        d2 = total - d1
        self.fixed_roll([d1, d2])

    @property
    def total(self) -> int:
        """Sum of dice outcome."""
        if self.result:
            return sum(self.result)
        return 0
