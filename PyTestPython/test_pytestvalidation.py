import pytest


@pytest.fixture(scope="module")
def prework():
    print("prework call")
    return "pass"


@pytest.fixture(scope="function")
def secondWork():
    print("second fixture call")
    yield  # it will pause  and execute the steps defined in function where this fixture is called and then come back to this line
    print("close the browser")


def test_initialcheck(prework, secondWork):
    print("first method")
    assert prework == "pass"


def test_secondcheck(presetupwork, secondWork):
    print("second method")


# run pytest PyTestPython/test_pytestvalidation.py -s -v
# output will be
"""
PyTestPython/test_pytestvalidation.py prework call
second fixture call
first method
.close the browser
setup call
second fixture call
second method
.close the browser
"""
