ilk = float(input("ilk marketteki fiyat: "))
ikinci = float(input("ikinci marketteki fiyat:  "))
if ilk < ikinci:
    print("ilk daha ucuz")
if ilk == ikinci:
    print("esit")
if ilk > ikinci:
    print("ikinci daha ucuz")
else:
    print("fiyatı doğru gir")