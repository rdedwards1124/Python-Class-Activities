class Person:
    def __init__(self, in_name, in_age):
        self.name = in_name
        self.age = in_age

    def get_name(self):
        return self.name


################################################
class Zoo:
    def __init__(self, name="Local Zoo"):
        self.name = name
        self.animals = []
        self.customers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{self.name} has a(n) {animal}")

    def add_animals(self, animals):
        self.animals.extend(animals)
        print(f"{self.name} has many animals")

    def add_customer(self, name):
        self.customers.append(name)
        print(f"{name} has entered {self.name}")

    def remove_customer(self, name):
        self.customers.remove(name)
        print(f"{name} has left {self.name}")

    def visit_animals(self):
        for a in self.animals:
            print(f"visiting {a.get_name()}")
            a.make_noise()
            a.eat_food()


###################################################
class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def make_noise(self):
        print("Every animal makes noise")

    def eat_food(self):
        print("All creatures need sustenance")


###################################################
class Customer(Person):
    def __init__(self, in_name, in_age, has_ticket=False, inside_zoo=False):
        super().__init__(in_name, in_age)
        self.has_ticket = has_ticket
        self.inside_zoo = inside_zoo

    def buy_ticket(self):
        self.has_ticket = True
        print("You have purchased a ticket!")

    def enter_zoo(self, the_zoo):
        if self.has_ticket:
            self.has_ticket = False
            self.inside_zoo = True
            the_zoo.add_customer(self.name)
            print("Welcome to the Zoo!")
        else:
            print("Please purchase ticket before entering...")

    def exit_zoo(self, the_zoo):
        if self.inside_zoo:
            self.inside_zoo = False
            the_zoo.remove_customer(self.name)


###################################################
class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name} says blub, blub, blub")

    def eat_food(self):
        print(f"{self.name} eats seafood.")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name} says tweet, tweet")

    def eat_food(self):
        print(f"{self.name} eats seeds, nuts and berries.")


class Chimp(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name} says hoot-grunt")

    def eat_food(self):
        print(f"{self.name} eats seeds, fruit, leaves, and bark.")


class Canine(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name} says woof, bark, growl.")

    def eat_food(self):
        print(f"{self.name} eats meat, fish.")


class Feline(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name} says growl, roar, purr.")

    def eat_food(self):
        print(f"{self.name} eats meat, fish.")


###################################################
nycZoo = Zoo("NYC Zoo")


salmon = Fish("salmon")
robin = Bird("robin")
parrot = Bird("parrot")
bonobo = Chimp("bonobo")
wolf = Canine("wolf")
fox = Canine("fox")
tiger = Feline("tiger")
lion = Feline("lion")
leopard = Feline("leopard")
nycZoo.add_animals([salmon, robin, parrot, bonobo])
nycZoo.add_animals([wolf, fox, tiger, lion, leopard])

alice = Customer("Alice", 25)
bob = Customer("Bob", 20)
charlie = Customer("Charlie", 10)
dave = Customer("Dave", 30)
for c in [alice, bob, charlie, dave]:
    c.buy_ticket()
    c.enter_zoo(nycZoo)
nycZoo.visit_animals()
for c in [alice, bob, charlie, dave]:
    c.exit_zoo(nycZoo)
