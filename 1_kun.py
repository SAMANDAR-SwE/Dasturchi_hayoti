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


import json



with open("test.json", "r", encoding="utf-8") as f:
    # json.dump(mahsulotlar, f, ensure_ascii=False, indent=2)
    mahsulotlar = json.load(f)

    for kategoriya in mahsulotlar:
        print(kategoriya)


# def soni_3_ga_bolish(son):
#     return f"{round(son, 2):,.2f}".replace(",", " ")

# def narxni_hisoblash(narx, nima, kategorya):
#     for kategoriya in mahsulotlar[kategorya]:
#         if kategoriya["Nomi"] == nima:
#             return f"{soni_3_ga_bolish(son=kategoriya["narxi"]*narx)} so'm boladi."

#     return "Topilmadi"

# def mahsulotni_chiqarish():
#     try:
#         kategoriya = input("Kategoriya (mevalar, sabzavot, poliz ekinlari): ")
#         print(f"{kategoriya} maxsulotlarimiz.")
#         for m in mahsulotlar[kategoriya]:
#             print(f"Nomi: {m["Nomi"]}, Narxi: {m["narxi"]} so'm")
#         return kategoriya   
#     except KeyError:
#         print("No to'g'ri kategorya.")



# while True:
#     print("\n1. Mahsulotlarni ko'rish")
#     print("2. Narx hisoblash")
#     print("0. Chiqish")
#     tanlov = input("Tanlang: ")

#     if tanlov == "0":
#         break
#     elif tanlov == "1":
#         mahsulotni_chiqarish()
#     elif tanlov == "2":
#         nima_olmoqchisiz = mahsulotni_chiqarish()
#         if nima_olmoqchisiz is None:
#             continue
#         try:
#             hisoblash = str(input("Nima olmoqchi bo'lsangi yozing:"))
#         except:
#             print("No to'g'ri ma'lumot.")
#         try:
#             narxs = float(input("Necha kg kerak: "))
#             print(narxni_hisoblash(narx=narxs, nima=hisoblash, kategorya=nima_olmoqchisiz))
#         except ValueError:
#             print("Xatto ma'lumot kirizdingiz.")
#     else:
#         print("Noto'g'ri tanlov")
