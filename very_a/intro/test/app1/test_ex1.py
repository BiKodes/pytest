import pytest

@pytest.fixture(scope="session")
def fixture_1():
    print('run-fixture-1')
    return 1

@pytest.mark.slow
def test_example1(fixture_1):
    print("test1")
    num = fixture_1
    assert num == 1

def test_example2(fixture_1):
    print("test2")
    num = fixture_1
    assert num == 1

@pytest.fixture
def yield_fixture():
    print('Start Test Phase')
    yield 6
    print('End Test Phase')

def test_example(yield_fixture):
    print('test3')
    assert yield_fixture == 6
