from abc import ABC, abstractmethod

class Tolov(ABC):
    @abstractmethod
    def tola(self, summa): ...

    @abstractmethod
    def qaytar(self, summa): ...

class NaqdTolov(Tolov):
    def __init__(self, balans=0):
        self.balans = balans

    def tola(self, summa):
        if summa > self.balans:
            raise ValueError("Balans yetarli emas")
        self.balans -= summa
        return f"Naqd: {summa} to'landi"

    def qaytar(self, summa):
        self.balans += summa
        return f"Naqd: {summa} qaytarildi"