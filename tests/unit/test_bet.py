import pytest
import crapssim
import numpy as np

from crapssim.bet import Fire, Bet, PassLine, Come, DontPass, DontCome, Field, Odds4, Odds5, Odds6, Odds8, Odds9, \
    Odds10, Place4, Place5, Place6, Place8, Place9, Place10, LayOdds4, LayOdds5, LayOdds6, LayOdds8, LayOdds9, \
    LayOdds10, Any7, Two, Three, Yo, Boxcars, AnyCraps, CAndE, Hard4, Hard6, Hard8, Hard10
from crapssim.dice import Dice
from crapssim.table import Table, Point


# Check EV of bets on a "per-roll" basis

@pytest.mark.parametrize("bet, ev", [
    (crapssim.bet.Place4(1), -0.0167),
    (crapssim.bet.Place5(1), -0.0111),
    (crapssim.bet.Place6(1), -0.0046),
    (crapssim.bet.Place8(1), -0.0046),
    (crapssim.bet.Place9(1), -0.0111),
    (crapssim.bet.Place10(1), -0.0167),
    (crapssim.bet.Field(1), -0.0556),
    (crapssim.bet.Any7(1), -0.1667),
    (crapssim.bet.Two(1), -0.1389),
    (crapssim.bet.Three(1), -0.1111),
    (crapssim.bet.Yo(1), -0.1111),
    (crapssim.bet.Boxcars(1), -0.1389),
    (crapssim.bet.AnyCraps(1), -0.1111),
    (crapssim.bet.CAndE(1), -0.1111),
    (crapssim.bet.Hard4(1), -0.0278),
    (crapssim.bet.Hard6(1), -0.0278),
    (crapssim.bet.Hard8(1), -0.0278),
    (crapssim.bet.Hard10(1), -0.0278),
])
def test_ev_oneroll(bet, ev):
    t = Table()
    t.add_player()
    t.point.number = 8  # for place bets to pay properly
    outcomes = []
    t.players[0].add_bet(bet)
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            t.dice.fixed_roll([d1, d2])
            status, win_amt, remove = bet.get_status(t), bet.get_win_amount(t), bet.should_remove(t)

            outcomes.append(win_amt if status == "win" else -1 if status == "lose" else 0)

    assert round(np.mean(outcomes), 4) == ev


@pytest.mark.parametrize('rolls, correct_status, correct_win_amt, correct_remove', [
    ([(6, 1)], None, 0.0, False),
    ([(2, 2), (3, 1), (4, 3), (6, 6)], None, 0.0, False),
    ([(2, 2), (4, 3)], 'lose', 0.0, True),
    ([(2, 2), (2, 2), (3, 3), (3, 3), (4, 3), (4, 4), (4, 4), (5, 5), (5, 5)], 'win', 24, False),
    ([(2, 2), (2, 2), (3, 3), (3, 3), (4, 3), (4, 4), (4, 4), (5, 5), (5, 5), (5, 5), (5, 5)], None, 0.0, False),
    ([(2, 2), (2, 2), (3, 3), (3, 3), (4, 3), (4, 4), (4, 4), (5, 5), (5, 5), (5, 5), (3, 4)], 'lose', 0.0, True),
    ([(2, 2), (2, 2), (3, 3), (3, 3), (4, 3), (4, 4), (4, 4), (5, 5), (5, 5), (2, 3), (2, 3)], 'win', 249, False),
    ([(2, 2), (2, 2), (3, 3), (3, 3), (4, 3), (4, 4), (4, 4), (5, 5), (5, 5), (2, 3), (2, 3), (4, 5), (4, 5)],
     'win', 999, True)
])
def test_fire(rolls, correct_status, correct_win_amt, correct_remove):
    table = Table()
    table.add_player()
    bet = Fire(1)
    table.players[0].add_bet(bet)

    # table.fixed_run(rolls)
    for roll in rolls:
        table.fixed_roll_and_update(roll)

    status, win_amt, remove = bet.get_status(table), bet.get_win_amount(table), bet.should_remove(table)

    assert (status, win_amt, remove) == (correct_status, correct_win_amt, correct_remove)


@pytest.mark.parametrize('bet, point_number, allowed', [
    (PassLine(5), None, True),
    (PassLine(5), 6, False),
    (Come(5), None, False),
    (Come(5), 6, True),
    (DontPass(5), None, True),
    (DontPass(5), 4, False),
    (DontCome(5), None, False),
    (DontCome(5), 8, True),
    (Field(5), None, True),
    (Field(5), 4, True)
])
def test_bet_allowed_point(bet, point_number, allowed):
    table = Table()
    table.add_player()
    dice = Dice()
    dice.total = point_number

    point = Point()
    point.update(dice)

    table.point = point

    assert bet.allowed(player=table.players[0]) == allowed


@pytest.mark.parametrize('bet, new_shooter, allowed', [
    (Field(5), True, True),
    (Field(5), False, True),
    (Fire(5), True, True),
    (Fire(5), False, False)
])
def test_bet_allowed_new_shooter(bet, new_shooter, allowed):
    table = Table()
    table.add_player()

    if new_shooter is False:
        table.fixed_roll((3, 4))

    assert bet.allowed(player=table.players[0]) == allowed


def test_come_equality():
    come_one = Come(5)
    come_one.point = 5
    come_one.new_point = True

    come_two = Come(5)
    come_two.point = 5
    come_two.new_point = True

    assert come_one == come_two


def test_come_point_inequality():
    come_one = Come(5)
    come_one.point = 5
    come_one.new_point = True

    come_two = Come(5)
    come_two.point = 6
    come_two.new_point = True

    assert come_one != come_two


def test_dont_come_equality():
    dont_come_one = DontCome(5)
    dont_come_one.point = 5
    dont_come_one.new_point = True

    dont_come_two = DontCome(5)
    dont_come_two.point = 5
    dont_come_two.new_point = True

    assert dont_come_one == dont_come_two


def test_dont_come_point_inequality():
    dont_come_one = DontCome(5)
    dont_come_one.point = 5
    dont_come_one.new_point = True

    dont_come_two = Come(5)
    dont_come_two.point = 8
    dont_come_two.new_point = True

    assert dont_come_one != dont_come_two


def test_cant_instantiate_bet_object():
    with pytest.raises(TypeError) as e_info:
        Bet(400)


def test_get_cande_dice_2_payout_ratio():
    table = Table()
    table.dice.fixed_roll((1, 1))
    assert CAndE(5).get_payout_ratio(table) == 3


def test_get_cande_dice_3_payout_ratio():
    table = Table()
    table.dice.fixed_roll((1, 2))
    assert CAndE(5).get_payout_ratio(table) == 3


def test_get_cande_dice_11_payout_ratio():
    table = Table()
    table.dice.fixed_roll((6, 5))
    assert CAndE(5).get_payout_ratio(table) == 7


def test_get_cande_dice_12_payout_ratio():
    table = Table()
    table.dice.fixed_roll((6, 6))
    assert CAndE(5).get_payout_ratio(table) == 3


@pytest.mark.parametrize('dice1, dice2, correct_ratio', [
    (1, 1, 2),
    (1, 2, 1),
    (2, 2, 1),
    (5, 4, 1),
    (5, 5, 1),
    (6, 5, 1),
    (6, 6, 2)
])
def test_get_field_default_table_payout_ratio(dice1, dice2, correct_ratio):
    table = Table()
    table.dice.fixed_roll((dice1, dice2))
    assert Field(5).get_payout_ratio(table) == correct_ratio


@pytest.mark.parametrize('dice1, dice2, correct_ratio', [
    (1, 1, 2),
    (1, 2, 14),
    (2, 2, 14000),
    (5, 4, 1),
    (5, 5, 1),
    (6, 5, 1),
    (6, 6, 3)
])
def test_get_field_non_default_table_payout_ratio(dice1, dice2, correct_ratio):
    table = Table()
    table.settings['field_payouts'].update({3: 14, 12: 3, 4: 14000})
    table.dice.fixed_roll((dice1, dice2))
    assert Field(5).get_payout_ratio(table) == correct_ratio


@pytest.mark.parametrize('points_made, correct_ratio', [
    ([4, 5, 6, 9], 24),
    ([4, 5, 6, 9, 10], 249),
    ([4, 5, 6, 8, 9, 10], 999)
])
def test_get_fire_default_table_payout_ratio(points_made, correct_ratio):
    table = Table()
    bet = Fire(5)
    bet.points_made = points_made
    assert bet.get_payout_ratio(table) == correct_ratio


@pytest.mark.parametrize('points_made, correct_ratio', [
    ([4, 5, 6], 6),
    ([4, 5, 6, 9], 9),
    ([4, 5, 6, 9, 10], 69),
    ([4, 5, 6, 8, 9, 10], 420)
])
def test_get_fire_non_default_table_payout_ratio(points_made, correct_ratio):
    table = Table()
    table.settings['fire_points'] = {3: 6, 4: 9, 5: 69, 6: 420}
    bet = Fire(5)
    bet.points_made = points_made
    assert bet.get_payout_ratio(table) == correct_ratio


@pytest.mark.parametrize('bet', [
    PassLine(5),
    Odds4(5),
    Odds5(5),
    Odds6(5),
    Odds8(5),
    Odds9(5),
    Odds10(5),
    Place4(5),
    Place5(5),
    Place6(6),
    Place8(8),
    Place9(9),
    Place10(10),
    LayOdds4(5),
    LayOdds5(5),
    LayOdds6(5),
    LayOdds8(5),
    LayOdds9(5),
    LayOdds10(5),
    Field(5),
    DontPass(5),
    DontCome(5),
    Any7(5),
    Two(5),
    Three(5),
    Yo(5),
    Boxcars(5),
    AnyCraps(5),
    Hard4(5),
    Hard6(5),
    Hard8(5),
    Hard10(5)
])
def test_is_removable_table_point_off(bet):
    table = Table()
    table.add_player()
    assert bet.is_removable(table.players[0]) is True


@pytest.mark.parametrize('bet', [
    Odds4(5),
    Odds5(5),
    Odds6(5),
    Odds8(5),
    Odds9(5),
    Odds10(5),
    Place4(5),
    Place5(5),
    Place6(6),
    Place8(8),
    Place9(9),
    Place10(10),
    LayOdds4(5),
    LayOdds5(5),
    LayOdds6(5),
    LayOdds8(5),
    LayOdds9(5),
    LayOdds10(5),
    Field(5),
    DontPass(5),
    DontCome(5),
    Any7(5),
    Two(5),
    Three(5),
    Yo(5),
    Boxcars(5),
    AnyCraps(5),
    Hard4(5),
    Hard6(5),
    Hard8(5),
    Hard10(5)
])
def test_is_removable_table_point_on(bet):
    table = Table()
    table.add_player()
    table.point.number = 6
    assert bet.is_removable(table.players[0]) is True


def test_passline_is_irremovable_table_point_off():
    bet = PassLine(5)
    table = Table()
    table.add_player()
    table.point.number = 6
    assert bet.is_removable(table.players[0]) is False


def test_come_is_removable_without_point():
    bet = Come(5)
    table = Table()
    table.add_player()
    table.point.number = 6
    assert bet.is_removable(table.players[0]) is True


def test_come_is_irremovable_with_point():
    bet = Come(5)
    bet.point = 10
    table = Table()
    table.add_player()
    table.point.number = 6
    assert bet.is_removable(table.players[0]) is False


@pytest.mark.parametrize('bet', [
    PassLine(5),
    Place4(5),
    Place5(5),
    Place6(5),
    Place8(5),
    Place9(5),
    Place10(5),
    DontPass(5),
    Field(5),
    Any7(5),
    Two(5),
    Three(5),
    Yo(5),
    Boxcars(5),
    AnyCraps(5),
    Hard4(5),
    Hard6(5),
    Hard8(5),
    Hard10(5)
])
def test_bets_always_allowed_point_off(bet):
    table = Table()
    table.add_player()
    assert bet.allowed(table.players[0])


@pytest.mark.parametrize('bet', [
    Come(5),
    Place4(5),
    Place5(5),
    Place6(5),
    Place8(5),
    Place9(5),
    Place10(5),
    DontCome(5),
    Field(5),
    Any7(5),
    Two(5),
    Three(5),
    Yo(5),
    Boxcars(5),
    AnyCraps(5),
    Hard4(5),
    Hard6(5),
    Hard8(5),
    Hard10(5)
])
def test_bets_always_allowed_point_on(bet):
    table = Table()
    table.point.number = 10
    table.add_player()
    assert bet.allowed(table.players[0])


def test_pass_line_odds_allowed():
    table = Table()
    table.add_player()
    table.players[0].bets_on_table = [PassLine(5)]
    table.point.number = 6
    bet = Odds6(25)
    assert bet.allowed(table.players[0])


def test_pass_line_odds_too_high():
    table = Table()
    table.add_player()
    table.players[0].bets_on_table = [PassLine(5)]
    table.point.number = 4
    bet = Odds4(25)
    assert bet.allowed(table.players[0]) is False


def test_come_odds_allowed():
    table = Table()
    table.add_player()
    come_bet = Come(5)
    come_bet.point = 6
    table.players[0].bets_on_table = [come_bet]
    bet = Odds6(25)
    assert bet.allowed(table.players[0])


def test_come_odds_not_allowed():
    table = Table()
    table.add_player()
    come_bet = Come(5)
    come_bet.point = 6
    table.players[0].bets_on_table = [come_bet]
    bet = Odds6(9000)
    assert bet.allowed(table.players[0]) is False