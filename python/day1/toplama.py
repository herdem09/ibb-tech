num = int(input("Enter the number:  "))
even = 0
odd = 0
for i in range(0, num+1):
    if i % 2 != 0:
        odd = i+odd
    else:
        even = i+even

print(odd)
print(even)

