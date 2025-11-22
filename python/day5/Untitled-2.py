dosya = open("a.txt", "w")
dosya.write("asdadn\n")
dosya.close()


dosya = open("a.txt", "r")
print(dosya.readline(123))
