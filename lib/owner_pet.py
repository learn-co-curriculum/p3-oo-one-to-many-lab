class Pet:

    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError('Not a valid pet type.')

        self.name = name
        self._pet_type = pet_type
        self._owner = owner

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise ValueError('Not a valid pet type.')
        self._pet_type = pet_type


    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Owner):
            raise TypeError("Object is not of type Owner")
        self._owner = owner



class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self._pets.append(pet)
            pet.owner = self
        else:
            raise TypeError("Input object is not of type Pet")

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)


# pet = Pet('Steve', 'cat')
# pet2 = Pet('John', 'dog')

# owner = Owner('James')

# owner.add_pet(pet)
# owner.add_pet(pet2)

# [print(pet.name) for pet in owner.get_sorted_pets()]
