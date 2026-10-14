mahsulotlar = {
    
        "mevalar" :
            [
                {"Nomi" : "olma","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "bonon","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "limon","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "sd","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "sdgfsdfg","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12}
            ],

    
        "sabzavot":
            [
                {"Nomi" : "sgsdg","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "sdfg","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "sdgf","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "sdfg","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "sdgf","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "sdfg","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12}
            ],
    

    
        "poliz ekinlari" :
            [
                {"Nomi" : "sdgf","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "sgdf","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "sfdg","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "hgj","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "fgh","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
                {"Nomi" : "hgj","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12}
                    
            ]
    

}
nima_olmoqchisiz = str(input("Hello gays. Nima kerak? asosiy menyu: mevalar, sabzavotlar, poliz ekinlari: "))
print(f"{nima_olmoqchisiz} maxsulotlarimiz.")
for kategoriya in mahsulotlar[nima_olmoqchisiz]:
    print(f"Nomi: {kategoriya["Nomi"]}, Narxi: {kategoriya["narxi"]} so'm")
hisoblash = str(input("Nima olmoqchi bo'lsangi yozing:"))
narxs = float(input("Necha kg kerak: "))
def soni_3_ga_bolish(son):
    return f"{round(son, 2):,.2f}".replace(",", " ")

def narxni_hisoblash(narx, nima, kategorya):
    for kategoriya in mahsulotlar[kategorya]:
        if kategoriya["Nomi"] == nima:
            return f"{soni_3_ga_bolish(son=kategoriya["narxi"]*narx)} so'm boladi."

print(narxni_hisoblash(narx=narxs, nima=hisoblash, kategorya=nima_olmoqchisiz))
