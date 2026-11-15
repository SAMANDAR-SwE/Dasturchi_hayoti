from kun13 import Mahsulot, Savat
class Mijoz:
    def __init__(self, ism, telefon):
        self.ism = ism
        self.telefon = telefon

    def __str__(self):
        return f"{self.ism} ({self.telefon})"


class Buyurtma:
    def __init__(self, mijoz, savat):
        self.mijoz = mijoz
        self.savat = savat


    def jami(self):
        return self.savat.jami()

    def __str__(self):
        return f"{self.mijoz} \n{self.savat}"
    


ali = Mijoz("Ali", "+998901234567")

savat = Savat()
savat.qosh(Mahsulot("olma", 30000, 12), 2)
savat.qosh(Mahsulot("limon", 25000, 8), 1)

buyurtma = Buyurtma(ali, savat)
print(buyurtma)
