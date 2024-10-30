#student name: Peter Kim
#student number: 18693002

import threading

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

    mid_point = len(testcase) // 2

    # Determine the half to sort and store it in temp
    temp = testcase[:mid_point] if firstHalf else testcase[mid_point:]

    # Implement bubble sort algorithm
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
    global SortedFullList
    temp: list = []
    i, j = 0, 0

    # Merge the two sorted halves
    while i < len(sortedFirstHalf) and j < len(sortedSecondHalf):
        if sortedFirstHalf[i] <= sortedSecondHalf[j]: # Compare the current elements of both sorted lists
            temp.append(sortedFirstHalf[i])
            i += 1
        else:
            temp.append(sortedSecondHalf[j])
            j += 1

    # Append any remaining elements. The order here dosen't matter as at this point, one of the lists is already empty, and the remaining values
    # are larger than thoes appended.
    temp.extend(sortedFirstHalf[i:]) 
    temp.extend(sortedSecondHalf[j:]) 

    SortedFullList = temp  # Update the global variable

if __name__ == "__main__":
    # Shared variables
    testcase = [1,78,2,-2,-3,45959,5,1,2,3,4,1,3,-12312,123,-32323,2,1,1,1,3,2,22,1,2,23,1]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []

    # Implement multithreading
    thread1 = threading.Thread(target=sortingWorker, args=(True,))
    thread2 = threading.Thread(target=sortingWorker, args=(False,))

    # Start sorting threads
    thread1.start()
    thread2.start()

    # Wait for sorting threads to finish
    thread1.join()
    thread2.join()

    # Now start the merging thread
    thread3 = threading.Thread(target=mergingWorker)
    thread3.start()
    thread3.join()

    # As a simple test, print the final sorted list
    print("The final sorted list is ", SortedFullList)