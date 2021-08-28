class Tomato:
    index: int
    ripeness: str
    states: tuple = ("Отсутствует", "Цветение", "Зеленый", "Красный")

    def __init__(self, index: int):
        self.index = index
        self.ripeness = self.states[0]

    def grow(self):
        self.ripeness = self.states[self.states.index(self.ripeness) + 1]

    def is_ripe(self):
        if self.ripeness == self.states[3]:
            return True
        else:
            return False


tomat = Tomato(1)
print(tomat.grow())