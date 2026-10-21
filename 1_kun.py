# mahsulotla = {
    
#         "mevalar" :
#             [
#                 {"Nomi" : "olma","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "bonon","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "limon","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "sd","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "sdgfsdfg","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12}
#             ],

    
#         "sabzavot":
#             [
#                 {"Nomi" : "sgsdg","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "sdfg","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "sdgf","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "sdfg","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "sdgf","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "sdfg","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12}
#             ],
    

    
#         "poliz ekinlari" :
#             [
#                 {"Nomi" : "sdgf","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "sgdf","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "sfdg","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "hgj","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "fgh","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12},
#                 {"Nomi" : "hgj","narxi" : 30000, "yaroqlilik muddati" : "12-12-2026", "miqdori" : 12}
                    
#             ]
    

# }


import json



with open("test.json", "r", encoding="utf-8") as f:
    # json.dump(mahsulotlar, f, ensure_ascii=False, indent=2)
    mahsulotlar = json.load(f)



def soni_3_ga_bolish(son):
    return f"{round(son, 2):,.2f}".replace(",", " ")

def narxni_hisoblash(narx, nima, kategorya):
    for kategoriya in mahsulotlar[kategorya]:
        if kategoriya["Nomi"] == nima:
            return f"{soni_3_ga_bolish(son=kategoriya["narxi"]*narx)} so'm boladi."

    return "Topilmadi"

def mahsulotni_chiqarish():
    kategoriya = input("Kategoriya (mevalar, sabzavot, poliz ekinlari):")
    if kategoriya not in mahsulotlar:
        print("Bunday kategoriya yo'q.")
        return None
    
    print(f"{kategoriya} maxsulotlarimiz.")
    
    for m in mahsulotlar[kategoriya]:
        print(f"  {m['Nomi']} - {m['narxi']} so'm")
    return kategoriya   
    


while True:
    print("\n1. Mahsulotlarni ko'rish")
    print("2. Narx hisoblash")
    print("3 Savat")
    print("0. Chiqish")
    tanlov = input("Tanlang: ")

    if tanlov == "0":
        break
    elif tanlov == "1":
        mahsulotni_chiqarish()
    elif tanlov == "2":
        nima_olmoqchisiz = mahsulotni_chiqarish()
        if nima_olmoqchisiz is None:
            continue
        try:
            hisoblash = input("Nima olmoqchi bo'lsangi yozing:")
        except:
            print("No to'g'ri ma'lumot.")
        try:
            narxs = float(input("Necha kg kerak: "))
            print(narxni_hisoblash(narx=narxs, nima=hisoblash, kategorya=nima_olmoqchisiz))
        except ValueError:
            print("Xatto ma'lumot kirizdingiz.")
    elif tanlov == "3":
        while True:
            print("\n--- SAVAT ---")
            print("1. Savatga qo'shish")
            print("2. Savatni ko'rish")
            print("3. Savatni tozalash")
            print("0. Orqaga")
            savat_tanlov = input("Tanlang: ")
            
            if savat_tanlov == "0":
                break
            elif savat_tanlov == "1":
                kategoriya = input("Kategoriya: ").strip()
                nomi = input("Nomi: ").strip()
                try:
                    kg = float(input("Necha kg: "))
                    narxi = float(input("Narxi: "))
                except ValueError:
                    print("Son kiriting.")
                    continue
                yaroq = input("Yaroqlilik muddati: ").strip()
            
                mahsulot = {"Nomi": nomi, "narxi": narxi, "yaroqlilik muddati": yaroq, "miqdori": kg}
                mahsulotlar.setdefault(kategoriya, []).append(mahsulot)
            
                with open("test.json", "w", encoding="utf-8") as f:
                    json.dump(mahsulotlar, f, ensure_ascii=False, indent=2)
                print("Qo'shildi.")
            elif savat_tanlov == "2":
                try:
                    with open("test.json", "r", encoding="utf-8") as f:
                        data = json.load(f)

                    print("\n--- SAVATDAGI BARCHA MAHSULOTLAR ---")
                    for kat_nomi, elementlar in data.items():
                        print(f"\n--- {kat_nomi.upper()} ---")
                        for mahsulot in elementlar:
                            print(
                                f"Nomi: {mahsulot['Nomi']}, "
                                f"Narxi: {mahsulot['narxi']} so'm, "
                                f"Muddati: {mahsulot['yaroqlilik muddati']}, "
                                f"Miqdori: {mahsulot['miqdori']}"
                            )
                except FileNotFoundError:
                    print("Fayl topilmadi.")
                            

            elif savat_tanlov == "3":
                # savat.clear()
                print("Savat tozalandi")
            else:
                print("Noto'g'ri tanlov")
    else:
        print("Noto'g'ri tanlov")
