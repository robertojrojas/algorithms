# Insert Using Binary Search

from time import time


def binary_search_contains(ordered, target):
    """Use binary array search to return index position of target is in collection """

    low  = 0
    high = len(ordered) - 1
    while low <= high:
        mid = (low + high) / 2
        if target == ordered[mid]:
            return mid # found it!
        elif target < ordered[mid]:
            high = mid - 1
        else:
            low = mid + 1
    # not found
    return -(low + 1)

def insertInPlaceBruteForce(ordered, target):
    """Inserts target in the proper location - Brute force """
    for i in range(len(ordered)):
        if target < ordered[i]:
            ordered.insert(i, target)

    ordered.append(target)


def insertInPlace(ordered, target):
    """Inserts target in the proper location - Using Binary search """
    location = binary_search_contains(ordered, target)
    if location < 0:
        ordered.insert(-(location + 1), target)
        return

    ordered.append(target)


def performance():
    """Determine execution performance of contains """
    n = 1024
    while n < 50000000:
        sorted = range(n)
        now = time()

        # by using n+1 the worst case scenario is evaluated
        #insertInPlaceBruteForce(sorted, n+1)
        insertInPlace(sorted, n+1)


        done = time()

        print n, (done-now)*1000
        n *= 2


if __name__ == "__main__":
    performance()
