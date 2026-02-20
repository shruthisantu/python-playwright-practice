import pytest


@pytest.fixture(scope="session")
def presetupwork():
    print("setup call")
