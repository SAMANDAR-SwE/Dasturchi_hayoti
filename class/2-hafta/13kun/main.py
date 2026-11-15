from shakl import Shakl
from tortburchak import Tortburchak, Kvadrat
from sozlamalar import Sozlamalar


print("=== 1. Oddiy shakllar ===")
k = Kvadrat(5)
print(k)                       # Kvadrat(yuza=25.00)
print(k.perimetr())            # 20.0

t = Tortburchak(3, 4)
print(t)                       # Tortburchak(yuza=12.00)
print(t.perimetr())            # 14.0

print("\n=== 2. Fabrika ===")
s1 = Shakl.fabrika("kvadrat", 2)
s2 = Shakl.fabrika("tortburchak", 2, 3)
print(s1, s2)

try:
    Shakl.fabrika("doira", 5)
except ValueError as e:
    print("Xato:", e)          # Noma'lum shakl turi: doira

print("\n=== 3. Abstrakt class ===")
try:
    Shakl()
except TypeError as e:
    print("Xato:", e)          # Can't instantiate abstract class

print("\n=== 4. Validatsiya ===")
try:
    t.eni = -1
except ValueError as e:
    print("Xato:", e)          # Eni musbat bo'lishi kerak

print("\n=== 5. __slots__ ===")
try:
    t.yangi = 5
except AttributeError as e:
    print("Xato:", e)          # 'Tortburchak' object has no attribute 'yangi'

print("\n=== 6. Singleton ===")
a = Sozlamalar("uz", "so'm")
b = Sozlamalar("en", "dollar")
print(a is b)                  # True
print(a)                       # Sozlamalar(til='uz', valyuta="so'm") — o'zgarmadi!