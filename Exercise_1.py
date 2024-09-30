import random

def swap(a,i,j):
    a[i],a[j]=a[j],a[i]

def sort_three(a=[2,4,1,3,5]):
    n=len(a)-1
    mid=n//2
    if a[mid]<a[0]:
        swap(a,0,mid)
    if a[n]<a[0]:
        swap(a,0,n)
    if a[n]<a[mid]:
        swap(a,mid,n)
    return [a[0],a[mid],a[n]]

def main():
    ch=int(input("enter your set size:"))
    arr=[]
    for _ in range(ch):
        arr.append(int(input("enter your element: ")))

    print(sort_three(arr))



if __name__=="__main__":
    main()