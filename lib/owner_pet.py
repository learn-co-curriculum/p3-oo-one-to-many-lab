class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_pet_type(self):
        return self.pet_type

    def set_pet_type(self, pet_type):
        self.pet_type = pet_type


class Owner:
    def __init__(self, name):
        self._name = name
        self._pets = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self._pets.append(pet)
        else:
            raise TypeError("Input object is not of type Pet")

    def remove_pet(self, pet):
        if isinstance(pet, Pet):
            if pet in self._pets:
                self._pets.remove(pet)
            else:
                raise ValueError("Pet not found in the list")
        else:
            raise TypeError("Input object is not of type Pet")

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.get_name())


# pet = Pet('Steve', 'cat')
# pet2 = Pet('John', 'dog')

# owner = Owner('James')

# owner.add_pet(pet)
# owner.add_pet(pet2)

# [print(pet.name) for pet in owner.get_sorted_pets()]
# print(owner.get_name())
# print(pet.get_name())
# print(pet.get_pet_type())