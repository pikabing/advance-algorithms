import random
import math
import time


def findMedianOfElements(lst):
    # print(lst)
    n = len(lst)
    s_lst = sorted(lst)
    position = math.floor((n+1)/2)
    return s_lst[position -1]

def findMedianOfMedians(arr):
    n = len(arr)
    listOfMedians = []
    i = 0
    while n > 5:
        med = findMedianOfElements(arr[i: i+5])
        # print(med)
        listOfMedians.append(med)
        i  = i + 5
        n -= 5
    if n != 0:
        med = findMedianOfElements(arr[i:])
        listOfMedians.append(med)

    # print(listOfMedians)
    return listOfMedians

def findMedianOfMediansDriver(arr):
    listMedians = findMedianOfMedians(arr)

    while(len(listMedians) != 1):
        listMedians = findMedianOfMedians(listMedians)

    return listMedians[0]

def deterinisticMedian(arr,arrN, k):
    med = findMedianOfMediansDriver(arrN)
    L = []
    R = []
    for element in arr:
        if element < med:
            L.append(element)
        else:
            R.append(element)

    p = sorted(arr).index(med) 

    if k == p:
        return arr[p]
    elif k < p:
        return deterinisticMedian(arr,L,k)
    else:
        return deterinisticMedian(arr,R,k-p)

def deterministicMedianDriver(arr):
    k = math.floor((len(arr)+1)/2)
    med = deterinisticMedian(arr,arr,k)
    print(med)


def findRank(arr, element):
    return sorted(arr).index(element) + 1

def checkMedianMonteCarlo(arr, delta):
    n = len(arr)
    position = random.randint(0, n-1)
    predictedElement = arr[position]
    # print(predictedElement)
    rank = findRank(arr, predictedElement)
    # print(rank)
    leftLimit = math.floor((1/2 - delta) * (n+1))
    rightLimit = math.ceil((1/2 + delta) * (n+1))

    if rank >= leftLimit and rank <= rightLimit:
        return predictedElement
    else:
        return False

def median_las_vegas(arr, delta):
    while(1):
        result = checkMedianMonteCarlo(arr, delta)
        if result != False:
            return result


def arrayGenerate():
    size = random.randint(3,10000)
    print("Size of array is: ", size)

    arr = []
    for i in range(0,size):
        x = random.randint(1,10000)
        arr.append(x)

    # print("Original Array: ", arr)
    return arr

def lasVegasDriver(arr):
    median = median_las_vegas(arr, 0.1)
    print(median)


arr = arrayGenerate()

startDA = time.time()
deterministicMedianDriver(arr)
print("Deterministic Method Ended in {} seconds.".format((time.time() - startDA)))

startLV = time.time()
lasVegasDriver(arr)
print("Las_Vegas Method Ended in {} seconds.".format((time.time() - startLV)))


