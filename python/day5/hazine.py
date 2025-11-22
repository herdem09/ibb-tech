import random

harita = ["mağara", "orman", "göl", "kale", "çiftlik", "dağ", "tapınak", "köy", "çöl", "ada"]
x = random.choice(harita)
inp=""
while True:
    inp= input("hazine nerde?= ")
    if inp == x :
        print("Tebrikler hazineyi buldunuz")
        break
    else:
        print(" hazine burada değil")