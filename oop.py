
class Mahsulot:
    def __init__(self, nomi: str, narxi: int , miqdori: int):
        self.nomi = nomi
        self.narxi = narxi
        self.miqdori = miqdori

    def __str__(self):
        return f"{self.nomi} - {self.narxi} so'm"

    def eng_qimmat(self):
        return 


royxat = [
    Mahsulot("olma", 30000, 12),
    Mahsulot("limon", 25000, 8),
    Mahsulot("banan", 40000, 5),
    Mahsulot("anor", 35000, 10),
]

# def eng_qimmat(royxat):
#     qimmat = royxat[0]
#     for m in royxat:
#         if m.narxi > qimmat.narxi:
#             qimmat = m
#     return qimmat

# def jami_qiymat(royxat):
#     jami = 0
#     for m in royxat:
#         jami += m.narxi * m.miqdori         # jami ga shu mahsulotning narxi * miqdori ni qo'shing
#     return jami
# print(jami_qiymat(royxat))
# print(eng_qimmat(royxat))



class Savat:
    def __init__(self):
        self.royxat = []

    def qosh(self, mahsulot, kg):
        self.royxat.append([mahsulot, kg])
        return "Mahsulot qoshildi"


olma = Mahsulot("olma", 30000, 12)
limon = Mahsulot("limon", 25000, 8)

savat = Savat()
savat.qosh(olma, 2)
savat.qosh(limon, 1)
print(len(savat.royxat))  