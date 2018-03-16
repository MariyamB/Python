#source code:test_c_to_f.py
#name: Sai Ratnam Peri

import c_to_f as m

def test_minus_40():
    assert m.c_2_f(-40.0) == -40.0
def test_freezing():
    assert m.c_2_f(0.0) == 32.0
