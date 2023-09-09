import pytest

from crapssim.bet import PassLine, Odds
from crapssim.bet.one_roll import Field
from crapssim.bet.place import Place
from crapssim.strategy.examples import IronCross
from crapssim.table import Table, TableUpdate


@pytest.mark.parametrize("point, last_roll, strat_info, bets_before, dice_result, bets_after", [
    (
        None, None, None,
        [],
        None,
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [PassLine(bet_amount=5.0)],
        (5, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (5, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (5, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (1, 5),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        9, 9, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (6, 3),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 8, None,
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (5, 3),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 10, None,
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (6, 4),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 6, None,
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (1, 5),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (1, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        9, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (3, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 9, None,
        [Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (5, 4),
        [Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        4, 4, None,
        [Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (1, 3),
        [Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        4, 11, None,
        [Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0)],
        (5, 6),
        [Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (5, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        4, 4, None,
        [PassLine(bet_amount=5.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (3, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [PassLine(bet_amount=5.0)],
        (5, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (5, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 12, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (6, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (5, 1),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        None, 11, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (5, 6),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (2, 4),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 10, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0)],
        (6, 4),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (3, 3),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        9, 9, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (3, 6),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (6, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        8, 8, None,
        [PassLine(bet_amount=5.0)],
        (2, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        8, 10, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (5, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 8, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (3, 5),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (4, 2),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 4),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        8, 8, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (2, 6),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (4, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        8, 8, None,
        [PassLine(bet_amount=5.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        8, 10, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (5, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        8, 11, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (5, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 8, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (2, 6),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        9, 9, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (6, 3),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (6, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 11, None,
        [],
        (6, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (2, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (1, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 11, None,
        [],
        (5, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [PassLine(bet_amount=5.0)],
        (3, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (4, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 11, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (5, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 4, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (1, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (4, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [PassLine(bet_amount=5.0)],
        (4, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 10, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (5, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (1, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (2, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 10, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 12, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (6, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (6, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 11, None,
        [],
        (6, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (3, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 5, None,
        [PassLine(bet_amount=5.0)],
        (2, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 4, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (5, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        8, 8, None,
        [PassLine(bet_amount=5.0)],
        (3, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (5, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 5, None,
        [PassLine(bet_amount=5.0)],
        (1, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (4, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 11, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (6, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (2, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (2, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 11, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (6, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (4, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (5, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 10, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (4, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (6, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 10, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (6, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (4, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 4, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 4, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (1, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 4, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (3, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (4, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (5, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 11, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (5, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 4, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (3, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (3, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        4, 4, None,
        [PassLine(bet_amount=5.0)],
        (1, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 12, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (6, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (2, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (1, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        10, 10, None,
        [PassLine(bet_amount=5.0)],
        (4, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 10, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        10, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 10, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (3, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 10, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (2, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 2, None,
        [],
        (1, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        8, 8, None,
        [PassLine(bet_amount=5.0)],
        (4, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        8, 4, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (1, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (3, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 12, None,
        [],
        (6, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (1, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        8, 8, None,
        [PassLine(bet_amount=5.0)],
        (5, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        8, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (2, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        8, 2, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (1, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        8, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (4, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        8, 10, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        8, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (1, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (2, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        4, 4, None,
        [PassLine(bet_amount=5.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (3, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (1, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 10, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (4, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        4, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (4, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        4, 10, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (1, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 5, None,
        [PassLine(bet_amount=5.0)],
        (1, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (4, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 5, None,
        [Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (4, 1),
        [Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (2, 4),
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 11, None,
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (5, 6),
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (2, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [PassLine(bet_amount=5.0)],
        (2, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 4),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (1, 5),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 9, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0)],
        (4, 5),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 11, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0)],
        (5, 6),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 11, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0)],
        (5, 6),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 5, None,
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0)],
        (3, 2),
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 2, None,
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (1, 1),
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 3, None,
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (1, 2),
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (6, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        9, 9, None,
        [PassLine(bet_amount=5.0)],
        (3, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (4, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (4, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (4, 3),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (6, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 11, None,
        [],
        (5, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        4, 4, None,
        [PassLine(bet_amount=5.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (5, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (2, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        4, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (3, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        4, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (2, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        8, 8, None,
        [PassLine(bet_amount=5.0)],
        (2, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (2, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        9, 9, None,
        [PassLine(bet_amount=5.0)],
        (5, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 9, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (5, 4),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        9, 9, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (3, 6),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        9, 10, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0)],
        (6, 4),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (5, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [PassLine(bet_amount=5.0)],
        (1, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 10, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (5, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 2, None,
        [],
        (1, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 11, None,
        [],
        (5, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [PassLine(bet_amount=5.0)],
        (5, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (3, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (1, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [PassLine(bet_amount=5.0)],
        (3, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (4, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 2, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (1, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (5, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 4),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (5, 1),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 4, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0)],
        (3, 1),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 8, None,
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0)],
        (2, 6),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 11, None,
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (5, 6),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (4, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 6, None,
        [Place(8, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (3, 3),
        [Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), PassLine(bet_amount=5.0)]
    ),
    (
        None, 11, None,
        [Place(8, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (6, 5),
        [Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), PassLine(bet_amount=5.0)]
    ),
    (
        9, 9, None,
        [Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), PassLine(bet_amount=5.0)],
        (4, 5),
        [Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 9, None,
        [Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (4, 5),
        [Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        4, 4, None,
        [Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (3, 1),
        [Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (6, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 5, None,
        [PassLine(bet_amount=5.0)],
        (3, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (4, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (3, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [PassLine(bet_amount=5.0)],
        (1, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (1, 5),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        9, 9, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (6, 3),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 9, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (3, 6),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        8, 8, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (2, 6),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        8, 5, None,
        [Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0)],
        (1, 4),
        [Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (3, 4),
        [PassLine(bet_amount=5.0)]
    ),
    (
        4, 4, None,
        [PassLine(bet_amount=5.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (3, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        4, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        4, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (4, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        4, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (4, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        4, 2, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0)],
        (1, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (6, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (2, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        9, 9, None,
        [PassLine(bet_amount=5.0)],
        (4, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (4, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 4, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (6, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 5, None,
        [PassLine(bet_amount=5.0)],
        (4, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (4, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 12, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (6, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (4, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (6, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        8, 8, None,
        [PassLine(bet_amount=5.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        8, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (5, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        8, 11, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (5, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (2, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 5, None,
        [PassLine(bet_amount=5.0)],
        (2, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (6, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 2, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (1, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 5, None,
        [Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (2, 3),
        [Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        None, 11, None,
        [Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (6, 5),
        [Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        9, 9, None,
        [Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (6, 3),
        [Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        9, 4, None,
        [Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (3, 1),
        [Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        9, 6, None,
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (2, 4),
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 10, None,
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (4, 6),
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 6, None,
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (5, 1),
        [Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (4, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (3, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 4, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (1, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (2, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 4, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (2, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (2, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (3, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (1, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 3, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (1, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 9, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (4, 5),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        4, 4, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (2, 2),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (6, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        5, 5, None,
        [PassLine(bet_amount=5.0)],
        (2, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 2, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (1, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 4, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (3, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 10, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (4, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (5, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        5, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (5, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 5, None,
        [Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (4, 1),
        [Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        None, 3, None,
        [Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (2, 1),
        [Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        10, 10, None,
        [Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (5, 5),
        [Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 10, bet_amount=10.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        10, 8, None,
        [Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 10, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (6, 2),
        [Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 10, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (2, 5),
        [PassLine(bet_amount=5.0)]
    ),
    (
        None, 12, None,
        [],
        (6, 6),
        [PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [PassLine(bet_amount=5.0)],
        (3, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 4, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (1, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 10, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (6, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 9, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (5, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (4, 2),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (3, 3),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 11, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0)],
        (5, 6),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (6, 1),
        [PassLine(bet_amount=5.0)]
    ),
    (
        9, 9, None,
        [PassLine(bet_amount=5.0)],
        (6, 3),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        9, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 9, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 9, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0)],
        (4, 5),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        5, 5, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (2, 3),
        [Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        5, 11, None,
        [Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0)],
        (6, 5),
        [Place(6, bet_amount=12.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        None, 7, None,
        [],
        (5, 2),
        [PassLine(bet_amount=5.0)]
    ),
    (
        8, 8, None,
        [PassLine(bet_amount=5.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        8, 2, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (1, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        8, 6, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (4, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 8, bet_amount=10.0), Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 8, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0)],
        (5, 3),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        4, 4, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (1, 3),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 3, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 1),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 8, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0)],
        (4, 4),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 8, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0)],
        (6, 2),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 10, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (4, 6),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 8, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0)],
        (3, 5),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 10, None,
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (6, 4),
        [Place(5, bet_amount=10.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 6, None,
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 4),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 9, None,
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (4, 5),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 3, None,
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (1, 2),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 9, None,
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (6, 3),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        4, 6, None,
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (2, 4),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 4, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 4, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (1, 3),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        None, 3, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0)],
        (2, 1),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Place(6, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (2, 4),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 3, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0)],
        (1, 2),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 8, None,
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0)],
        (5, 3),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 4, None,
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (3, 1),
        [Place(5, bet_amount=10.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (1, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (4, 1),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (2, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 5, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (1, 4),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(8, bet_amount=12.0), Place(5, bet_amount=10.0), Field(bet_amount=5.0)]
    ),
    (
        6, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (6, 2),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 11, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (5, 6),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        6, 8, None,
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0)],
        (3, 5),
        [PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), Field(bet_amount=5.0)]
    ),
    (
        None, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0)],
        (4, 2),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)]
    ),
    (
        6, 6, None,
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0)],
        (2, 4),
        [Place(5, bet_amount=10.0), Place(8, bet_amount=12.0), PassLine(bet_amount=5.0), Odds(PassLine, 6, bet_amount=10.0), Field(bet_amount=5.0)]
    )
])
def test_ironcross_integration(point, last_roll, strat_info, bets_before, dice_result, bets_after):
    table = Table()
    table.add_player(bankroll=float("inf"), strategy=IronCross(5))  # ADD STRATEGY HERE
    table.point.number = point
    table.last_roll = last_roll
    table.players[0].bets = bets_before
    table.dice.fixed_roll(dice_result)
    TableUpdate().run_strategies(table)
    assert table.players[0].bets == bets_after
