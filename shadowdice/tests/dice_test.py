# -*- coding: utf-8 -*-

import random
import unittest
from unittest.mock import patch

from ..dice import Dice


class DiceTest(unittest.TestCase):

    @patch("shadowdice.dice.randint")
    def test_call_NoSuccesses_ReturnsNoSuccesses(self, rint):
        rint.side_effect = [1, 2, 3]
        
        self.assertEqual(0, Dice(3)().result.successes)
        
    @patch("shadowdice.dice.randint")
    def test_call_WithEdge_ExplodesAllSixes(self, rint):
        rint.side_effect = [6, 2, 3, 6, 5, 5]
        
        self.assertEqual(4, Dice(3, edge=1)().result.successes)
        
    @patch("shadowdice.dice.randint")
    def test_call_WithoutEdge_DoesNotExplodeSixes(self, rint):
        rint.side_effect = [6, 2, 3, 6, 5, 5]
        
        self.assertEqual(1, Dice(3)().result.successes)
        
    @patch("shadowdice.dice.randint")
    def test_call_WithEdgeAndLimit_IgnoresLimit(self, rint):
        rint.side_effect = [5, 5, 5, 5]
        
        self.assertEqual(4, Dice(3, edge=1, limit=3)().result.successes)
        
    @patch("shadowdice.dice.randint")
    def test_call_WithoutEdgeAndLimit_MaxesSuccessesAtLimit(self, rint):
        rint.side_effect = [5, 5, 5, 5]
        
        self.assertEqual(3, Dice(4, limit=3)().result.successes)
        
    @patch("shadowdice.dice.randint")
    def test_call_WithEdge_RollsForEveryDie(self, rint):
        rint.side_effect = [5, 5, 5, 5, 5]
        
        self.assertEqual(5, Dice(3, edge=2, limit=3)().result.successes)
    
    @patch("shadowdice.dice.randint")
    def test_call_WithHalfOnes_NoGlitch(self, rint):
        rint.side_effect = [5, 5, 1, 1]
        
        self.assertFalse(Dice(4)().result.glitch)
        
    @patch("shadowdice.dice.randint")
    def test_call_WithHalfPlusOneOnes_NoGlitch(self, rint):
        rint.side_effect = [5, 5, 1, 1, 1]
        
        self.assertTrue(Dice(5)().result.glitch)
        
