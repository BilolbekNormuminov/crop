from crop import *
from potato import Potato
from wheat import Wheat


def create_crop() -> Crop:
    print()
    print("Which crop would you like to create?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("Please select an option from the above menu")

    choice = input_int(
        "Option selected: ", "Please, enter a valid option", lambda value: value in (1, 2))

    match choice:
        case 1:
            new_crop = Potato()
        case 2:
            new_crop = Wheat()

    return new_crop


def main():
    new_crop = create_crop()
    manage_crop(new_crop)


if __name__ == "__main__":
    main()
