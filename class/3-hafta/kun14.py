from kun13 import Mahsulot, Savat


class Meva(Mahsulot):
    def __init__(self, nomi, narxi, midori, muddat):
        super().__init__(nomi, narxi, midori)
        self.muddat = muddat
    def __str__(self):
        return f"{super().__str__()}, muddati: {self.muddat}"
         


class Texnika(Mahsulot):
    def __init__(self, nomi, narxi, midori, kafolat):
        super().__init__(nomi, narxi, midori)
        self.kafolat = kafolat
    def __str__(self):
        return f"{super().__str__()}, kafolat: {self.kafolat} oy"
     


olma = Meva("olma", 30000, 12, "12-12-2026")
noutbuk = Texnika("noutbuk", 8000000, 3, 12)
print(olma)
print(noutbuk)

royxat = [olma, noutbuk]          # yangi qator (probelsiz)

for m in royxat:                  # yangi qator (probelsiz)
    print(m)                      #

savat = Savat()
savat.qosh(olma, 2)
savat.qosh(noutbuk, 1)
print(savat.jami())
print(len(savat))