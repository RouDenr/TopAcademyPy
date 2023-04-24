
arr = [1,2,1,4,3,2,1,4]
w = 8
maxArea = 0


i = 0
j = len(arr) - 1

while j > i:
    maxArea = max(maxArea, min(arr[i], arr[j]) * (j - i))
    if (arr[i] < arr[j]):
        i +=1
    else:
        j -=1

print(maxArea)
