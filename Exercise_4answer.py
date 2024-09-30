import random
import time


def quicksort(a):
    _qsort(a, 0, len(a) - 1)


def _qsort(a, lo, hi):
    # For small arrays insertion sort is to be prefered: no recursion.
    # The implementation of sorted in Python uses insertion sort
    # for arrays of length less than 64. So we can use that.
    # The base case is then
    #     if lo + 64 > hi: a[lo:hi+1] = sorted(a[lo:hi+1])

    # but, at least three elements for the base case
    # (think of partition, needs 3 elements to work properly)

    if lo + 64 > hi:
        a[lo:hi + 1] = sorted(a[lo:hi + 1])
    else:
        _pivot(a, lo, hi)
        i = _partition(a, lo, hi)
        _qsort(a, lo, i - 1)
        _qsort(a, i + 1, hi)


# Now the functions we studied in the previous exercises.
# Here with names as auxiliary functions (starting with _)
# Also, we use the name _pivot instead of sort_three because it could be
# some other function than median of three!
# For example, you could pick a random value in the slice as pivot!

def _swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def _pivot(a, lo, hi):
    mid = (lo + hi) // 2
    # sort lo, mid, hi:
    if a[mid] < a[lo]:
        _swap(a, lo, mid)
    if a[hi] < a[lo]:
        _swap(a, lo, hi)
    if a[hi] < a[mid]:
        _swap(a, mid, hi)


def _partition(a, lo, hi):
    # place the pivot out of the way, in position hi -1
    mid = (lo + hi) // 2
    _swap(a, mid, hi - 1)

    # initialize the indices to walk through the array from low to high and from hight to low
    i = lo
    j = hi - 1
    pivot = a[j]

    # the algorithm that Tim explains
    while True:
        while True:
            i += 1
            if a[i] >= pivot: break

        while True:
            j -= 1
            if a[j] <= pivot: break

        if i >= j: break
        _swap(a, i, j)

    # put the pivot in place and return the position of the pivot
    _swap(a, i, hi - 1)
    return i
def tabulate_T_n(start, times):
    table=[]
    for t in range(times+1):
        size=start*(2**t)
        total_time=0
        for _ in range(10):
            a=random.sample(range(size*2),size)
            starting_time=time.time()
            quicksort(a)
            ending_time=time.time()
            total_time+=ending_time-starting_time
        avg_time=total_time/10
        table.append((size,avg_time))
    return table


def main():
    start=800
    times=10
    table=tabulate_T_n(start,times)
    print(table)
    filename="Exercise.txt"
    with open(filename,"a") as f:
        print(table,file=f)

if __name__=="__main__":
    main()