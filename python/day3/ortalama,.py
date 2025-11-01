import random
i = 0
a = 0
num_list = []

while i < 6:
    num_list.append(random.randint(1, 50))
    i = i + 1
a = sum(num_list)
a = a / 5
print(num_list, a)
