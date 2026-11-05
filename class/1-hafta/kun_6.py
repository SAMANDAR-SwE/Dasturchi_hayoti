from kun_3 import Talaba
from kun_2 import Mahsulot, Savat


class Hisob:
    def __init__(self):
        self._balans = 0

    def pul_qosh(self, summa):
        self._balans += summa

    @property
    def balans(self):
        return self._balans

    @balans.setter
    def balans(self, qiymat):
        if qiymat < 0:
            raise ValueError("Balans manfiy bo'lmaydi")
        self._balans = qiymat



s = Savat()
s.qosh(Mahsulot("Non", 5000))
s.qosh(Mahsulot("Sut", 12000))

print(s.jami)      # 17000 ✅ (qavssiz)
print(s)           # Savat: 2 ta mahsulot, jami: 17000 so'm ✅
print(repr(s))   