
a = [1, -2, 8, 6, 5, 11, 3, 7]


def maximum(a):
    max = a[0]
    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]
    return max


def minimum(a):
    min = a[0]
    for i in range(1, len(a)):
        if a[i] < min:
            min = a[i]
    return min


print("Maximum value is: ", maximum(a))
print("Minimum value is: ", minimum(a))
