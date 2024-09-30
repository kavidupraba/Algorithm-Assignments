import random

def swap(a,i,j):
    a[i],a[j]=a[j],a[i]

def sort_three(a,low,high):
    mid=(low+high)//2

    #while not(a[low]<a[mid]<a[high]):
    if a[low] > a[mid]:
        swap(a,low,mid)

    if a[low] > a[high]:
        swap(a,low,high)

    if a[mid] > a[high]:
        swap(a,mid,high)


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
    while i < j:  # i,j always stay outside of the pivot point (pivot index)
        # that means they should never cross each other i should stay left side of the pivot point
        # while j should stay right side of the pivot point(pivot index) PIVOT INDEX WILL BE THE i value when
        # wile loop stop i  stop facing larger element to the pivot point and we replaced pivot at hi-1
        while i < j and a[i] <= pivot:
            i += 1
        while i < j and pivot <= a[j]:
            j -= 1

        swap(a, i, j)

    swap(a, i, hi - 1)

    return i
    """while True:
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
    print(a)
    swap(a, i, hi - 1)
    print(a)
    return i"""


def main():

    #for x in range(10):
    a = list(range(2))
    i = 0
    j = 1

    random.shuffle(a)
    #print(f"\n({x+1})LIST\nbefore using sort_three")
    print(f"\nbefore using sort_three")
    r_n=len(a)-1
    r_m=(0+r_n)//2
    print(f"pivot position in the random list:{r_m}\nvalue assigned to that position: {a[r_m]}")
    print(a)
    sort_three(a,i,j)
    n=len(a)-1
    mid=(0+n)//2

    #after using sort_three()
    print("\nafter using sort_three")
    #if a[0]<a[mid]<a[n]:
    print(a)
    print(f"pivot position after using sort_three:{mid} \npivot value:{a[mid]}")
    # after using partition()
    answer=partition(a, i, j)
    print(f"\nafter using partition")
    #if a[0] < a[answer] < a[n]:
    print(f"This is pivot position:{answer}")
    print(f"This is the pivot value:{a[answer]}")
    print(a)




if __name__=="__main__":
    main()