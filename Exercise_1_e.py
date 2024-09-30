def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def sort_three(a=[2,4,1,3,5]):
    n = len(a) - 1
    mid = n // 2
    count=[]

    if a[mid] < a[0]:
        swap(a, 0, mid)
        count.extend([a[0],a[mid]])



    if a[n] < a[0]:
        swap(a, 0, n)
        if a[0]not in count:
            count.append(a[0])
        if a[n] not in count:
            count.append(a[n])




    if a[n] < a[mid]:
        swap(a, mid, n)

        if a[mid] not in count:  
            count.append(a[mid])
        if a[n] not in count:
            count.append(a[n])


    #result=[a[0],a[mid],a[n]]
    count.sort()
    return count

def main():

    try:
        ch=int(input("enter your set size:"))
        arr=[]

        for _ in range(ch):
            arr.append(int(input("enter your element: ")))
        print(sort_three(arr))

    except ValueError:
        print(sort_three())
    except UnboundLocalError:
        print(sort_three())

if __name__=="__main__":
    main()