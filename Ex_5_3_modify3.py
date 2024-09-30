import random as rd
import time as tm
import matplotlib.pyplot as plt


def check(x, y, gap_panelty=1, mismatch_panelty=2, matching_reward=0):
    if len(x) == 0:
        return len(x) * gap_panelty
    if len(y) == 0:
        return len(y) * gap_panelty

    i = len(x)
    j = len(y)

    match_or_unmatch = check(x[:-1], y[:-1]) + (matching_reward if x[i - 1] == y[j - 1] else mismatch_panelty)
    gap_from_y_side = check(x[:-1], y) + gap_panelty
    gap_from_x_side = check(x, y[:-1]) + gap_panelty

    return min(match_or_unmatch, gap_from_y_side, gap_from_x_side)

def check2(x,y,gapp,mmp):
    m=len(x)
    n=len(y)
    A=[[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        A[i][0]=i*gapp
    for j in range(n+1):
        A[0][j]=j*gapp

    for i in range(1,m+1):
        for j in range(1,n+1):
            maching=A[i-1][j-1]+(0 if x[i-1]==y[j-1] else mmp)
            gap_for_x=A[i][j-1]+gapp
            gap_for_y=A[i-1][j]+gapp
            A[i][j]=min(maching,gap_for_x,gap_for_y)

    return A[m][n]


def main():

    execution_time={"size":[],"recursion_function_time":[],"metrics_function_time":[]}
    size_list=[1000, 2000, 4000, 8000, 16000]
    for size in size_list:
        GP = 1
        MMP= 2
        #skipper=0
        xl=rd.choices('ACGT',k=size)
        yl=rd.choices('ACGT',k=size)
        x=''.join(xl)
        y=''.join(yl)

        list_start=tm.perf_counter() #process_time() or time() is not give us time difference
                                     # so we use perf_counter() it's better for calculating short time durations
        result1=check2(x,y,GP,MMP)
        list_end=tm.perf_counter()
        list_function_executiontime=list_end-list_start
        try:
            rcursive_start=tm.perf_counter()
            result2=check(x,y)
            recursive_end=tm.perf_counter()
            recursive_function_executiontime = recursive_end - rcursive_start
            execution_time["recursion_function_time"].append(recursive_function_executiontime)
        except RecursionError:
            calculated_time = 3 ** (size ** 2)
            #execution_time["recursion_function_time"].append("NA")
            #execution_time["recursion_function_time"].append(float('inf'))
            execution_time["recursion_function_time"].append(calculated_time)
        finally:
            execution_time["size"].append(size)
            execution_time["metrics_function_time"].append(list_function_executiontime)




    #for i in range(len(execution_time["recursion_function_time"])):
        #if execution_time["recursion_function_time"][i] == "NA":
            #execution_time["recursion_function_time"][i]=calculated_time

    #integer values are too large or time values have too many floating points Overfloaw error normalising key's related to time
    #execution_time["size"]=[val/1000 for val in execution_time["size"]]
    maximumr=max(execution_time["recursion_function_time"])
    execution_time["recursion_function_time"]=[val/maximumr for val in execution_time["recursion_function_time"]]
    maximumrm=max(execution_time["metrics_function_time"])
    execution_time["metrics_function_time"]=[val/maximumrm for val in execution_time["metrics_function_time"]]

    #print(execution_time)
    plt.plot(execution_time["size"],execution_time["recursion_function_time"],color="blue",label="recursive")
    plt.legend()
    plt.plot(execution_time["size"],execution_time["metrics_function_time"], color="red",label="metrics")
    plt.legend()
    plt.xlabel("size")
    plt.ylabel("computation_time")
    plt.show()







if __name__=='__main__':
    main()


