class Mahsulot:
    def __init__(self, nomi, narxi, midori):
        self.nomi = nomi
        self.narxi = narxi
        self.midori = midori
    def __str__(self):
        return f"{self.nomi} - {self.narxi} so'm ({self.midori} dona)"

    def narx_hisobla(self,kg):
        return self.narxi * kg

    @property
    def narxi(self):
        return self._narxi

    @narxi.setter
    def narxi(self, qiymat):
        if qiymat < 0:                   
            raise ValueError("Narx musbat bo'lsin")
        self._narxi= qiymat        

class Savat:
    def __init__(self):
        self.royxat = []

    def qosh(self,mahsulot, kg):
        self.royxat.append([mahsulot, kg])

    def jami(self):
        jami = 0
        for mahsulot, kg in self.royxat:
            jami += mahsulot.narx_hisobla(kg)
        return jami

    def clear(self):
        self.royxat.clear()

    def __len__(self):
        return len(self.royxat)
    
olma = Mahsulot("olma", 30000, 12)
savat = Savat()
savat.qosh(olma, 2)
savat.qosh(Mahsulot("limon", 25000, 8), 1)
print(len(savat))     # 2
savat.clear()
print(len(savat))     # 0