# class Talaba:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
#         self.baholar = []

#     def baho_qosh(self, baho):
#         self.baholar.append(baho)

#     def ortacha(self):
#         if not self.baholar:
#             return 0

#         jami = 0
#         for i in self.baholar:
#             jami += i
#         return jami / len(self.baholar)
    
#     def malumot(self):
#         print(f"{self.ism} - {self.yosh} {self.ortacha()}")




# class Guruh:
#     def __init__(self, nom):
#         self.nom = nom
#         self.talabalar = []

#     def talaba_qosh(self,talaba):
#         self.talabalar.append(talaba)

#     def ortacha(self):
#         gurux_ortacha = 0 
#         for t in self.talabalar:
#             gurux_ortacha += t.ortacha()
#         return gurux_ortacha / len(self.talabalar)

#     def eng_yaxshi(self):
#         eng_yaxshi_1 = self.talabalar[0]
#         for i in self.talabalar:
#             if eng_yaxshi_1.ortacha() < i.ortacha():
#                 eng_yaxshi_1 = i
#         return eng_yaxshi_1.ism


# t1 = Talaba("Ali", 20)
# t1.baho_qosh(5); t1.baho_qosh(5)

# t2 = Talaba("Vali", 22)
# t2.baho_qosh(3); t2.baho_qosh(4)

# g = Guruh("101")
# g.talaba_qosh(t1)
# g.talaba_qosh(t2)

# print(g.ortacha())      # 4.25
# print(g.eng_yaxshi())   # Ali