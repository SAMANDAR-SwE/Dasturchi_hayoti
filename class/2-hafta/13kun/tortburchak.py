from shakl import Shakl


class Tortburchak(Shakl):
    __slots__ = ("_eni", "_boyi")

    def __init__(self, eni: float, boyi: float):
        self.eni = eni       # setter orqali — validatsiya ishlaydi
        self.boyi = boyi

    @property
    def eni(self) -> float:
        return self._eni

    @eni.setter
    def eni(self, qiymat: float):
        if qiymat <= 0:
            raise ValueError("Eni musbat bo'lishi kerak")
        self._eni = float(qiymat)

    @property
    def boyi(self) -> float:
        return self._boyi

    @boyi.setter
    def boyi(self, qiymat: float):
        if qiymat <= 0:
            raise ValueError("Bo'yi musbat bo'lishi kerak")
        self._boyi = float(qiymat)

    def yuza(self) -> float:
        return self._eni * self._boyi

    def perimetr(self) -> float:
        return 2 * (self._eni + self._boyi)

    def __repr__(self):
        return f"Tortburchak({self._eni}, {self._boyi})"


class Kvadrat(Tortburchak):
    __slots__ = ()   # ota __slots__ ni meros oladi, yangi yo'q

    def __init__(self, tomon: float):
        super().__init__(tomon, tomon)

    def __repr__(self):
        return f"Kvadrat({self._eni})"