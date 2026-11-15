class Savat:
    def __init__(self):
        self.mahsulotlar = []

    def qosh(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def __len__(self):
        return len(self.mahsulotlar)

    def __getitem__(self, index):
        return self.mahsulotlar[index]
    
    def __iter__(self):
        return iter(self.mahsulotlar)
        


# Sinov
s = Savat()
s.qosh("Non")
s.qosh("Sut")
s.qosh("Olma")

print(len(s))        # 3
print(s[0])          # Non
print(s[1])          # Sut
print(s[2])          # Olma

for m in s:
    print(m)         # Non, Sut, Olma