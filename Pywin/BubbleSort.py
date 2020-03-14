lis = [200, 100, 400, 600, 900, 300]

'''
def BubbleSort(lis):
    for i in range(len(lis) - 1, 0, -1):
        for j in range(i):
            if lis[j] > lis[j + 1]:
                temp = lis[j]
                lis[j] = lis[j + 1]
                lis[j + 1] = temp
            print(lis)

(BubbleSort(lis))
print(lis)'''

l = [4, 3, 2, 1, 7, 5]


def selsort(l):
    for i in range(6):
        min = i;
        for j in range(i, 6):
            if l[j] < l[min]:
                min = j
        temp = l[i]
        l[i] = l[min]
        l[min] = temp


selsort(l)
print(l)
