import unittest
from hand import *
from result import *

class TestPokerGames(unittest.TestCase):
    four_kind_hand = Hand(['4','4','4','4','A'])
    full_house_hand = Hand(['6','6','6','7','7'])
    straight_hand = Hand(['5','6','7','8','9'])
    three_kind_hand = Hand(['J','J','J','2','3'])
    two_pair_hand = Hand(['2','2','K','K','3'])
    pair_hand = Hand(['A','A','2','3','7'])
    high_card_hand = Hand(['J','2','4','5','8'])

    def test_fourkind(self):
        self.assertEqual(self.four_kind_hand.classify(), HandTypes.Four_Of_A_Kind)
    def test_fullhouse(self):
        self.assertEqual(self.full_house_hand.classify(), HandTypes.Full_House)
    def test_straight(self):
        self.assertEqual(self.straight_hand.classify(), HandTypes.Straight)
    def test_threekind(self):
        self.assertEqual(self.three_kind_hand.classify(), HandTypes.Three_Of_A_Kind)
    def test_twopair(self):
        self.assertEqual(self.two_pair_hand.classify(), HandTypes.Two_Pair)
    def test_pair(self):
        self.assertEqual(self.pair_hand.classify(), HandTypes.Pair)
    def test_highcard(self):
        self.assertEqual(self.high_card_hand.classify(), HandTypes.High_Card)
    def test_emptyhand(self):
        with self.assertRaises(ValueError) : Hand([])
    def test_shortcard(self):
        with self.assertRaises(ValueError) : Hand(['2', '6', '7', '8'])
    def test_result_case_one(self):
        player_one = Hand(['A', 'A', 'A', 'K', 'T'])
        player_two = Hand(['2', '2', '2', '3', '3'])
        result = Result(player_one, player_two)
        self.assertEqual(result.compare(), 0)
    def test_result_case_two(self):
        player_one = Hand(['A', 'A', 'K', 'K', 'T'])
        player_two = Hand(['A', 'A', 'K', 'K', 'T'])
        result = Result(player_one, player_two)
        self.assertEqual(result.compare(), -1)
    def test_result_case_three(self):
        player_one = Hand(['A', 'A', '2', '2', '3'])
        player_two = Hand(['K', 'K', 'Q', 'Q', 'T'])
        result = Result(player_one, player_two)
        self.assertEqual(result.compare(), 1)
    def test_result_case_four(self):
        player_one = Hand(['A', 'A', 'A', '2', '2'])
        player_two = Hand(['K', 'K', 'K', 'Q', 'Q'])
        result = Result(player_one, player_two)
        self.assertEqual(result.compare(), 1)
    def test_result_case_four(self):
        player_one = Hand(['A', 'A', '2', '3', '4'])
        player_two = Hand(['A', 'A', '2', '3', '5'])
        result = Result(player_one, player_two)
        self.assertEqual(result.compare(), -1)
    def test_result_case_five(self):
        player_one = Hand(['A', 'A', '9', '9', '3'])
        player_two = Hand(['A', 'A', '8', '8', 'K'])
        result = Result(player_one, player_two)
        self.assertEqual(result.compare(), 1)
    def test_result_case_six(self):
        player_one = Hand(['K', 'K', 'K', 'K', 'A'])
        player_two = Hand(['K', 'K', 'K', 'A', '*'])
        result = Result(player_one, player_two)
        self.assertEqual(result.compare(), -1)
    def test_result_case_seven(self):
        player_one = Hand(['K', 'Q', 'J', 'T', '*'])
        player_two = Hand(['K', 'K', 'J', 'J', '2'])
        result = Result(player_one, player_two)
        self.assertEqual(result.compare(), 1)
    def test_result_case_eight(self):
        player_one = Hand(['K', 'K', 'A', '6', '8'])
        player_two = Hand(['K', 'K', '9', '5', '7'])
        result = Result(player_one, player_two)
        self.assertEqual(result.compare(), -1)
    def test_result_case_nine(self):
        player_one = Hand(['A', 'A', '5', '3', '4'])
        player_two = Hand(['K', '5', 'Q', 'J', 'J'])
        result = Result(player_one, player_two)
        self.assertEqual(result.compare(), 1)
    def test_result_case_ten(self):
        player_one = Hand(['K', 'K', 'A', 'K', '8'])
        player_two = Hand(['K', 'K', '9', 'K', '7'])
        result = Result(player_one, player_two)
        self.assertEqual(result.compare(), -1)
    def test_result_case_eleven(self):
        player_one = Hand(['A', 'A', 'A', '3', '4'])
        player_two = Hand(['K', '5', 'J', 'J', 'J'])
        result = Result(player_one, player_two)
        self.assertEqual(result.compare(), 1)
    def test_wild_fourkind(self):
        four_kind_hand = Hand(['4', '4', '4', '*', 'A'])
        print('\n', four_kind_hand.getlist())
        self.assertEqual(four_kind_hand.classify(), HandTypes.Four_Of_A_Kind)
    def test_wild_fullhouse(self):
        full_house_hand = Hand(['6', '6', '*', '7', '7'])
        print(full_house_hand.getlist())
        self.assertEqual(full_house_hand.classify(), HandTypes.Full_House)
    def test_wild_straight(self):
        straight_hand = Hand(['5', '6', '*', '8', '9'])
        print(straight_hand.getlist())
        self.assertEqual(straight_hand.classify(), HandTypes.Straight)
    def test_wild_threekind(self):
        three_kind_hand = Hand(['J', 'J', '*', '2', '3'])
        print(three_kind_hand.getlist())
        self.assertEqual(three_kind_hand.classify(), HandTypes.Three_Of_A_Kind)
    def test_wild_pair(self):
        pair_hand = Hand(['A', '*', '2', '3', '7'])
        print(pair_hand.getlist())
        self.assertEqual(pair_hand.classify(), HandTypes.Pair)

if __name__ == '__main__':
    unittest.main()
