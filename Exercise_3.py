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
    return i
    '''for i in range(lo,hi):
        if pivot==a[i]:
            return i'''

def main():

        a = list(range(10))
        i = 0
        j = 9

        random.shuffle(a)
        print("before using sort_three")
        print(a)
        sort_three(a,i,j)
        n=len(a)-1
        mid=(0+n)//2

        #after using sort_three()
        print("after using sort_three")
        if a[0]<a[mid]<a[n]:
            print(a)
        answer=partition(a, i, j)
        print(f"\nThis is pivot position:{answer}")
        print(f"This is the middle value:{a[answer]}\n")
        #after using partition()
        print("after using partition")
        if a[0] < a[answer] < a[n]:
           print((a))




if __name__=="__main__":
    main()