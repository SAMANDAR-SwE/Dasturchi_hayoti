# class Xodim:
#     def __init__(self, ism, oylik):
#         self.ism = ism
#         self.oylik = oylik

#     def malumot(self):
#         print(f"{self.ism} - {self.oylik} so'm")


# class Menejer(Xodim):
#     def __init__(self, ism, oylik, bolim):
#         super().__init__(ism, oylik)
#         self.bolim = bolim

#     def malumot(self):
#         super().malumot()
#         print(f"Bo'lim {self.bolim} ")


# x = Xodim("Ali", 3000000)
# x.malumot()      # Ali — 3000000 so'm

# m = Menejer("Vali", 5000000, "IT")
# m.malumot()
# # Vali — 5000000 so'm
# # Bo'lim: IT


# class Transport:
#     def __init__(self, nom, tezlik):
#         self.nom = nom 
#         self.tezlik = tezlik

#     def malumot(self):
#         print(f"{self.nom} - {self.tezlik} km/soat")

#     def harakat(self):
#         print("Harakatlanyapdi...")

# class Avtomobil(Transport):
#     def __init__(self, nom, tezlik, yonilgi):
#         super().__init__(nom, tezlik)       
#         self.yonilgi = yonilgi

#     def harakat(self):
#         print("Mashina yo'lda ketyapti")

# class Velosiped(Transport):
#     def __init__(self, nom, tezlik):
#         super().__init__(nom, tezlik)

#     def harakat(self):
#         print("Velosiped pedal o'ynayapti")

# a = Avtomobil("Malibu", 200, "Benzin")
# print(a.nom)         # Malibu
# print(a.yonilgi)     # Benzin
# a.malumot()          # Malibu — 200 km/soat
# a.harakat()          # Mashina yo'lda ketyapti

# v = Velosiped("Trek", 30)
# v.malumot()          # Trek — 30 km/soat
# v.harakat()          # Velosiped pedal o'ynayapti


# class Shakl:
#     def __init__(self, nom):
#         self.nom = nom

#     def yuza(self):
#         return 0 

#     def malumot(self):
#         print(f"{self.nom}: yuza = {self.yuza()}")


# class Doira(Shakl):
#     def __init__(self, nom, radius):
#         super().__init__(nom)
#         self.radius = radius

#     def yuza(self):
#         return 3.14 * self.radius ** 2

# class Kvadrat(Shakl):
#     def __init__(self, nom, tomon):
#         super().__init__(nom)
#         self.tomon = tomon

#     def yuza(self):
#         return self.tomon ** 2

# d = Doira("Doira", 5)
# d.malumot()          # Doira: yuza = 78.5

# k = Kvadrat("Kvadrat", 4)
# k.malumot()          # Kvadrat: yuza = 16


class Hisob:
    def __init__(self, egasi, balans=0):
        self.egasi = egasi
        self.balans = balans

    def pul_qosh(self, summa):
        self.balans += summa

    def malumot(self):
        print(f"{self.egasi}: {self.balans} so'm")


class JamgarmaHisob(Hisob):
    def __init__(self, egasi, balans, foiz):
        super().__init__(egasi, balans)
        self.foiz = foiz

    def foiz_qosh(self):
        self.balans += (self.balans / 100) * self.foiz

    def malumot(self):
        super().malumot()
        print(f"Foiz: {self.foiz}%")


h = Hisob("Ali", 1000000)
h.malumot()          # Ali: 1000000 so'm

print("---")

j = JamgarmaHisob("Vali", 2000000, 10)
j.foiz_qosh()        # 10% → 200000 qo'shildi
j.malumot()
# Vali: 2200000 so'm
# Foiz: 10%