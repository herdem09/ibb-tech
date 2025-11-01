ogrenciler = [
    {"isim": "Ahmet", "not": 85},
    {"isim": "Ayşe", "not": 92},
    {"isim": "Mehmet", "not": 78},
    {"isim": "Fatma", "not": 95},
    {"isim": "Ali", "not": 88}
]

grades = []
for ogrenci in ogrenciler:
    isim = ogrenci["isim"]
    notu = ogrenci["not"]
    if notu < 85:
        print(isim, "başarısız")
    else:
        print(isim, "başarılı")
    grades.append(notu)

ortalama = sum(grades) / len(grades)
print("Sınıf ortalaması:", ortalama)
