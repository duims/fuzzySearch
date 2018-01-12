from hypothesis import given
from hypothesis.strategies import text

from scanDetection.fuzzySearch import lev


@given(text(), text(max_size=10))
def test_add_levenshtein(s, modifier):
    v = f"{s}{modifier}"
    assert(lev(s, v) == len(modifier))


@given(text(), text(), text())
def test_delete_levenshtein(s, u, v):
    long_str = f"{s}{u}{v}"
    short_str = f"{s}{v}"
    assert(lev(long_str, short_str) == len(u))


@given(text(), text(), text(), text())
def test_substitute_levenshtein(s, u, v, w):
    left = f"{s}{u}{v}"
    right = f"{s}{w}{v}"
    assert(lev(left, right) == lev(u, w))
