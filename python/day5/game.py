import random

def game(character, monster):
    while monster>0:
          monster = monster - character*(random.randint(8,12)/10)
          print("canavarın canı: ", monster)
          i=+1
          if monster<0:
               print("canavar öldü")
    print(f"canavar {i} vuruşta öldü ")


game(int(input("karakterin canı: ")),int(input("canavarın canı: ")))
