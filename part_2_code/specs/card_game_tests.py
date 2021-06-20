import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card = Card("Heart", 1)
        self.card1 = Card("Spade", 2)
        self.card2 = Card("Diamond", 4)
        self.card_game = CardGame()
        self.cards = [self.card, self.card1, self.card2]

    def test_check_for_ace(self):
        expected = True
        actual = self.card_game.check_for_ace(self.card)
        self.assertEqual(expected, actual)

    def test_check_for_no_ace(self):
        expected = False
        actual = self.card_game.check_for_ace(self.card1)
        self.assertEqual(expected, actual)

    def test_highest_card(self):
        expected = self.card2
        actual = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(expected, actual)

    def test_cards_total(self):
        expected = "You have a total of 7"
        actual = self.card_game.cards_total(self.cards)
        self.assertEqual(expected, actual)
