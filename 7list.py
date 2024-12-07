# # """
# # 23/11/2024

# # Dasturlash asoslari

# # #07-dars: Lists

# # Muallif: Anvar Narzullaev

# # """
# # #ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# # ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
# # #Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
# # print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
# # print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
# # print(ismlar[-1] + " g'ildirakni g'izillatib g'ildratti")

# # # sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
# # sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
# # print(sonlar)

# # # Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
# # sonlar[0] = sonlar[0]+sonlar[-1]
# # sonlar[1] = -67.8
# # sonlar[4] = sonlar[4] + 37
# # del sonlar[5]
# # print(sonlar)

# # #t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# # t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
# # z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']

# # #Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
# # print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
# # zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
# # suhbat qilishni istar edim\n")

# # #friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
# # friends = []
# # friends.append('John')
# # friends.append('Alex')
# # friends.append('Danny')
# # friends.append('Sobirjon')
# # friends.append('Vanya')
# # print(friends)

# # #Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
# # friends.remove('John')
# # friends.remove('Alex')
# # print(friends)

# # #Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# # friends.append('Hasan')
# # friends.insert(0, 'Husan')
# # friends.insert(2, 'Ivan')
# # print(friends)

# # #Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# # mehmonlar = []
# # mehmonlar.append(friends.pop(3))
# # mehmonlar.append(friends.pop(-1))
# # mehmonlar.append(friends.pop(0))
# # print("\nKelgan mehmonlar: ", mehmonlar)



# #7 Dars

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat
# print(mevalar[0])

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())

# narhlar = [12000, 18000, 10900, 22000]
# print(narhlar[2] + narhlar[3])

# car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 

# #Elementlarni o'zgartirish
# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
# print(narhlar)



# #append -> element qo'shish(oxiriga qo'shadi)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append('qizil')
# print(mevalar)
# #N_2
# cars = [] # bo'sh ro'yxat yaratamiz
# cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# print(cars)

# #insert -> elementni ro'yxatga qo'shish(xoxlagan indexda qo'shish mumkun)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.insert(1, 'qizil')
# print(mevalar)


# #extend -> listlarni bir qayta birga o'zgartirish

# mevalar1 = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar2 = ['qizil', 'yashil', 'sari']
# mevalar1.extend(mevalar2)
# print(mevalar1)

# #N_2
# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
# print(cars)


# #remove -> elementni o'chirish

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.remove('anjir')
# print(mevalar)





# #pop -> elementni o'chirish va qaytarish

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.pop(1)
# print(mevalar)









# #index -> elementning ro'yxatdagi indeksi qaytarish

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# print(mevalar.index('anjir'))




# #count -> elementning ro'yxatdagi qismlar soni qaytarish

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anjir']
# print(mevalar.count('anjir'))


# """
# 23/11/2024

# Dasturlash asoslari

# #08-dars: Ro'yxatlar bilan ishlash

# Muallif: Anvar Narzullaev

# """
# #O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# davlatlar = ["O'zbekiston","Qozog'iston", "Rossiya", "Malayziya", "Singapur", "AQSh"]
# print(davlatlar)

# #Ro'yxatning uzunligini konsolga chiqaring
# print(len(davlatlar))

# #sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(davlatlar))

# #sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(sorted(davlatlar, reverse=True))

# #Asl ro'yxatni qaytadan konsolga chiqaring
# print(davlatlar)

# #reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print(davlatlar)

# #sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

# #120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# sonlar = list(range(120,1200,2))

# #Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print(sum(sonlar))

# #Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# print(max(sonlar)-min(sonlar))

# #Ro'yxatdagi elementlar sonini hisoblang
# print(len(sonlar))

# #Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# print(sonlar[:20])
# print(sonlar[-20:])
# print(sonlar[530:550])

# #taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# taomlar = ['osh','somsa','norin','shashlik','qozonkabob']

# #nonushta degan yangi ro'yxatga taomlardan nusxa oling
# nonushta = taomlar[:]

# #Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
# nonushta.remove('norin')
# nonushta.remove('shashlik')
# nonushta.remove('qozonkabob')
# nonushta.append('non va qaymoq')
# nonushta.append('issiq non')

# #Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# print(taomlar)
# print(nonushta)

# #Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
# nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non"


