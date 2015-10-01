import unittest
import os
import __builtin__ as builtins

os.environ["INPUTOVERRIDE"] = ''

# Hack around the hacks
_open = builtins.open
from ipy_lib import *

_ipy_open = builtins.open
builtins.open = _open


class IPyLibTests(unittest.TestCase):
    def setUp(self):
        os.environ["INPUTOVERRIDE"] = __file__

    def tearDown(self):
        os.environ["INPUTOVERRIDE"] = ''

    def test_file_input(self):
        this_file = open(__file__).read()
        self.assertEquals(this_file, file_input())

    def test_open_override(self):
        # _ipy_open -> the open hack
        self.assertEquals(_ipy_open('somefile'), file_input())


class HouseMarketTest(unittest.TestCase):
    def setUp(self):
        self.ui = HouseMarketUserInterface()

    def test_init(self):
        self.assertListEqual([], self.ui.dots)
        self.assertListEqual([], self.ui.lines)

    def test_plot_dot(self):
        self.ui.plot_dot(5, 3, 'g')
        self.ui.plot_dot(3, 7, 'g')
        self.assertIn((5, 3, 'g'), self.ui.dots)
        self.assertIn((3, 7, 'g'), self.ui.dots)

    def test_plot_line(self):
        self.ui.plot_line(5, 3)
        self.ui.plot_line(7, 6)
        self.assertIn((5, 3), self.ui.lines)
        self.assertIn((7, 6), self.ui.lines)

    def test_show(self):
        self.ui.show()


class StockMarketTest(unittest.TestCase):
    def setUp(self):
        self.ui = StockMarketUserInterface()

    def test_init(self):
        self.assertListEqual([], self.ui.plots)

    @unittest.skip("TODO")
    def test_get_stock_quotes(self):
        pass

    def test_plot(self):
        self.ui.plot([1, 2, 3, 4], 'b')
        self.ui.plot([4, 5, 6, 7], 'g')
        self.assertIn(([1, 2, 3, 4], 'b'), self.ui.plots)
        self.assertIn(([4, 5, 6, 7], 'g'), self.ui.plots)

    def test_show(self):
        self.ui.show()

class BarChartTest(unittest.TestCase):
    def setUp(self, number_of_bars=10):
        self.number_of_bars = number_of_bars
        self.ui = BarChartUserInterface(number_of_bars)

    def test_init(self):
        self.assertListEqual([], self.ui.bar_list)
        self.assertListEqual([], self.ui.bar_list)

    def test_raise_bar(self):
        test_list = [1] * self.number_of_bars
        for i in range(self.number_of_bars):
            self.ui.raise_bar(i)
        self.assertListEqual(test_list, self.ui.bar_list)

    def test_name_bar(self):
        test_names = ['a'] * self.number_of_bars
        for i in range(self.number_of_bars):
            self.ui.set_bar_name(i, 'a')
        self.assertListEqual(test_names, self.ui.name_list)

class OthelloReplayTest(unittest.TestCase):
    def setUp(self):
        self.ui = OthelloReplayUserInterface()

    def test_place(self):
        test_moves = [(1, 1, self.ui.BLACK)] * 10
        for i in range(10):
            self.ui.place(1,1, self.ui.BLACK)
        self.assertListEqual(test_moves, self.ui.moves)

if __name__ == '__main__':
    unittest.main()
