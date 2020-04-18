def merge_sort(arr):

    if len(arr) > 1:

        midpoint = len(arr) // 2
        left = arr[:midpoint]
        right = arr[midpoint:]

        merge_sort(left)
        merge_sort(right)

        x = 0
        y = 0
        z = 0

        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                arr[z] = left[x]
                x += 1

            else:
                arr[z] = right[y]
                y += 1
            z += 1

        while x < len(left):
            arr[z] = left[x]
            x += 1
            z += 1

        while y < len(right):
            arr[z] = right[y]
            y += 1
            z += 1


b = [1, 2, 3]

c = [5, -9, 2, 1]

d = [777, 4324, 56243, 0, 34, 343]

print(*b)
merge_sort(b)
print(*b)

print(*c)
merge_sort(c)
print(*c)

print(*d)
merge_sort(d)
print(*d)
