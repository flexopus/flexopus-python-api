from flexopus import status

def test_ok():
    assert status() is "OK"
