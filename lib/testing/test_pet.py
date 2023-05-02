from owner_pet import Pet, Owner
import pytest

def test_pet_init_valid():
    """Test Pet class initialization with valid input"""
    pet = Pet("Buddy", "dog")
    assert pet.name == "Buddy"
    assert pet.pet_type == "dog"
    assert pet.owner is None


def test_pet_init_invalid_pet_type():
    """Test Pet class initialization with invalid pet type"""
    with pytest.raises(ValueError):
        Pet("Buddy", "invalid_type")

def test_pet_pet_type_setter_valid():
    """Test Pet class pet_type setter with valid input"""
    pet = Pet("Buddy", "dog")
    pet.pet_type = "cat"
    assert pet.pet_type == "cat"

def test_pet_pet_type_setter_invalid():
    """Test Pet class pet_type setter with invalid input"""
    pet = Pet("Buddy", "dog")
    with pytest.raises(ValueError):
        pet.pet_type = "invalid_type"

def test_pet_owner_setter_valid():
    """Test Pet class owner setter with valid input"""
    pet = Pet("Buddy", "dog")
    owner = Owner("John")
    pet.owner = owner
    assert pet.owner == owner

def test_pet_owner_setter_invalid():
    """Test Pet class owner setter with invalid input"""
    pet = Pet("Buddy", "dog")
    with pytest.raises(TypeError):
        pet.owner = "not_owner_obj"
