# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animals():

    def __init__(self, *args, **kwargs):
        self.name, self.age = args

class Fish(Animals):

    def __init__(self, fish_size, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fish_size = fish_size

class Snake(Animals):

    def __init__(self, poison, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.poison = poison

class Bird(Animals):

    def __init__(self, flight_capability, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flight_capability = flight_capability

class Fabric():

    dict_animals = {
        "Bird": Bird,
        "Snake": Snake,
        "Fish": Fish
    }

    def __init__(self, type_Animal, *args, **kwargs):
        self.animal = self.dict_animals[type_Animal](*args, **kwargs)
        print(type_Animal, ":", self.animal.__dict__)

    def __add__(self, other):
        Animal_1 = type(self.animal)
        Animal_2 = type(other.animal)

        if Animal_2 == Animal_1:
            return "Doesn't eat"
        elif Animal_1 == Bird or Animal_2 == Bird:
            return "Bird Nyam-Nyam"
        elif Animal_1 == Snake or Animal_2 == Snake:
            return "Snake Nyam-Nyam"

if __name__ == "__main__":
    list_animal = [
        Fabric("Fish", "Small", "Данио", 5),
        Fabric("Fish", "Medium", "Телескоп", 80),
        Fabric("Fish", "Medium", "Золотая", 80),
        Fabric("Fish", "Big", "Сомик", 20),
        Fabric("Snake", "Non_venomous", "Питон", 4),
        Fabric("Snake", "Non_venomous", "Удав", 3),
        Fabric("Snake", "Poisonous", "Гадюка", 20),
        Fabric("Bird", "Not_flying", "Пингвин", 4),
        Fabric("Bird", "Flying", "Сокол", 5),
        Fabric("Bird", "Not_flying", "Страус", 5)]

    for i in list_animal:
        for j in list_animal:
            if i != j:
                print(i + j)
