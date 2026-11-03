from kun_3 import Talaba
from kun_2 import Mahsulot


# Mahsulot __eq__ sinovi
m1 = Mahsulot("Non", 5000)
m2 = Mahsulot("Sut", 5000)
m3 = Mahsulot("Olma", 8000)

print(m1 == m2)   # True
print(m1 == m3)   # False


# Talaba __eq__ sinovi
t1 = Talaba("Ali", 20)
t2 = Talaba("Ali", 20)
t3 = Talaba("Vali", 22)

print(t1 == t2)   # True
print(t1 == t3)   # False


# Talaba __lt__ sinovi
t1.baho_qosh(5)
t3.baho_qosh(3)

print(t1 < t3)    # False (5.0 < 3.0 emas)
print(t3 < t1)    # True ✅


# sorted() sinovi
t4 = Talaba("Hasan", 19)
t4.baho_qosh(4)

talabalar = [t1, t3, t4]
tartiblangan = sorted(talabalar)
for t in tartiblangan:
    print(t.ism, t.ortacha())