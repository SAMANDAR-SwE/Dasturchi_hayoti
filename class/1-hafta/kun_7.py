class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self.baholar = []

    def baho_qosh(self, baho):                    # ← qo'shildi
        self.baholar.append(baho)
    
    @property
    def ortacha(self):
        if not self.baholar:
            return 0

        jami = 0
        for i in self.baholar:
            jami += i
        return jami / len(self.baholar)

    def __str__(self):
        return f"{self.ism} ({self.yosh} yosh)"

    def __repr__(self):
        return f"Talaba('{self.ism}', {self.yosh})"
    
    def __eq__(self, value):
        return self.ism == value.ism and self.yosh == value.yosh

    def __lt__(self, other):
        return self.ortacha < other.ortacha

    @property
    def yosh(self):
        return self._yosh

    @yosh.setter
    def yosh(self, qiymat):
        if not (0 < qiymat <= 120):
            raise ValueError("Yosh 0 dan katta, 120 dan kichik bo'lishi kerak")
        self._yosh = qiymat


t1 = Talaba("Ali", 20)
t1.baho_qosh(5)
t1.baho_qosh(3)

t2 = Talaba("Vali", 22)
t2.baho_qosh(4)

print(t1)                        # Ali (20 yosh)
print(repr(t1))                  # Talaba('Ali', 20)
print(t1.ortacha)                # 4.0
print(t1 < t2)                   # False (4.0 < 4.0 emas)
print(t1 == Talaba("Ali", 20))   # True

try:
    t1.yosh = 200
except ValueError as e:
    print(f"Xato: {e}")