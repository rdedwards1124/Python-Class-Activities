class Race:
    def __init__(self, name, driver_limit):
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = []

    def add_driver(self, driver):
        if len(self.drivers) < self.driver_limit:
            self.drivers.append(driver)
            print(f"Racer: {driver.name}, Age: {driver.age}, Rank: {driver.ranking}")
        else:
            print("Too many drivers!!!")

    def get_average_ranking(self):
        total = 0
        for driver in self.drivers:
            total += driver.get_ranking()
        average = total/len(self.drivers)
        return average


class Driver:
    number_of_drivers = 0

    def __init__(self, name, age, ranking):
        self.name = name
        self.age = age
        self.ranking = ranking
        Driver.number_of_drivers += 1

    def get_ranking(self):
        return self.ranking


driver1 = Driver("Lewis Hamilton", 36, 83)
driver2 = Driver("Eliud Kipchoge", 36, 95)
driver3 = Driver("Sebastian Vettel", 34, 76)
driver4 = Driver("Ayrton Senna", 34, 99)

Indie500 = Race("Indie 500", 10)

Indie500.add_driver(driver1)
Indie500.add_driver(driver2)
Indie500.add_driver(driver3)
Indie500.add_driver(driver4)
Indie500.add_driver(Driver("Gig Gagne", 30, 100))
Indie500.add_driver(Driver("Person", 70, 10))


print(f"Average Rank of Racers: {Indie500.get_average_ranking()}")


