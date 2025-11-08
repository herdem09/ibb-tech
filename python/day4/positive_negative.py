positive = []
negative = []


def positive_negative(list):
    for i in list:
        if i < 0:
            negative.append(i)
        elif i > 0:
            positive.append(i)
    return positive, negative


a, b = positive_negative([2, -5, 7, -2, 8, -1])
print(f"positives: {a}")
print(f"negatives: {b}")
