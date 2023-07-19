#array1 = [8,1,3,5,7,2,9,7,0,22,45,11]
array1 = ['mat','cat','bat']
n = len(array1)

for i in range(0,n):
    for j in range(i+1, n):
        if array1[i] > array1[j]:
            temp = array1[i]
            array1[i] = array1[j]
            array1[j] = temp

print(array1)