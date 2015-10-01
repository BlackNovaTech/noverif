import __builtin__ as builtins
import os as _os
import sys as _sys
import pickle as _pickle

# define class before instantiation (damn you single pass interpreter!)
class LibStdout(object):
    def __init__(self):
        self.logger = Logger()

    def write(self, text):
        msg = "(Call:Print:" + str(text).encode('string-escape') + ":stdlib#print)"
        self.logger.log(msg)


class Logger(object):
    def __init__(self):
        self.msg_list = []

    def compose(self):
        if not self.msg_list == []:
            total_message = '\n'.join(self.msg_list)
            total_message += '\n'
            _stdout.write(total_message)
        else:
            pass

    def log(self, message):
        self.msg_list.append(message)

    def __del__(self):
        self.compose()


class HouseMarketUserInterface(object):
    def __init__(self):
        self.dots = []
        self.lines = []
        self.log = Logger()

    def plot_dot(self, x, y, color, **kwargs):
        self.dots.append((x, y, color))

    def plot_line(self, *args, **kwargs):
        self.lines.append(args)

    def show(self):
        pass


class StockMarketUserInterface(object):
    def __init__(self, enable_cache=False):
        self.plots = []
        self.log = Logger()

    def get_stock_quotes(self, symbol, start, end):
        input_file = _file_open()
        pickles = _pickle.load(input_file)
        return pickles[symbol + start + end]

    def plot(self, prices, color, **kwargs):
        self.plots.append((prices, color))

    def show(self):
        pass


class BarChartUserInterface(object):
    def __init__(self, number_of_bars):
        self.number_of_bars = number_of_bars
        self.bar_list = self.create_bars()
        self.name_list = self.create_names()
        self.logger = Logger()

    def create_bars(self):
        bar_list = []
        for i in range(self.number_of_bars):
            bar_list.append(0)
        return bar_list

    def create_names(self):
        name_list = []
        for i in range(self.number_of_bars):
            name_list.append("")
        return name_list

    def raise_bar(self, index):
        try:
            self.bar_list[index] += 1
        except IndexError:
            self.logger.log("(Error:Index:" + str(index) + ":barchart#raise_bar)")

    def show(self):
        pass

    def set_bar_name(self, index, name):
        try:
            self.name_list[index] = name
        except IndexError:
            self.logger.log("(Error:Index:" + str(index) + ":barchart#set_bar_name)")

    def stay_open(self):
        pass

    def wait(self, ms):
        self.logger.log("(Call:Wait:" + str(ms) + ":barchart#wait)")


class OthelloReplayUserInterface(object):
    def __init__(self, scale):
        self.NUMBER_OF_ROWS = 8
        self.NUMBER_OF_COLUMNS = 8
        self.EMPTY = 0
        self.WHITE = 1
        self.BLACK = 2
        self.moves = []
        self.logger = Logger()

    def show(self):
        pass

    def place(self, x, y, color):
        self.moves.append((x, y, color))

    def wait(self, ms):
        self.logger.log("(Call:Wait:" + str(ms) + ":othello#wait)")

    def clear_text(self):
        pass

    def clear(self):
        pass

    def print_(self, text):
        self.logger.log("(Call:Print:" + str(text) + ":othello#print)")

    def place_transparent(self, x, y, color):
        self.moves.append((x, y, self.EMPTY))

    def stay_open(self):
        pass


def _file_open():
    file_to_test = _os.environ.get("INPUTOVERRIDE")
    if file_to_test is None:
        raise ImportError(
            "Error: INPUTOVERRIDE environment variable not set, need file name for input!")

    # redirect all calls to open and file_input to this
    try:
        return _open(file_to_test, 'r')
    except IOError:
        raise ImportError(
            "The file name set in INPUTOVERRIDE was not found, "
            "please check if the file name is correct or if the file is present!")


def file_input():
    input_file = _file_open()
    str_file = input_file.read()
    return str_file

# don't try this at home, kids!
# redefine builtin file#open
_open = builtins.open
builtins.open = lambda *args, **kwargs: file_input()
# redefine builtin stdout
_stdout = _sys.stdout
_sys.stdout = LibStdout()
