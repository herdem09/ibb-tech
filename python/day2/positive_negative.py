numbers = [0, 1, 99, -3, -7]
a = 0
b = 0
c = 0
for i in numbers:
    if i > 0:
        a = a+1
    elif i < 0:
        b = b+1
    else:
        c = c+1
print(f"positive: {a}")
print(f"negative: {b}")
print(f"zero: {c}")
