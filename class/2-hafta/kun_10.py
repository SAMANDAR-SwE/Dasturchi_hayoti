# class Hayvon:
#     def __init__(self,name: str,yosh: int):
#         self.name = name
#         self.yosh = yosh

#     def ovoz(self):
#         return "..."

#     def tanish(self):
#         return f"Men {self.name}, {self.yosh} yoshdaman"

# class Sutemizuvchi(Hayvon):
#     def __init__(self, name, yosh, tuyoq):
#         super().__init__(name, yosh)
#         self.tuyoq = tuyoq
    
#     def emiz(self):
#         return f"{self.name} emizyapti"

# class Qush(Hayvon):
#     def __init__(self, name, yosh, qanot):
#         super().__init__(name, yosh)    
#         self.qanot = qanot    
#     def uch(self):
#         return f"{self.name} uchyapti"

# class Korzinka:
#     def __init__(self):
#         self.hayvonlar = []
#     def qosh(self, hayvon):
#         self.hayvonlar.append(hayvon)
#     def malumot(self):
#         for h in self.hayvonlar:
#             print(h.tanish())


# k = Korzinka()

# h1 = Sutemizuvchi("Sher", 5, "bor")
# h2 = Qush("Burgut", 3, 2)

# k.qosh(h1)
# k.qosh(h2)

# # k.hayvonlar = [h1, h2]

# k.malumot()
# # for h in [h1, h2]:
# #   h.tanish()
# #
# # 1-iteratsiya: h = h1 → h1.tanish() → "Men Sher, 5 yoshdaman"
# # 2-iteratsiya: h = h2 → h2.tanish() → "Men Burgut, 3 yoshdaman"


# class A:
#     def salom(self):
#         print("A")

# class B(A):
#     def salom(self):
#         super().salom()
#         print("B")

# class C(A):
#     def salom(self):
#         super().salom()
#         print("C")

# class D(B, C):
#     def salom(self):
#         super().salom()
#         print("D")

# D().salom()



# class Baliq:
#     def suz(self):
#         print("Suzayapman")
# class Qush:
#     def uch(self):
#         print("Uchayapman")

# class UcharBaliq(Baliq, Qush):
#     def __init__(self, nom):
#         self.nom = nom

#     def malumot(self):
#         print(f"{self.nom} - Suzadi va uvhadi")



# u = UcharBaliq("Nemo")
# print(u.nom)         # Nemo
# u.suz()              # Suzayapman
# u.uch()              # Uchyapman
# u.malumot()          # Nemo — suzadi va uchadi
# print(UcharBaliq.__mro__)


class It:
    def ovoz(self):
        print("Vov-vov")

class Mushuk:
    def ovoz(self):
        print("Miyov")

class Sigir:
    def ovoz(self):
        print("Moo")


# Sinov
hayvonlar = [It(), Mushuk(), Sigir()]

for h in hayvonlar:
    h.ovoz()


class Doira:
    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return 3.14 * (self.radius ** 2)
        # ← 3.14 * radius ** 2
        pass

class Kvadrat:
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2
        # ← tomon ** 2
        pass

class Uchburchak:
    def __init__(self, asos, balandlik):
        self.asos = asos
        self.balandlik = balandlik

    def yuza(self):
        return self.asos * (self.balandlik / 2)
        


# Sinov
shakllar = [Doira(5), Kvadrat(4), Uchburchak(6, 3)]

for s in shakllar:
    print(f"Yuza: {s.yuza()}")