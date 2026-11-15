from django

class Kutubxona:
    def __init__(self, nom):
        self.nom = nom
        self.kitoblar = []

    def qosh(self, kitob):
        self.kitoblar.append(kitob)

    def __len__(self):
        return len(self.kitoblar)

    def __getitem__(self, key):
        return self.kitoblar[key]

    def __iter__(self):
        return iter(self.kitoblar)

    def __enter__(self):
        print(f"{self.nom} ochildi")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"{self.nom} yopildi")
        
            


with Kutubxona("Milliy kutubxona") as kx:
    kx.qosh("O'tkan kunlar")
    kx.qosh("Mehrobdan chayon")
    kx.qosh("Kecha va kunduz")

    print(len(kx))          # 3
    print(kx[0])            # O'tkan kunlar
    print(kx[1])            # Mehrobdan chayon

    for kitob in kx:
        print(kitob)        # har biri

# Milliy kutubxona ochildi
# 3
# O'tkan kunlar
# Mehrobdan chayon
# O'tkan kunlar
# Mehrobdan chayon
# Kecha va kunduz
# Milliy kutubxona yopildi