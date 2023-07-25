from lib.counter import *

def test_add_five_to_counter():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5
    assert counter.report() == "Counted to 5 so far."

def test_add_float_to_counter():
    counter = Counter()
    counter.add(2.5)
    assert counter.count == 2.5
    assert counter.report() == "Counted to 2.5 so far."

def test_add_negative_to_counter():
    counter = Counter()
    counter.add(-1)
    assert counter.count == -1
    assert counter.report() == 'Counted to -1 so far.'