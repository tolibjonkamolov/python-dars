"""
for BILAN TANISHAMIZ

Dasturlash davomida kodimizning biror qismini bir necha marta takrorlash talab etilishi mumkin.
Misol uchun, ro'yxat ichidagi har bir elementni alohida qatordan konsolga chiqarish, 
yoki bo'lmasa har bir elementni kvdartaga oshirish va hokazo. 

Mana shunday vaziyatlarda bizga for operatori yordam beradi. Dasturlashda bu tsikl (loop) deb ataladi.
"""



"""
Keling quyidagi misolni ko'ramiz. Bizda mehmonlar ro'yxati bor, biz har bir mehmonning ismini yangi qatordan chiqarmoqchimiz.
Buning uchun quyidagi kodni yozamiz:
"""

# mehmonlar = ["Ali", "Vali", "G'ani", "Xasan", "Xusan", "Olim", "Sobir", "Kamol", "Jamol"]
# for mehmon in mehmonlar:
#     print("Assalomu alekum", mehmon)

"""
Keling, kodni tahlil qilaylik. 
1-qatorda biz mehmonlar degan ro'yxat yaratdik va uni mehmonlarning ismi bilan to'ldirdik.

2-qatorda for tsiklini bohladik. Bu qator Pythonga mehmonlar degan ro'yxatdan har bir elementini olib uni yangi,
mehmon degan o'zgaruvchiga yuklashni buyuryapti (o'zgaruvchiga istalgan nom berishingiz mumkin.
Biz tushunarli bo'lishi uchun mehmon deb atadik)

3-qatorda biz mehmon degan o'zgaruvchining qiymatini konsolga chiqardik.
Bu tsikl to mehmonlar ro'yxatida elementlar tugagunga qadar takrorlanadi.
"""

"""
"For" so'zi ingliz tilidan "uchun" deb tarjima qilinadi.

Yuqoridagi kodni oddiy tilga tarjima qilsak "Mehmonlar ro'yxatidagi har bir mehmon uchun uning ismini konsolga chiqar" degan ma'noni beradi.
"""




"""
for QANDAY ISHLAYDI:
Keling yana bir misol ko'raylik. 
"""

# mehmonlar = ["Ali", "Vali", "G'ani", "Xasan", "Xusan", "Olim", "Sobir", "Kamol", "Jamol"]
# for mehmon in mehmonlar:
#     print("Assalomu alekum ", mehmon, "Sizni 4 - dekabr kuni to'yga kaklif etamiz")
#     print("Hurmat bilan Qodirovlar oilasi\n")

"""
Agar biron bir so'zni faqat birmartta chiqarmoqchi bo'lsak bu so'zni sikldan tashqarrida qoldiramiz

Misol:
"""

# for i in range(10):
#     print(f"Salom {i}")
# print("Bu sikldan tashqarida")


"""
for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH:

Keling quyidagi misolni ko'ramiz
"""

# sonlar = list(range(21))

# for son in sonlar:
#     print(son)

# for son in sonlar:
#     print(f"{son} ning kvadrati {son ** 2}")


""" for yordamida yangi ro'yxat ham shakllantirish mumkin: """

# sonlar = list(range(10))
# sonlar_kvadrati = []

# for son in sonlar:
#     sonlar_kvadrati.append(son**2)

# print(sonlar)
# print(sonlar_kvadrati)


"""
for va input()
for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan olingan qiymatlar bilan to'ldirish mumkin:
"""

# dostlar = [] # bo'sh ro'yxat
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)

"""
Kodni tahlil qilamiz:
1-qatorda bo'sh dostlar ro'yxatini yaratdik
2-qatorda ekranga "5 ta eng yaqin do'stingiz kim?" degan xabarni chiqardik
3-qatorda tsiklni boshladik. range(5) funktsiyasi 0 dan 5 gacha sonlar ketma-ketligini yaratadi (0,1,2,3,4) tsikl esa n shularning har biriga teng bo'lib chiqquncha davom etadi. 
4-qatorda tsikl badani kelgan. Bu yerda biz foydalanuvchidan n+1 do'stingizni kiriting deb so'radik. Nima uchun n+1 (n emas)? Sababi n 0 dan 4 gacha qiymatlarni oladi, foydalanuvchiga tushunarli bo'lishi uchun esa biz "0-do'stingizni ismini kiriting:" deb emas, balki n+1 ya'ni 1-ismni kiriting deb murojat qilyapmiz.
5-qatorda shakllangan ro'yxatni konsolga chiqardik.
"""


""" AMALIYOT """


"""
Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing

Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring
(n o'rniga kod necha marta takrorlanganini yozing)
"""

# ismlar = ["Ali", "Vali", "G'ani", "Soli", "Hasan", "Husan"]
# for ism in ismlar:
#     print(f"Assalomu alekum {ism}")
# print(len(ism))


"""
10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
"""

# raqamlar = list(range(1,100,2))
# for raqam in raqamlar:
#     print(raqam ** 3)


"""
Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
"""

# kinolar = []
# print("5 ta Sevimli kinoyingiz nomi: ")

# for i in range(5):
#     kinolar.append(input(f"{i+1} Sevimli kino nomi: "))

# print(kinolar)


"""
Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang,
va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
"""

# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# print(ismlar)