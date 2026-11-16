from abc import ABC, abstractmethod
class Mahsulot(ABC):
    def __init__(self, nomi, narxi, midori):
        self.nomi = nomi
        self.narxi = narxi
        self.midori = midori
    def __str__(self):
        return f"{self.nomi} - {self.narxi} so'm ({self.midori} dona)"
    
    @abstractmethod
    def tavsif(self):
        ...
    
    def narx_hisobla(self,kg):
        return self.narxi * kg

    @property
    def narxi(self):
        return self._narxi

    @narxi.setter
    def narxi(self, qiymat):
        if qiymat <= 0:                   
            raise ValueError("Narx musbat bo'lsin")
        self._narxi= qiymat        

class Savat:
    def __init__(self):
        self.royxat = []

    def qosh(self,mahsulot, kg):
        self.royxat.append([mahsulot, kg])
    @abstractmethod
    def tavsif(self):
        ...
    def jami(self):
        jami = 0
        for mahsulot, kg in self.royxat:
            jami += mahsulot.narx_hisobla(kg)
        return f"{jami}"

    def clear(self):
        self.royxat.clear()

    def __len__(self):
        return len(self.royxat)

    def __str__(self):
        qatorlar = []
        for mahsulot, kg in self.royxat:
            qatorlar.append(f"{mahsulot.nomi} - {mahsulot.narxi} so'm x {kg} kg = {mahsulot.narx_hisobla(kg)} so'm")
        qatorlar.append(f"Jami: {self.jami()} so'm")
        return "\n".join(qatorlar)

        
