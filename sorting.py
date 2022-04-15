

def bubble(array): 
    i = 0 
    j = 0
    n = len(array)
    while i < n - 1: 
        while j < n - i - 1: 
            if array[j] > array[j+1]: 
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            j += 1
        j = 0
        i += 1
    print(array)



# recursive
def mergeSort(array, left, right):  
    if (left < right): 
        middle = (left + right)//2
        mergeSort(array, left, middle)
        mergeSort(array, middle+1, right)
        merge(array, left, middle, right)

# helper
def merge(array, left, middle, right): 
    nr = right - middle
    nl = middle - left + 1
    i = 0 
    j = 0
    leftarray = [] 
    rightarray = [] 
    while i < nl: 
        leftarray.append(array[left+i])
        i += 1 
    i = 0 
    while j < nr: 
        rightarray.append(array[middle + 1 + j])
        j += 1
    j = 0
    print("Left Array", leftarray)
    print("Right Array", rightarray)


    k = left # index of array replacement
    while(i < nl and j < nr): #while both haven't exceeded their bounds  
        if leftarray[i] < rightarray[j]: 
            array[k] = leftarray[i]
            i += 1
        else: 
            array[k] = rightarray[j]
            j += 1
        k += 1

    while i < nl: 
        array[k] = leftarray[i]
        i += 1
        k += 1
    while j < nr: 
        array[k] = rightarray[j]
        j += 1
        k += 1
    print(array)




def quickSort(array, left, right):
    if left < right: 
        p = partition(array, left, right)
        quickSort(array, left, p-1) # quicksort on low
        quickSort(array, p + 1, right) # quicksort on high
    print(array)

def partition(array,left, right):  
    p = array[right] # pick a random value to pivot on. It is best to try and find the median value
    i = left-1 # keeps track of the smallest element in the list
    j = left
    while j < right: 
        if array[j] < p:
            i += 1
            temp = array[j]
            array[i] = array[j]
            array[j] = array[i]
        print(array)
        j += 1

    temp = array[j]
    array[i+1] = array[j]
    array[j] = array[i+1]
    #print("Partition", array)
    return i + 1

    




def negloop(): 
    for i in range(1, 10+1):
        print(i)







if __name__ == "__main__": 
    negloop()
    testarray = [1,2,8,3,6,7,4,2,1,3,5,5,4]
    bubble(testarray)
    mergeSort(testarray, 0, len(testarray)-1)
    quickSort(testarray, 0, len(testarray)-1)