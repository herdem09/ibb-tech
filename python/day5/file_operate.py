def write(filename, write):
    file = open(filename, "w")
    file.write(write)
    file.close()


def read(filename):
    file = open(filename, "r+")
    return(file.readlines())
    file.close()


write(input("File name: "), input("What to write: "))
print(read(input("File name: ")))