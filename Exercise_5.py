import math
import random
import time
import pandas as pd
import matplotlib.pyplot as plt



def swap(a,i,j):
    a[i],a[j]=a[j],a[i]

def pviot(a,lo,hi):
    mid=(lo+hi)//2
    if a[mid]<a[lo]:
        swap(a,mid,lo)
    if a[hi]<a[lo]:
        swap(a,mid,lo)
    if a[hi]<a[mid]:
        swap(a,hi,mid)

def partition(a,lo,hi):
    mid=(lo+hi)//2
    swap(a,mid,hi-1)
    i=lo
    j=hi-1
    pviot=a[hi-1]
    while i<j:
        while i<j and a[i]<pviot:
            i+=1
        while i<j and a[j]>pviot:
            j-=1
        if i<j:
            swap(a,i,j)
    swap(a,i,hi-1)
    return i


def quick_sort(a,lo,hi):
    qsort(a,lo,hi-1)

def qsort(a,lo,hi):
    if lo+64>hi:
        a[lo:hi+1]=sorted(a[lo:hi+1])
    else:
        pviot(a,lo,hi)
        i=partition(a,lo,hi)
        qsort(a,lo,i-1)
        qsort(a,i+1,hi)
def tabulate_T_n(start, times):
    table = []
    for t in range(times):
        size = start * (2 ** t)
        total_time = 0
        for i in range(10):
            a = random.sample(range(size * 2), size)
            stime = time.time()
            quick_sort(a, 0, size)
            #print(a)
            #print(size,t,i)
            etime = time.time()
            total_time += etime - stime
        avarage_time = total_time / 10
        table.append((size, avarage_time))
    return table

def main():
    start=800
    times=10
    table=tabulate_T_n(start,times)
    extended_table=[(n,t,math.log2(n),n*math.log2(n),n**2) for n,t in table]
    extended_dic={"size":[],"average_time":[],"BigO(log2n)":[],"Bigo(nlog2n)":[],"Bigo(n**2)":[]}
    for a,b,c,d,e in extended_table:
        extended_dic["size"].append(a)
        extended_dic["average_time"].append(b)
        extended_dic["BigO(log2n)"].append(c)
        extended_dic["Bigo(nlog2n)"].append(d)
        extended_dic["Bigo(n**2)"].append(e)
    table_pd=pd.DataFrame(data=extended_dic)#creating dataframe using pandas

    normalize_table=table_pd.copy()#copying those data frame to new data frame
    # (to normalize data) we do this if deference between scales are too large

    normalize_table["average_time"] /= normalize_table["average_time"].max()
    normalize_table["BigO(log2n)"] /= normalize_table["BigO(log2n)"].max()
    normalize_table["Bigo(nlog2n)"] /= normalize_table["Bigo(nlog2n)"].max()
    normalize_table["Bigo(n**2)"] /= normalize_table["Bigo(n**2)"].max()

    ax=normalize_table.plot(x="size",y=["average_time","BigO(log2n)","Bigo(nlog2n)","Bigo(n**2)"],kind='line',figsize=(10,6))

    ax.set_title("Comparison of average time with BigO complexity ")
    ax.set_xlabel("size")
    ax.set_ylabel("normalize value")
    ax.legend(["average_time","O(log2n)","O(nlog2n)","O(n**2)"])


    table_pd.plot()
    plt.show()


    print(table_pd)
    file_name="extended_tabel.txt"
    with open(file_name,'w') as f:
        print(table_pd,file=f)



if __name__=="__main__":
    main()




