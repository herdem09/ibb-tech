'''
input = str(input("enter the number"))
a = 0
for i in input:
    if i:
        a = a + 1
print(a)
'''

input = int(input("enter the number"))
a = 0

while input != 0:
    number = input//10
    a = a + 1
print(a)