import enum
class AnimalType(enum.Enum):
    Cat = 1
    Dog = 2


class Animal:
    def __init__(self, type: AnimalType):
        self.type = type

class Cat(Animal):
    def __init__(self, name):
        super().__init__(AnimalType.Cat)
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(AnimalType.Dog)
        self.name = name

class AnimalQueue:
    def __init__(self):
        self.animals_list = []

    def __str__(self):
        animals_name = []
        if len(self.animals_list) > 0:
            for animal in self.animals_list:
                animals_name.append(animal.name)
        else:
            return "There is no element"

        return " ".join(animals_name)


    def enque(self, animal: Animal):
        self.animals_list.append(animal)

    def deque(self):
        if len(self.animals_list) > 0:
            return self.animals_list.pop(0)
        else:
            return "There is no animal"

    def dequeue_dog(self):
        for index, animal in enumerate(self.animals_list):
            if animal.type == AnimalType.Dog:
                return self.animals_list.pop(index)
        return "There is no dog in the list"

    def dequeue_cat(self):
        for index, animal in enumerate(self.animals_list):
            if animal.type == AnimalType.Cat:
                return self.animals_list.pop(index)
        return "There is no dog in the list"

animal_queue = AnimalQueue()
animal_queue.enque(Cat("Cat1"))
animal_queue.enque(Dog("Dog1"))
animal_queue.enque(Cat("Cat2"))
animal_queue.enque(Dog("Dog2"))
animal_queue.enque(Cat("Cat3"))
print(animal_queue)
animal_queue.dequeue_dog()
print(animal_queue)
animal_queue.deque()
print(animal_queue)
animal_queue.dequeue_cat()
print(animal_queue)