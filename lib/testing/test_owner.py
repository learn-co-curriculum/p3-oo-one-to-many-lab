from owner_pet import Pet, Owner
import pytest

class TestOwner:
  '''Class Owner in owner_pet.py'''

def test_owner_methods():
    owner = Owner("Alice")
    pet1 = Pet("Buddy", "Dog")
    pet2 = Pet("Milo", "Cat")

    assert owner.get_name() == "Alice"
    owner.set_name("Bob")
    assert owner.get_name() == "Bob"

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    assert len(owner._pets) == 2

    owner.remove_pet(pet1)

    assert len(owner._pets) == 1
    assert pet2 in owner._pets

    with pytest.raises(TypeError):
        owner.add_pet("String")

    with pytest.raises(TypeError):
        owner.remove_pet("String")

    with pytest.raises(ValueError):
        owner.remove_pet(pet1)

def test_get_sorted_pets():
    owner = Owner("Alice")
    pet1 = Pet("Buddy", "Dog")
    pet2 = Pet("Milo", "Cat")
    pet3 = Pet("Charlie", "Dog")

    owner.add_pet(pet1)
    owner.add_pet(pet2)
    owner.add_pet(pet3)

    sorted_pets = owner.get_sorted_pets()
    sorted_pet_names = [pet.get_name() for pet in sorted_pets]

    assert sorted_pet_names == ["Buddy", "Charlie", "Milo"]
