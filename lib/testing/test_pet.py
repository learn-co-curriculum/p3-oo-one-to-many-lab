from owner_pet import Pet, Owner

class TestPet:
  '''Class Pet in owner_pet.py'''

  def test_pet_methods(self):

      """Test attributes and constructor"""
      pet = Pet("Buddy", "Dog")

      assert pet.get_name() == "Buddy"
      assert pet.get_pet_type() == "Dog"

      pet.set_name("Milo")
      pet.set_pet_type("Cat")

      assert pet.get_name() == "Milo"
      assert pet.get_pet_type() == "Cat"
