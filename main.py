class Avto:
    """ Базовый класс avto. """
    def __init__(self, model: str, value: int):
        self._model = model
        self.value = value
    @property
    def model(self):
        return self._model
    def __str__(self):
        return f" Марка авто: '{self.model}'. Мощность движка: {self.value} л.с."
    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}).(value={self.value!r})."
    def engine(self):
        print("Двигатель автомобиля")

class Car(Avto):
    """ Дочерний класс car наследуемый от avto. """
    def __init__(self, color: str, model,  value: int):
        super().__init__(model, value) # Поменялся объем двигателя на 1.3 л.
        self.color = color
    def __str__(self):
        return f"Марка авто:'{self.model}'. Цвет : '{self.color}'. Мощность движка: {self.value} л.с."
    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}).(color={self.color!r}). (value={self.value!r})"
    def engine(self):
        print("Двигатель легкого автомобиля")
if __name__ == "__main__":
    a = Avto("Жигули", 75)
    print(a)
    print(a.engine())
    acar = Car("Запорожец", "Синий", 65)
    print(acar)
    print(acar.engine())
