def bubble_sort(array, Reversed=False):
    a = array
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if not Reversed:
                if a[j - 1] > a[j]:
                    a[j], a[j - 1] = a[j - 1], a[j]
            else:
                if a[j - 1] < a[j]:
                    a[j], a[j - 1] = a[j - 1], a[j]
    return a
