# class Telefon:
#     def __init__(self, model, narx):
#         self.model = model
#         self.narx = narx

#     def chegirma(self, foiz):
#         self.narx -= (self.narx / 100) * foiz

#     def malumot(self):
#         print(f"{self.model} - {self.narx} so'm")



# tel = Telefon("iPhone 15", 12000000)
# tel.chegirma(10)
# tel.malumot()   # iPhone 15 — 10800000.0 so'm


# class Kitob:
#     def __init__(self, nom, muallif, sahifalar):
#         self.nom = nom
#         self.muallif = muallif
#         self.sahifalar = sahifalar

#     def oqish_vaqti(self):
#         return self.sahifalar / 50 

#     def qisqa_malumot(self):
#         print(f"{self.nom} - {self.muallif}")

# k = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 300)
# print(k.oqish_vaqti())   # 6.0
# k.qisqa_malumot()        # O'tkan kunlar — Abdulla Qodiriy


# class Hisoblagich:
#     def __init__(self):
#         self.qiymat = 0

#     def oshir(self):
#         self.qiymat += 1

#     def kamaytir(self):
#         if self.qiymat > 0:
#             self.qiymat -= 1


#     def kor(self):
#         return self.qiymat

# h = Hisoblagich()
# h.oshir()
# h.oshir()
# h.kamaytir()
# h.kamaytir()
# h.kamaytir()   # 0 dan pastga tushmaydi
# print(h.kor())   # 0


# class Mahsulot:
#     def __init__(self, nom, narx):
#         self.nom = nom
#         self.narx = narx
    
#     def __str__(self):
#         return f"{self.nom} - {self.narx} so'm"
    
# #     def malumot(self):
#         # print(f"{self.nom} - {self.narx} so'm")


# class Savat:
#     def __init__(self):
#         self.mahsumotlar = []

#     def qosh(self, mahsulot):
#         self.mahsumotlar.append(mahsulot)

#     def jami(self):
#         jami_narx = 0
#         for m in self.mahsumotlar:
#             jami_narx += m.narx
#         return jami_narx

#     def malumot(self):
#         for m in self.mahsumotlar:
#             print(m)


# m1 = Mahsulot("Non", 5000)
# m2 = Mahsulot("Sut", 12000)
# m3 = Mahsulot("Olma", 8000)

# s = Savat()
# s.qosh(m1)
# s.qosh(m2)
# s.qosh(m3)

# print(s.jami())   # 25000
# s.malumot()

from kun_1 import Talaba

class Guruh:
    def __init__(self, nom):
        self.nom = nom
        self.talabalar = []

    def talaba_qosh(self, talaba):
        self.talabalar.append(talaba)

    def ortacha(self):
        if not self.talabalar:
            return 0 
        jami = 0
        for i in self.talabalar:
            jami += i.ortacha()
        return jami / len(self.talabalar)
    
    def eng_yaxshi(self):
        if not self.talabalar:
            return 0 
        yaxsi = self.talabalar[0]
        for i in self.talabalar:
            if i.ortacha() > yaxsi.ortacha():
                yaxsi = i
        return yaxsi.ism
    


# Talaba ni tekshirish
t1 = Talaba("Ali", 20)
t1.baho_qosh(5)
t1.baho_qosh(5)

# print(t1.ism)          # Ali
# print(t1.yosh)         # 20
# print(t1.baholar)      # [5, 5]
# print(t1.ortacha())    # 5.0
# t1.malumot()           # Ism: Ali ...


# Guruh ni tekshirish
g = Guruh("101-guruh")
g.talaba_qosh(t1)

# print(g.nom)           # 101-guruh
# print(len(g.talabalar)) # 1
# print(g.ortacha())     # 5.0
print(g.eng_yaxshi())  # Ali