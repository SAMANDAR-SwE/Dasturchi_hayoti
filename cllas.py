# class Talaba:
#     def __init__(self, ism, yosh):
#         self.ism  = ism
#         self.yosh = yosh

#     def print_line(self):
#         print(self.ism, " ", self.yosh)

#     def salom_ber(self):
#         print(f"Salom men {self.ism}, {self.yosh}")


# print(Talaba('Ali', 19).salom_ber(), Talaba('Vali', 20).salom_ber())


# class Hisob:
    # def __init__(self, egasi):
        # self.egasi = egasi
        # self.balans = 0
# 
    # def qosh(self, summa):
        # self.balans += summa
        # return f"Sizning balans:{self.balans} so'm"
    # 
    # def yech(self, summa):
        # if self.balans <= summa:
            # self.balans - summa
            # return "Mablag' yechildi."
# 
        # return "Mablag' yetarli emas."
# 
    # def __str__(self):
        # return f"{self.egasi}: {self.balans} so'm"
# 
# h = Hisob("Ali")
# h.qosh(100000)
# print(h.yech(30000))
# print(h.yech(200000))
# print(h)
# 
# 


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

def eng_qimmat(royxat):
    qimmat = royxat[0]
    for m in royxat:
        if m.narxi > qimmat.narxi:
            qimmat = m
    return qimmat

def jami_qiymat(royxat):
    jami = 0
    for m in royxat:
        jami += m.narxi * m.miqdori         # jami ga shu mahsulotning narxi * miqdori ni qo'shing
    return jami
print(jami_qiymat(royxat))
print(eng_qimmat(royxat))
