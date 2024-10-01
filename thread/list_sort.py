#student name: Peter Kim
#student number: 18693002

import threading as th

def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    global testcase, sortedFirstHalf, sortedSecondHalf

    length = len(testcase)
    mid_point = length // 2

    # Determine the half to sort and store it in temp
    temp = testcase[:mid_point] if firstHalf else testcase[mid_point:]

    # Implement a simple bubble sort algorithm
    for i in range(len(temp)):
        for j in range(0, len(temp) - i - 1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]

    # Store the sorted half in the appropriate variable
    if firstHalf:
        sortedFirstHalf = temp
    else:
        sortedSecondHalf = temp

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges/sorts
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    global testcase, sortedFirstHalf, sortedSecondHalf, SortedFullList
    length1 = len(sortedFirstHalf)
    length2 = len(sortedSecondHalf)
    temp: list = []
    i, j = 0, 0

    # Merge the two sorted halves
    while i < length1 and j < length2:
        if sortedFirstHalf[i] <= sortedSecondHalf[j]:
            temp.append(sortedFirstHalf[i])
            i += 1
        else:
            temp.append(sortedSecondHalf[j])
            j += 1

    # If there are remaining elements in sortedFirstHalf
    while i < length1:
        temp.append(sortedFirstHalf[i])
        i += 1

    # If there are remaining elements in sortedSecondHalf
    while j < length2:
        temp.append(sortedSecondHalf[j])
        j += 1

    # Assign the merged list to sortedFullList
    sortedFullList = temp

    # Print the sorted lists for debugging purposes
    print("Sorted First Half:", sortedFirstHalf)
    print("Sorted Second Half:", sortedSecondHalf)
    print("Merged List:", sortedFullList)


if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2,9,11,3,4,6,5,2,1,3,4,5,76,8,4]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified 
    thread1 = th.Thread(target = sortingWorker, args = (True,)) # The first arugment has to be callable - like function. 
    thread2 = th.Thread(target = sortingWorker, args = (False,)) # The first arugment has to be callable - like function. 
    thread3 = th.Thread(target = mergingWorker)
    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)