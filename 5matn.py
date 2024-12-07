"""
8/11/2020

Dasturlash asoslari

#05-dars: STRING (MATN)

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"

# # Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# # Diqqat uzun kodlarni \ belgisi yordamida keyingi qatorga
# # ko'chirish mumkin
# print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
#       tuman + " tumani, " + viloyat + " viloyati")

# #Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
# print("Iltimos, quyidagi ma'lumotlarni kiriting:")
# kocha = input("Ko'changiz: ")
# mahalla = input("Mahallangiz: ")
# tuman = input("Tumaningiz: ")
# viloyat = input("Viloyatingiz: ")
# print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
#       tuman + " tumani, " + viloyat + " viloyati")   

# # Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing
# print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
#       tuman + " tumani,\n" + viloyat + " viloyati")

# # Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(manzil)

# #manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.title())
# print(manzil.capitalize())


# name = "Saidahmad"
# surname = "Murodullayev"
# full_name=f"ism {name} familiya {surname}"
# print(full_name.upper()) # .upper() metodi terminalga kotta harfda chiqaradi


# name = "Saidahmad"
# surname = "Murodullayev"
# full_name=f"ism {name} familiya {surname}"
# print(full_name.lower()) # .lower() metodi terminalga kotta harfda chiqaradi


# name = "Saidahmad"
# surname = "Murodullayev"
# full_name=f"ism {name} familiya {surname}"
# print(full_name.title()) # .title() metodi Har bitta so'zni birinchi harfini kotta harfda terminalga chiqaradi


# name = "Saidahmad"
# surname = "Murodullayev"
# full_name=f"ism {name} familiya {surname}"
# print(full_name.capitalize()) # .capitalize() metodi har bitta matnni birinchi so'zni kotta harfda chiqaradi

# name = "Saidahmad"
# surname = "Murodullayev"
# full_name=f"ism {name} familiya {surname}"
# print(full_name.lstrip()) # .lstrip() metodi chap tarafdagi bo'shliqni olib tashlab terga chiqaradi


# name = "Saidahmad"
# surname = "Murodullayev"
# full_name=f"ism {name} familiya {surname}"
# print(full_name.rstrip()) # .rstrip() metodi o'ng tarafdagi bo'shliqni olib tashlab terga chiqaradi


# name = "Saidahmad"
# surname = "Murodullayev"
# full_name=f"ism {name} familiya {surname}"
# print(full_name.strip()) # .strip() metodi hamma bo'shliqni olib tashlab terga chiqaradi


# '''Input'''

# name = input("Ismingizni kiriting: ")
# print("Assalomu alykum :" + name)



#Amaliyot
# print("Iltimos quyidagi savollarga javob bering")
# kocha=input("Ko\'changizni kiriting:")
# mahalla=input("Mahallangizni kiriting:")
# tuman=input("Tumaningizni kiriting:") 
# viloyat=input("Viloyatingizni kiriting:")
# print(f"{kocha.upper()} ko\'chasi ,{mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

manzil=f"Bog\'bon ko'chasi, Sog\'bon mahallasi, Bodomzor tumani, Samarqand viloyati"
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())
print(manzil.lstrip())
print(manzil.rstrip())
print(manzil.strip())


