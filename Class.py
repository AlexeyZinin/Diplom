#Классы

class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):
        """Инициализируем атрибуты имя и возраст"""
        self.name = name
        self.age = age
        # print("Собака создана")

    def sit(self):
        """Собака будет садиться по команде"""
        print(self.name.title() + " собака села")

    def jump(self):
        """Собака прыгнула по команде"""
        print(self.name.title() + " собака прыгнула")

my_dog = Dog("Topik", 4)
my_dog_2 = Dog("Gyppi", 5)

print(my_dog.age)
print(my_dog.name)

my_dog.jump()