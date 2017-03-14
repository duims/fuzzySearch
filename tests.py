from hypothesis import given
from hypothesis.strategies import text, integers
from fuzzySearch import lev


@given(text(), text(max_size=10))
def test_add_levenshtein(s, modifier):
    v = generate_string(s, mod2=modifier)
    assert(lev(s, v) == len(modifier))


@given(text(), text(), text())
def test_delete_levenshtein(s, u, v):
    long_str = generate_string(mod1=s, mod2=u, mod3=v)
    short_str = generate_string(mod1=s, mod3=v)
    assert(lev(long_str, short_str) == len(u))


@given(text(), text(), text(), text())
def test_substitute_levenshtein(s, u, v, w):
    left = generate_string(mod1=s, mod2=u, mod3=v)
    right = generate_string(mod1=s, mod2=w, mod3=v)
    assert(lev(left, right) == lev(u, w))


def generate_string(mod1='', mod2='', mod3=''):
    return mod1 + mod2 + mod3
