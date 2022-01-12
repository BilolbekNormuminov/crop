from crop import Crop


class Wheat(Crop):
    # A wheat crop

    def __init__(self) -> None:
        super().__init__(1, 1, 1)
        self._type = "Wheat"
