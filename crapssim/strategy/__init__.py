"""
Strategies to be assigned to players on the Craps table. The strategy determines what bets the
player should make, remove, or change. Strategies are applied for the player to change the bets
after the previous bets and table have been updated.
"""

from crapssim.strategy.core import Strategy, AggregateStrategy, BetIfTrue, RemoveIfTrue, \
    IfBetNotExist, BetPointOff, BetPointOn, CountStrategy
from crapssim.strategy.odds import OddsMultiplierStrategy

from crapssim.strategy.examples import BetPassLine, PassLineOddsMultiplier, BetDontPass, DontPassOddsMultiplier, \
    BetPlace
