class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self.baholar = []

    def baho_qosh(self, baho):                    # ← qo'shildi
        self.baholar.append(baho)
    @staticmethod
    def yoshni_tekshir(yosh):
        return 0 < yosh <= 120
            
    @property
    def ortacha(self):
        if not self.baholar:
            return 0
        return sum(self.baholar) / len(self.baholar)

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


class Guruh:
    def __init__(self, nom):
        self.nom = nom 
        self.talabalar = []

    def talaba_qosh(self,talaba):
        self.talabalar.append(talaba)
    @property
    def ortacha(self):
        if not self.talabalar:
            return 0
        gurux_ortacha = 0 
        for bal in self.talabalar:
            gurux_ortacha += bal.ortacha
        return gurux_ortacha / len (self.talabalar)
    
    def eng_yaxshi(self):
        if not self.talabalar:
            return None
        eng_yaxshi_1 = self.talabalar[0]
        for i in self.talabalar:
            if eng_yaxshi_1.ortacha < i.ortacha:
                eng_yaxshi_1 = i
        return eng_yaxshi_1.ism

    def __str__(self):
        return f'{self.nom}- guruh ({len(self.talabalar)} ta talaba)'        

class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

    def __str__(self):
        return f"{self.nom} - {self.narx} so'm"

    def __repr__(self):
        return f"Mahsulot('{self.nom, self.narx}')"     

    def __eq__(self, value):
        return self.narx == value.narx 

    @property
    def narx(self):
        return self._narx
    
    @narx.setter
    def narx(self, qiymat):
        if not qiymat >= 0:
            raise ValueError("qiymat mos emas.")
        self._narx = qiymat




class Savat:
    def __init__(self):
        self.mahsulotlar = []

    def qosh(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    @property
    def jami(self):
        jami_narx = 0
        for m in self.mahsulotlar:
            jami_narx += m.narx

        return jami_narx

    def __str__(self):
        return f"Savat: {len(self.mahsulotlar)} ta mahsulot, jami: {self.jami} so'm"

    def __repr__(self):
        return f"Savat({len(self.mahsulotlar)} ta mahsulor)"


t1 = Talaba("Ali", 20)
t1.baho_qosh(5)
t1.baho_qosh(5)
print(Talaba.yoshni_tekshir(20))    # True
print(Talaba.yoshni_tekshir(-5))    # False