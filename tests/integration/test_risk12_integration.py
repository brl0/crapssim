import copy

import pytest

from crapssim.bet import PassLine, Place
from crapssim.bet.one_roll import Field
from crapssim.strategy.examples import Risk12
from crapssim.table import Table, TableUpdate


@pytest.mark.parametrize("point, last_roll, strat_info, bets_before, dice_result, bets_after", [
    (
        None, None, None,
        [],
        None,
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        10, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 6),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (5, 4),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)],
        (5, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (3, 3),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        10, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)],
        (2, 6),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (3, 2),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (3, 2),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (3, 4),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 6, {'winnings': 0},
        [],
        (5, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 2, {'winnings': 0},
        [],
        (1, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 5},
        [PassLine(bet_amount=5.0)],
        (2, 4),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        6, 5, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (2, 3),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        6, 9, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (3, 6),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 5},
        [],
        (2, 5),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        4, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 1),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        4, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (5, 2),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        4, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 1),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (3, 4),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        10, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (4, 1),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 3, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 12, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (6, 6),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 10, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (4, 6),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        9, 9, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (4, 5),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        9, 10, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (5, 5),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (1, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        5, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 12, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (2, 5),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        4, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        4, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (4, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (3, 4),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 12, {'winnings': 0},
        [],
        (6, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 5},
        [PassLine(bet_amount=5.0)],
        (1, 5),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        6, 10, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (4, 6),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        6, 11, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (5, 6),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        6, 9, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (3, 6),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 5},
        [],
        (6, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (1, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (4, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 11, {'winnings': 0},
        [],
        (5, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        10, 10, {'winnings': 10},
        [PassLine(bet_amount=5.0)],
        (4, 6),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 11, {'winnings': 10},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (6, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 5, {'winnings': 10},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (4, 1),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 6, {'winnings': 10},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (3, 3),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        None, 10, {'winnings': 10},
        [Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)],
        (6, 4),
        [Place(8, bet_amount=6.0), Place(6, bet_amount=6.0), PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        10, 10, {'winnings': 0},
        [Place(8, bet_amount=6.0), Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (5, 5),
        [Place(8, bet_amount=6.0), Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (6, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        9, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        9, 2, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (1, 1),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 9, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (5, 4),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 3, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (2, 1),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 2, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (1, 1),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        4, 4, {'winnings': 5},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (2, 2),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        4, 10, {'winnings': 5},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (6, 4),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        4, 5, {'winnings': 5},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (3, 2),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 5},
        [],
        (2, 5),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (4, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        4, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        4, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (5, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        4, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (6, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        4, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (5, 1),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (3, 4),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 2, {'winnings': 0},
        [],
        (1, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        9, 9, {'winnings': 5},
        [PassLine(bet_amount=5.0)],
        (4, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        9, 8, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        9, 4, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (1, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        9, 10, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        9, 12, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (6, 6),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 9, {'winnings': 5},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (3, 6),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        9, 9, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (3, 6),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        9, 5, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (4, 1),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (4, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        10, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (4, 1),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (2, 4),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        10, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        10, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)],
        (3, 2),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        10, 11, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)],
        (6, 5),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (6, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (4, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        5, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 11, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 5, {'winnings': 0},
        [],
        (1, 4),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        5, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 11, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (3, 4),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (3, 4),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 2, {'winnings': 0},
        [],
        (1, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 5},
        [PassLine(bet_amount=5.0)],
        (5, 1),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        6, 10, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        6, 5, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (1, 4),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 5},
        [],
        (2, 5),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 6, {'winnings': 0},
        [],
        (5, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        8, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        8, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (3, 4),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        9, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 6),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        9, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (3, 2),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        9, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)],
        (5, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        9, 12, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (6, 6),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (2, 5),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 3, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 6, {'winnings': 0},
        [],
        (4, 2),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        4, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 4, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (2, 2),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        9, 9, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (6, 3),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        9, 3, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (2, 1),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        9, 5, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (4, 1),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        9, 5, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (1, 4),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (1, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (4, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        5, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 3, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 11, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 11, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 5, {'winnings': 0},
        [],
        (4, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        9, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 9, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (5, 4),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0), PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (3, 4),
        [Place(6, bet_amount=6.0), Place(8, bet_amount=6.0),
         PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        5, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 11, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (4, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        8, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        8, 11, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 8, {'winnings': 0},
        [],
        (3, 5),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        10, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (5, 2),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        8, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        8, 11, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        8, 3, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 8, {'winnings': 0},
        [],
        (4, 4),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        5, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (2, 5),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (6, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        10, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 11, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (6, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)],
        (2, 6),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (2, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)],
        (5, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (3, 3),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        10, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        10, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (2, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (5, 1),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        10, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)],
        (3, 1),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        10, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)],
        (4, 1),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        10, 3, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        10, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)],
        (1, 4),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        10, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (4, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        5, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 12, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (1, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (3, 4),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        10, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 6),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (4, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 6, {'winnings': 0},
        [],
        (4, 2),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        8, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 8, {'winnings': 0},
        [],
        (3, 5),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 3, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 6, {'winnings': 0},
        [],
        (5, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        5, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 12, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 12, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 12, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 11, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 12, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 11, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 5, {'winnings': 0},
        [],
        (2, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (6, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 11, {'winnings': 0},
        [],
        (5, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        5, 5, {'winnings': 10},
        [PassLine(bet_amount=5.0)],
        (1, 4),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        5, 9, {'winnings': 10},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (5, 4),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        5, 8, {'winnings': 10},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)],
        (5, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        5, 6, {'winnings': 10},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (2, 4),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 10},
        [],
        (3, 4),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        10, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 2, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (1, 1),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        10, 3, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (1, 2),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (4, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 11, {'winnings': 0},
        [],
        (5, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 10},
        [PassLine(bet_amount=5.0)],
        (1, 5),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        6, 10, {'winnings': 10},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 10},
        [],
        (6, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 12, {'winnings': 0},
        [],
        (6, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        8, 8, {'winnings': 5},
        [PassLine(bet_amount=5.0)],
        (3, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)]
    ),
    (
        8, 4, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)],
        (3, 1),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)]
    ),
    (
        None, 8, {'winnings': 5},
        [Place(6, bet_amount=6.0)],
        (3, 5),
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        10, 10, {'winnings': 0},
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (5, 5),
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (2, 5),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        4, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 1),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        4, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (3, 2),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (1, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        10, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 6),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (6, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (1, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 11, {'winnings': 0},
        [],
        (5, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 10},
        [],
        (6, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        8, 8, {'winnings': 10},
        [PassLine(bet_amount=5.0)],
        (3, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0)]
    ),
    (
        None, 8, {'winnings': 10},
        [Place(6, bet_amount=6.0)],
        (3, 5),
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        5, 5, {'winnings': 0},
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (1, 4),
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        5, 10, {'winnings': 0},
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (6, 4),
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        5, 2, {'winnings': 0},
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (1, 1),
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        5, 3, {'winnings': 0},
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (2, 1),
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        5, 11, {'winnings': 0},
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (6, 5),
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        5, 10, {'winnings': 0},
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (5, 5),
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        5, 9, {'winnings': 0},
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)],
        (5, 4),
        [Place(6, bet_amount=6.0), PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (3, 4),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        5, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 4, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (5, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (1, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 5, {'winnings': 0},
        [],
        (2, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (6, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        5, 5, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (2, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (4, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (6, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 8, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (1, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 2, {'winnings': 0},
        [],
        (1, 1),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 5},
        [],
        (2, 5),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        4, 4, {'winnings': 5},
        [PassLine(bet_amount=5.0)],
        (1, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        4, 11, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (6, 5),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        4, 5, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (2, 3),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        4, 2, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (1, 1),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        4, 5, {'winnings': 5},
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)],
        (1, 4),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 5},
        [],
        (2, 5),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        9, 9, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 6),
        [PassLine(bet_amount=5.0), Place(6, bet_amount=6.0), Place(8, bet_amount=6.0)]
    ),
    (
        9, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (2, 4),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        9, 10, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        9, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0)],
        (1, 5),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        9, 3, {'winnings': 0},
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)],
        (1, 2),
        [PassLine(bet_amount=5.0), Place(8, bet_amount=6.0), Place(6, bet_amount=6.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (4, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        6, 6, {'winnings': 0},
        [PassLine(bet_amount=5.0)],
        (3, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, {'winnings': 0},
        [],
        (4, 3),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    ),
    (
        None, 11, {'winnings': 0},
        [],
        (5, 6),
        [PassLine(bet_amount=5.0), Field(bet_amount=5.0)]
    )
])
def test_risk12_integration(point, last_roll, strat_info, bets_before, dice_result, bets_after):
    table = Table()
    strategy = Risk12()
    table.point.number = point
    table.last_roll = last_roll
    if table.point.number in (4, 9, 10):
        strategy.pre_point_winnings = 10
    elif strat_info is not None and 'winnings' in strat_info:
        strategy.pre_point_winnings = strat_info['winnings']
    table.add_player(bankroll=float("inf"), strategy=strategy)  # ADD STRATEGY HERE
    table.players[0].bets = copy.copy(bets_before)
    table.dice.fixed_roll(dice_result)
    TableUpdate().run_strategies(table)
    assert table.players[0].bets == bets_after
