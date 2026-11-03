class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self.baholar = []
    def __str__(self):
        return f"{self.ism} ({self.yosh} yosh)"

    def __repr__(self):
        return f"Talaba('{self.ism}', {self.yosh})"   # ← class nomi bor
    
    def baho_qosh(self, baho):
        self.baholar.append(baho)

    def ortacha(self):
        if not self.baholar:
            return 0

        jami = 0
        for i in self.baholar:
            jami += i
        return jami / len(self.baholar)
    
    def malumot(self):
        print(f"{self.ism} - {self.yosh} {self.ortacha()}")

    def __eq__(self, value):
        return self.ism == value.ism and self.yosh == value.yosh

    def __lt__(self, other):
        return self.ortacha() < other.ortacha()


class Guruh:
    def __init__(self, nom):
        self.nom = nom
        self.talabalar = []

    def __str__(self):
        return f"{self.nom} ({len(self.talabalar)} ta talaba)"

    def talaba_qosh(self,talaba):
        self.talabalar.append(talaba)

    def ortacha(self):
        if not self.talabalar:
            return 0
        gurux_ortacha = 0 
        for t in self.talabalar:
            gurux_ortacha += t.ortacha()
        return gurux_ortacha / len(self.talabalar)

    def eng_yaxshi(self):
        if not self.talabalar:
            return None
        eng_yaxshi_1 = self.talabalar[0]
        for i in self.talabalar:
            if eng_yaxshi_1.ortacha() < i.ortacha():
                eng_yaxshi_1 = i
        return eng_yaxshi_1.ism

