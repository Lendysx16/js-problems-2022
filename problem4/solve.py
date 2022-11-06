num_of_stones = int(input())
arr = [int(input()) for i in range(num_of_stones)]
arr.sort()
arr1 = []
arr2 = []
for i in range(num_of_stones):
    if sum(arr1) <= sum(arr2):
        arr1.append(arr[i])
    else:
        arr2.append(arr[i])

summ1 = sum(arr1)
summ2 = sum(arr2)
if summ1 > summ2:
    if summ1 // summ2 <= 2:
        print('ДА')
    else:
        print('НЕТ')
else:
    if summ2 // summ1 <= 2:
        print('ДА')
    else:
        print('НЕТ')
