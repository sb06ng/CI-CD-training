import pytest
from example_fastapi_app.__main__ import person, persons_list


@pytest.fixture
def test_person_one():
    return person("Test", 20, "Tester")


@pytest.fixture
def test_person_two():
    return person("Test", 99, "Different Age")


@pytest.fixture(autouse=True)
def run_around_tests():
    persons_list.clear()
    yield
