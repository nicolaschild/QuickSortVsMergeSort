import math
import random
import time as t
#PIP install matplotlib if necessary
import matplotlib.pyplot as plt
"""SORTING ALGORITHMS"""
counter = 0
def reset():
    global counter
    counter = 0
def basicOps():
    global counter
    return counter
def quickSort(listToSort, low, high):
    if low < high:
        pivotPoint = partition(listToSort, low, high)
        quickSort(listToSort, low, pivotPoint)
        quickSort(listToSort, pivotPoint+1, high)
def partition(arr, low, high):
    global counter
    pivot = arr[low]
    i = low + 1
    j = low + 1
    while i <= high:
        counter +=1
        if arr[i] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            j +=1
        i += 1
    #swap j-1 and pivot
    arr[j-1], arr[low] = arr[low], arr[j-1]
    return j-1
def bestBasicOps(n):
    k = math.log2(n)/math.log2(2)
    return (k * (2**k)) - ((2**k)-1)
def worstBasicOps(n):
    #We get the pattern 0, 1, 3, 6, 10, 15, 21
    #Which can be rewritten as a(n) = a(n-1) + n
    return (n) * ((n-1)/2)
def mergeSort(arr):
    n = len(arr) #Number of elements in array
    if n > 1:
        middle = n//2
        left = arr[:middle]
        right = arr[middle:]
        mergeSort(left)
        mergeSort(right)
        merge(arr, left, right)
def merge(arr, left, right):
    global counter
    n = len(arr)
    m = n//2
    i = 0 #a index(where to inset the next sorted item)
    j = 0 #Left index
    k = 0 #Right index
    while j < m and k < n - m:
        counter+=1
        if left[j] <= right[k]:
            arr[i] = left[j]
            j+=1
        else:
            arr[i] = right[k]
            k+=1
        i+=1
    while j < m:
        arr[i] = left[j]
        j+=1
        i+=1
    while k < (n-m):
        arr[i] = right[k]
        i+=1
        k+=1
def bestBasicOps(n):
    #Closed form solution is a(n) = k * 2^(k-1) where k is log2(n)/log2(2)
    k = math.log2(n)/math.log2(2)
    return k * (2**(k-1))
def worstBasicOps(n):
    #This one was tricky, we can separate the - 1 to get the new form w(n) = 2*w(n/2) + n, which holds
    #the relation of a(n) = n * 2^n, and the difference is another relation a(n) = 2^n - 1
    #by combining the two we can get the form a(k) = (k * 2^k) - (2^k - 1), where k is
    #the log base 2 of n
    k = math.log2(n)/math.log2(2)
    return (k * (2**k)) - ((2**k)-1)

"""ANALYSIS ALGORITHMS"""
def runAlgorithms():
    # Run both algorithms using random data of various sizes of n = 2^k
    # k an integer greater than or equal to 10.  
    # I typically use something like set = { k0 = 10, k1 = 15, k2 = 20 }
    
    #We are going to run result of each k as it's own array like so
    """
        K=10 [[n (size of array), mergesortTime, basicOperations],
        --    [n (size of array), quicksortTime, basicOperations],
        k=15  [n (size of array), mergesortTime, basicOperations],
              [n (size of array), mergesortTime, basicOperations],
        k=20
         .
         .
         .                                                      ]
         odd numbered rows = quickSort stats
         even numbered rows = mergeSort stats
    """
    resultsArray = [] #Our 2-Dimmensional Array
    possibleKs = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    for k in possibleKs:
        n = 2**k
        # Now we create random data of size n
        sample = random.sample(range(0, n), n - 1)
        sample2 = sample
        #Now we will time and run both algorithms
        t1 = t.time()
        quickSort(sample, 0, len(sample) - 1)
        t2= t.time()
        quickSortTime = t2 - t1
        resultsArray.append([n, quickSortTime, basicOps()])
        #Reset counter
        reset()
        t1 = t.time()
        mergeSort(sample2)
        t2 = t.time()
        mergeSortTime = t2 - t1
        resultsArray.append([n, mergeSortTime, basicOps()])
    return resultsArray
def explainData(resultsArray):
    print(resultsArray)
    i = 0
    while i < len(resultsArray) - 1: #EVEN (MERGE SORT ROW)
        n = resultsArray[i][0]
        print(f"----FOR AN ARRAY OF SIZE {n}----".center(90))
        mergeSize = n
        mergeTime = resultsArray[i][1]
        mergeCalculations = resultsArray[i][2]
        print(f'Merge Sort of Size: {mergeSize} elements had {mergeCalculations} calculations in {mergeTime} seconds.')
        i += 1
        quickSize = n
        quickTime = resultsArray[i][1]
        quickCalculations = resultsArray[i][2]
        print(f'Quick Sort of Size: {quickSize} elements had {quickCalculations} calculations in {quickTime} seconds.')
        i += 1
        if mergeCalculations > quickCalculations:
            print(f"Quick Sort had {mergeCalculations - quickCalculations} less calculations!")
        else:
            print(f"Merge Sort had {quickCalculations - mergeCalculations} more calculations!")
        if mergeTime > quickTime:
            print(f"Quick Sort was {mergeTime - quickTime} seconds faster than Merge Sort")
        else:
            print(f"Merge Sort was {quickTime - mergeTime} seconds faster than Quick Sort")
        print('\n')
def graphDataMatplotLib(resultsArray):
    #Time will be our x-axis and calculations will be our y-axis
    mergeResults = [resultsArray[x] for x in range(len(resultsArray)) if x % 2 == 0]
    quickResults = [resultsArray[x] for x in range(len(resultsArray)) if x % 2 == 1]
    #X-AXIS' FOR GRAPHS
    mergeTimes = [mergeResults[x][1] for x in range(len(mergeResults))]
    quickTimes = [quickResults[x][1] for x in range(len(quickResults))]
    #Y-AXIS' FOR GRAPHS
    mergeCalculations = [mergeResults[x][2] for x in range(len(mergeResults))]
    quickCalculations = [quickResults[x][2] for x in range(len(mergeResults))]
    
    #plot both
    plt.plot(mergeTimes, mergeCalculations, label = "MERGE SORT")
    plt.plot(quickTimes, quickCalculations, label = "QUICK SORT")

    #Naming our X and Y axis'
    plt.xlabel("Time in Seconds")
    plt.ylabel("Calculations")
    plt.title("Merge Sort vs. Quick Sort")
    
    #Show the legend on the plot
    plt.legend()

    #Show the plot
    plt.show()
    
def pushToExcel(resultsArray):
    #Time will be our x-axis and calculations will be our y-axis
    mergeResults = [resultsArray[x] for x in range(len(resultsArray)) if x % 2 == 0]
    quickResults = [resultsArray[x] for x in range(len(resultsArray)) if x % 2 == 1]
    #MERGE AND QUICK SIZES - Since they're the same we can just keep one
    mergeSize = [mergeResults[x][0] for x in range(len(mergeResults))]
    #X-AXIS' FOR GRAPHS
    mergeTimes = [mergeResults[x][1] for x in range(len(mergeResults))]
    quickTimes = [quickResults[x][1] for x in range(len(quickResults))]
    #Y-AXIS' FOR GRAPHS
    mergeCalculations = [mergeResults[x][2] for x in range(len(mergeResults))]
    quickCalculations = [quickResults[x][2] for x in range(len(mergeResults))]

    """Going to organize our table like so:
    n (size of list), time for quick sort, calculations for quick sort, quick change in time from last run (delta T), time for merge sort, calculations for merge sort, merge change in time from last run (delta T)
    """
    with open('MergeVsQuick.csv', 'w') as file:
        file.write("n,Quick Time,Quick Calculations,Quick Delta T,,Merge Time,Merge Calculations,Merge Delta T\n")
        previousQuickTime = 0
        previousMergeTime = 0
        for i in range(len(mergeResults)):
            file.write(f"{mergeSize[i]},{quickTimes[i]},{quickCalculations[i]},{quickTimes[i]-previousQuickTime},,{mergeTimes[i]},{mergeCalculations[i]},{mergeTimes[i]-previousMergeTime}\n")
            #Update old times for delta time
            previousQuickTime = quickTimes[i]
            previousMergeTime = mergeTimes[i]


def main():
    results = runAlgorithms()
    # explainData(results)
    graphDataMatplotLib(results)
    # pushToExcel(results)


if __name__ == "__main__":
    main()
