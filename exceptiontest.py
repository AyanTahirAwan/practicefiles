import pytest

def f():
 raise SystemExit(1)

def testsys():
 with pytest.raises(SystemExit):
    f()