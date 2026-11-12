# class Talaba:
#     universitet = "TATU"

#     def __init__(self, ism):
#         self.ism = ism

#     @classmethod
#     def universitetni_almashtir(cls, yangi):
#         cls.universitet = yangi


# print(Talaba.universitet)                # TATU
# Talaba.universitetni_almashtir("MIT")
# print(Talaba.universitet)                # MIT


class Kitob:
    def __init__(self, nom, muallif, yil):
        self.nom = nom
        self.muallif = muallif
        self.yil = yil
        self.mavjud = True

    def __str__(self):
        return f"{self.nom} - {self.muallif} ({self.yil})"

    def __repr__(self):
        return f"Kitob('{self.nom}', '{self.muallif}', {self.yil})"

    def __eq__(self, value):
        return self.nom == value.nom and self.muallif == value.muallif


k = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 1926)
print(k)          # O'tkan kunlar — Abdulla Qodiriy (1926)
print(repr(k))    # Kitob('O'tkan kunlar', 'Abdulla Qodiriy', 1926)
print(k == Kitob("O'tkan kunlar", "Abdulla Qodiriy", 1926))   # True


class Azo:
    def __init__(self, nom):
        self.nom = nom
        self.olgan_kitoblar = []

    def __str__(self):
        return f"{self.nom} ({len(self.olgan_kitoblar)} ta kitob)"


    def kitob_ol(self, kitob):
        self.olgan_kitoblar.append(kitob)

    def kitob_qaytar(self, kitob):
        self.olgan_kitoblar.remove(kitob)


a = Azo("Ali")
a.kitob_ol(k)
print(a)                  # Ali (1 ta kitob)
print(a.olgan_kitoblar)   # [Kitob('O'tkan kunlar', ...)]

a.kitob_qaytar(k)
print(a)                  # Ali (0 ta kitob)     

class Kutubxona:
    def __init__(self, nom):
        self.nom = nom
        self.kitoblar = []
        self.azolar = []

    def kitob_qosh(self, kitob):
        self.kitoblar.append(kitob)

    def kitob_qaytar(self, azo, kitob):
        if kitob in azo.olgan_kitoblar:      # a'zoda shu kitob bormi?
            azo.kitob_qaytar(kitob)          # a'zodan olib tashlash
            kitob.mavjud = True              # kutubxonada yana mavjud
    
    def azo_qosh(self, azo):
        self.azolar.append(azo)

    def kitob_ber(self, azo, kitob):
        if kitob.mavjud:
            kitob.mavjud = False
            azo.kitob_ol(kitob)
        else:
            print("Kitob mavjud emas")

    
    @property
    def mavjud_kitoblar(self):
        return sum(1 for k in self.kitoblar if k.mavjud)
    
    
    def __str__(self):
        return f"Kutubxona: {len(self.kitoblar)} kitob, {len(self.azolar)} ta a'zo"

    # Kitob
k = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 1926)
print(k)              # O'tkan kunlar - Abdulla Qodiriy (1926)
print(repr(k))        # Kitob('O'tkan kunlar', 'Abdulla Qodiriy', 1926)
print(k == Kitob("O'tkan kunlar", "Abdulla Qodiriy", 1926))   # True

# A'zo
a = Azo("Ali")
a.kitob_ol(k)
print(a)              # Ali (1 ta kitob)
a.kitob_qaytar(k)
print(a)              # Ali (0 ta kitob)

# Kutubxona
kx = Kutubxona("Milliy kutubxona")
kx.kitob_qosh(k)
kx.azo_qosh(a)

print(kx)                    # Kutubxona: 1 kitob, 1 ta a'zo
print(kx.mavjud_kitoblar)    # 1

kx.kitob_ber(a, k)
print(kx.mavjud_kitoblar)    # 0
print(k.mavjud)              # False
print(a)                     # Ali (1 ta kitob)

kx.kitob_qaytar(a, k)
print(kx.mavjud_kitoblar)    # 1
print(k.mavjud)              # True
print(a)                     # Ali (0 ta kitob)