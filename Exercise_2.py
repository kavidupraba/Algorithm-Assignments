import random

def sort_three(a,low,high):
    mid=(low+high)//2
    '''Ma=max(a[low],a[mid],a[high])
    Mi=min(a[low],a[mid],a[high])
    a[mid]=a[low]+a[mid]+a[high]-Ma-Mi
    a[low]=Mi
    a[high]=Ma'''
    while not(a[low]<a[mid]<a[high]):
        if a[low] > a[mid]:
            a[low], a[mid] = a[mid], a[low]

        if a[low] > a[high]:
            a[low], a[high] = a[high], a[low]

        if a[mid] > a[high]:
            a[mid], a[high] = a[high], a[mid]
    '''arr=[]
    arr.extend([a[low],a[mid],a[high]])
    for ar in arr:
        if a[high]<=ar:
            a[high]=ar
        if a[low]>=ar:
            a[low]=ar
    total=a[high]+a[low]+a[mid]
    a[mid]=total-a[low]-a[high]'''









def main():
    test_case = list(range(1000))
    i = random.randrange(0, 500) #this will going to give a random Integer number between 0,500(500) so the array not be too short
    j = random.randrange(i + 1, 1000)#this will going to give a random integer number larger than i because
                                     # end (high/j) should always should higher than the i (l0w).randrange(3,9)give random number between 3-9

    random.shuffle(test_case)
    sort_three(test_case, i, j)
    m=(i+j)//2
    if test_case[i] < test_case[m] and test_case[m] < test_case[j]:
        print(test_case[i],test_case[m],test_case[j])

if __name__=="__main__":
    main()
