from random import randint

from utils import input_int


class Crop:
    """A generic food crop"""

    def __init__(self, growth_rate: int, ligth_need: int, water_need: int) -> None:
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = ligth_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def needs(self) -> dict:
        return {"light need": self._light_need, "water need": self._water_need}

    def report(self) -> dict:
        return {"type": self._type, "status": self._status, "growth": self._growth, "days growing": self._days_growing}

    def print_report(self) -> None:
        print(f"        type: {self._type}")
        print(f"      status: {self._status}")
        print(f"      growth: {self._growth}")
        print(f"days growing: {self._days_growing}")

    def _update_status(self) -> None:
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"
        else:
            raise

    def grow(self, light: int, water: int) -> None:
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate

        self._days_growing += 1
        self._update_status()



def auto_grow(crop: Crop, days: int) -> None:
    for day in range(days):
        light = randint(1, 10)
        water = randint(1, 10)

        crop.grow(light, water)


def manual_grow(crop: Crop) -> None:
    light = input_int("Please, enter a value for light (1-10): ",
                      lambda value: 1 <= value <= 10)
    water = input_int("Please, enter a value for water (1-10): ",
                      lambda value: 1 <= value <= 10)

    crop.grow(light, water)


def manage_crop(crop: Crop) -> None:
    print("This is crop management program")
    print()

    noexit = True
    while noexit:
        print("1. Grow manually over 1 day")
        print("2. Grow automatically over 30 days")
        print("3. Report status")
        print("0. Exit test program")
        print()
        print("Please select an option from the above menu")

        option = input_int("Option selected: ", "Please enter a valid option: ",
                           lambda value: value in (0, 1, 2, 3))
        print()

        match option:
            case 1:
                manual_grow(crop)
            case 2:
                auto_grow(crop, 30)
            case 3:
                crop.print_report()
            case 0:
                noexit = False

        print()

    print("Thank you for using our crop management program!")
