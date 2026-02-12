import pytest
from example_fastapi_app.__main__ import (
    person,
    persons_list,
    rest_api,
)
from fastapi.testclient import TestClient

client = TestClient(rest_api)


def test_create_person():
    """Test POST /person"""
    response = client.post(
        "/person", json={"name": "Charlie", "age": 22, "description": "Student"}
    )
    assert response.status_code == 200
    assert len(persons_list) == 1
    assert persons_list[0].name == "Charlie"


def test_get_person():
    """Test GET /person/{name}"""
    persons_list.append(person("David", 45, "Architect"))

    response = client.get("/person/David")
    assert response.status_code == 200
    assert response.json()["name"] == "David"


def test_delete_person():
    """Test DELETE /person/{name}"""
    persons_list.append(person("Eve", 28, "Artist"))

    response = client.delete("/person/Eve")
    assert response.status_code == 200
    assert len(persons_list) == 0


def test_update_person():
    """Test PUT /person/{name}"""
    persons_list.append(person("Frank", 50, "CEO"))

    response = client.put(
        "/person/Frank", json={"name": "Frank", "age": 51, "description": "Retired"}
    )
    assert response.status_code == 200
    assert persons_list[0].age == 51
    assert persons_list[0].description == "Retired"


def test_get_nonexistent_person():
    """Test error handling when person doesn't exist"""
    with pytest.raises(ValueError):
        client.get("/person/Ghost")
