from example_fastapi_app.__main__ import person


def test_person_creation(test_person_one: person):
    """Test that the person class correctly assigns attributes"""
    assert test_person_one.name == "Test"
    assert test_person_one.age == 20
    assert test_person_one.description == "Tester"


def test_person_equality(test_person_one: person, test_person_two: person):
    """Test the __eq__ override logic"""
    assert test_person_one == test_person_two
