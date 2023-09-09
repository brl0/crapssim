import numpy as np

import crapssim as craps
from crapssim.strategy import AggregateStrategy
from crapssim.strategy.simple_bet import DontPassAmount, FieldAmount, YoAmount
from crapssim.strategy.examples import NDontCome


class DStrat(AggregateStrategy):
    def __init__(self, unit, dp_amt, n_dc, dc_amt, f_amt, yo_amt):
        bets = (
            DontPassAmount(dp_amt * unit),
            NDontCome(n_dc, dc_amt * unit),
            FieldAmount(f_amt * unit),
            YoAmount(round(yo_amt * unit, 0)),
        )
        super().__init__(*bets)


def test_dan_strat():
    strategy = DStrat(25, 3, 2, 1, 1, 0.1)
    bankroll = 500
    max_rolls = 20
    table = craps.Table()
    table.add_player(bankroll=bankroll, strategy=strategy, name="D")
    table.run(max_shooter=20, max_rolls=max_rolls, runout=True)


def test_dan_strat_fixed():
    strategy = DStrat(25, 3, 2, 1, 1, 0.1)
    bankroll = 500
    max_rolls = 20
    table = craps.Table()
    table.add_player(bankroll=bankroll, strategy=strategy, name="D")
    rolls = np.random.randint(1, 7, size=(max_rolls, 2)).tolist()
    table.fixed_run(rolls, verbose=False)
