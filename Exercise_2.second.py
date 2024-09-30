import random

def swap(a,i,j):
    a[i],a[j]=a[j],a[i]

def sort_three(a,low,high):
    mid=(low+high)//2

    while not(a[low]<a[mid]<a[high]):
        if a[low] > a[mid]:
            a[low], a[mid] = a[mid], a[low]

        if a[low] > a[high]:
            a[low], a[high] = a[high], a[low]

        if a[mid] > a[high]:
            a[mid], a[high] = a[high], a[mid]


# Before start we know that a[lo] <= a[mid] <= a[hi]

def partition(a, lo, hi):
    # Place the pivot out of the way, in position hi - 1
    # The element in position hi is >= pivot so we keep it there!
    mid = (lo + hi) // 2
    swap(a, mid, hi - 1)

    # initialize the indices to walk through the array from low to high and from hight to low
    # i starts from the left
    i = lo

    # j starts from the right
    j = hi - 1

    pivot = a[j]

    # the algorithm that Tim explains
    while True:
        while True:
            i += 1
            if a[i] >= pivot: break
        # here you know that a[i] >= pivot!

        while True:
            j -= 1
            if a[j] <= pivot: break
        # here you know that a[i] >= pivot and a[j] <= pivot

        if i >= j: break  # you are done if the indices have crossed each other!

        # here you know that a[i] >= pivot and a[j] <= pivot and i < j!
        swap(a, i, j)

    # put the pivot in its place and return the position of the pivot
    swap(a, i, hi - 1)
    for i in range(lo,hi):
        if pivot==a[i]:
            return i

def main():

        test_case = list(range(10))
        i = 0
        j = 9

        random.shuffle(test_case)
        sort_three(test_case,i,j)
        print(test_case)
        answer=partition(test_case, i, j)
        print(answer)
        print(test_case[answer])
        print((test_case))




if __name__=="__main__":
    main()