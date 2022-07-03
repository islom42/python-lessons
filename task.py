""" 
- Quyidagi o'zgaruvchilarni yarating:
  `kocha="Bog'bon" mahalla="Sog'bon" tuman="Bodomzor" viloyat="Samarqand"`
  Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
  `Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati`
"""
kocha = "Bog\'bon"
mahalla = "Sog\'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
adress = f"{kocha} ko'chasi {mahalla} mahallasisi, {tuman} tumani, {viloyat} viloyati"
print(adress);

kocha = input("Ko'changizni kiriting\n>>>")
mahalla = input("Mahallangizni kiriting\n>>>")
tuman = input("Tumanni kiriting\n>>>")
viloyat = input("Viloyatni kiriting\n>>>")
adress = f"{kocha.title()} ko'chasi {mahalla.title()} mahallasi, {tuman.title()} tumani, {viloyat.title()} viloyati"
print(adress);
