import numpy as np
import pandas as pd
import pytest

import crapssim as craps
from crapssim import Table
from crapssim.bet import Come, DontCome, DontPass, Field, Odds, PassLine, Place
from crapssim.strategy import *
from crapssim.strategy import (
    BetDontPass,
    BetIfTrue,
    BetPassLine,
    BetPlace,
    DontPassOddsMultiplier,
    PassLineOddsMultiplier,
)
from crapssim.strategy.examples import *
from crapssim.strategy.examples import (
    DiceDoctor,
    HammerLock,
    IronCross,
    Knockout,
    Pass2Come,
    PassLinePlace68,
    PassLinePlace68Move59,
    Place68CPR,
    Place68DontCome2Odds,
    Place682Come,
    Risk12,
)
from crapssim.strategy.simple_bet import *
from crapssim.table import Table, TableUpdate


class TwoDontCome(CountStrategy):
    """Strategy that adds a DontCome bet of a certain amount if that bet doesn't exist on the table.
    Equivalent to CountStrategy((DontCome, ), 2, bet)."""

    def __init__(self, bet_amount: float):
        """If there are less than two DontCome bets placed, place a DontCome bet.

        Parameters
        ----------
        bet_amount
            Amount of the come bet.
        """
        bet = DontCome(bet_amount)
        super().__init__((DontCome,), 2, bet)


def test_dan_strat():
    class DanStrat(AggregateStrategy):
        def __init__(self, dp_amt, yo_amt, f_amt, dc_amt):
            bets = (
                DontPassAmount(dp_amt),
                YoAmount(yo_amt),
                FieldAmount(f_amt),
                TwoDontCome(dc_amt),
            )
            super().__init__(*bets)

    strategy = DanStrat(75, 3, 25, 25)
    bankroll = 500
    max_rolls = 20

    table = craps.Table()
    table.add_player(bankroll=bankroll, strategy=strategy, name="Dan")
    table.run(max_shooter=20, max_rolls=max_rolls, runout=True)
