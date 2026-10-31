# Mashq 1: It class

# class It:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh

#     def qichqir(self):
#         print(f"Vov-vov! Men {self.ism}") 

#     def tanish(self):
#         print(f"Men {self.ism}, {self.yosh} yoshdaman")


# it = It("Bobik", 3)
# it.qichqir()   # Vov-vov! Men Bobik
# it.tanish()    # Men Bobik, 3 yoshdaman




# Mashq 2: Hisoblagich class


# class Hisoblagich:
#     def __init__(self):
#         self.qiymat = 0

#     def oshir(self):
#         self.qiymat += 1

    
#     def kamaytir(self):
#         self.qiymat -= 1

#     def kor(self):
#         return self.qiymat
# h = Hisoblagich()
# h.oshir()
# h.oshir()
# print(h.kor())   # 2
# h.kamaytir()
# print(h.kor())   # 1


# Mashq 3: Avtomobil class

# class Avtomobil:
#     def __init__(self, marka, rang):
#         self.marka = marka
#         self.rang = rang
#         self.tezlik = 0

#     def gaz_ber(self, qiymat):
#         self.tezlik += qiymat

#     def tormoz(self):
#         self.tezlik = 0

#     def holat(self):
#         print(f"{self.marka} ({self.rang}) — {self.tezlik} km/soat")



# car = Avtomobil("Malibu", "oq")
# car.gaz_ber(40)
# car.gaz_ber(20)
# car.holat()      # Malibu (oq) — 60 km/soat
# car.tormoz()
# car.holat()      # Malibu (oq) — 0 km/soat




# Mashq 4 (qiyinroq): Talaba classi

class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self.baholar = []

    def baho_qosh(self, baho):
        self.baholar.append(baho)

    def ortacha(self):
        if not self.baholar:
            return 0
        return sum(self.baholar) / len(self.baholar)

    def malumot(self):
        print(f"Ism: {self.ism}")
        print(f"Yoshi: {self.yosh}")
        print(f"O'rtacha bahosi: {self.ortacha()}")


