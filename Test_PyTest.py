from c_to_f import c2f

def test_minu_40():
    assert c2f(-40) == -40

def test_freezing():
    assert c2f(0) == 32

def test_boiling():
    assert c2f (100) == 212

