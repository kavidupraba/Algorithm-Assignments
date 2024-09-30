import random
import time


def _quicksort(a,lo,hi):
    _qsort(a,lo,hi)

def _qsort(a,lo,hi):
    if lo>=hi:
        return
    _pivot(a,lo,hi)
    i=_partition(a,lo,hi)
    _qsort(a,lo,i-1)
    _qsort(a,i+1,hi)


def _swap(a,i,j):
    a[i],a[j]=a[j],a[i]


def _pivot(a,lo,hi):
    mid=(lo+hi)//2
    if a[mid]<a[lo]:
        _swap(a,mid,lo)
    if a[hi]<a[lo]:
        _swap(a,hi,lo)
    if a[hi]<a[mid]:
        _swap(a,hi,mid)

def _partition(a,lo,hi):
    m=(lo+hi)//2
    pviot=a[m]
    _swap(a,m,hi-1)
    i=lo
    j=hi-1
    while i<j:# i,j always stay outside of the pivot point (pivot index)
        # that means they should never cross each other i should stay left side of the pivot point
        # while j should stay right side of the pivot point(pivot index) PIVOT INDEX WILL BE THE i value when
        # wile loop stop i  stop facing larger element to the pivot point and we replaced pivot at hi-1
        while i<j and a[i]<=pviot:
            i+=1
        while i<j and pviot<=a[j]:
            j-=1

        _swap(a,i,j)

    _swap(a,i,hi-1)

    return i

def tabulate_T_n(start, times):
    table=[]
    for t in range(times+1):
        size=start*(2**t)
        total_time=0
        for _ in range(10):
            a=random.sample(range(size*2),size)
            starting_time=time.time()
            _quicksort(a, 0, len(a) - 1)
            ending_time=time.time()
            total_time+=ending_time-starting_time
        avg_time=total_time/10
        table.append((size,avg_time))
    return table


def main():
    start=10
    times=10
    table=tabulate_T_n(start,times)
    print(table)

if __name__=="__main__":
    main()