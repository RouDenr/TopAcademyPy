
def move_zeros(arr):
    count_z = 0
    i = 0
    for j in arr:
        if j != 0:
            arr[i] = j
            i += 1
        else:
            count_z += 1

    for i in range(len(arr) - 1, len(arr) - count_z - 1, -1):
        arr[i] = 0


arr = [0, 0, 1, 0, 5 ,0, 4, 11]

move_zeros(arr)

print(arr)
