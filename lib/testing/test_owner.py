import pytest
from owner_pet import Pet, Owner

def test_owner_init():
    """Test Owner class initialization"""
    owner = Owner("John")
    assert owner.name == "John"
    assert len(owner._pets) == 0

def test_owner_add_pet_valid():
    """Test Owner class add_pet method with valid input"""

    owner = Owner("John")
    pet = Pet("Buddy", "dog")
    owner.add_pet(pet)
    assert len(owner._pets) == 1
    assert pet in owner._pets
    assert pet.owner == owner


def test_owner_add_pet_invalid():
    """Test Owner class add_pet method with invalid input"""
    owner = Owner("John")
    with pytest.raises(TypeError):
        owner.add_pet("not_pet_obj")


def test_owner_get_sorted_pets():
    """Test Owner class get_sorted_pets method"""
    owner = Owner("John")
    pet1 = Pet("Buddy", "dog")
    pet2 = Pet("Whiskers", "cat")
    pet3 = Pet("Max", "dog")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    owner.add_pet(pet3)
    sorted_pets = owner.get_sorted_pets()
    assert sorted_pets == [pet1, pet3, pet2]
