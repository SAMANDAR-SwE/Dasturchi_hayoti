import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()

try:
    connection = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

    cursor = connection.cursor()
    
    select_query = "SELECT id, nomi, narxi, shelf_life, per_piece, category FROM mahsulotlar;"
    cursor.execute(select_query)
    mahsulotlar = cursor.fetchall()
    for row in mahsulotlar:
        print(f"{row[0]:<4} | {row[1]:<28} | ${row[2]:<9} | {row[3]:<6} | {row[4]:<12}")
    print("-" * 80)

except (Exception, psycopg2.Error) as error:
    print("Xatolik yuz berdi:", error)

finally:
    # 6. Ulanishlarni har doim yopish shart
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("\nPostgreSQL ulanishi yopildi.")


# mahsulotlar = {
    
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
