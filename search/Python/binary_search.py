# Binary Search

from time import time


def contains(collection, target):
    """Determine whether collecitons contains target """
    return target in collection

def binary_search_contains(ordered, target):
    """Use binary array search to determine if target is in collection """

    low  = 0
    high = len(ordered) - 1
    while low <= high:
        mid = (low + high) / 2
        if target == ordered[mid]:
            return True # found it!
        elif target < ordered[mid]:
            high = mid - 1
        else:
            low = mid + 1
    # not found
    return False

def performance():
    """Determine execution performance of contains """
    n = 1024
    while n < 50000000:
        sorted = range(n)
        now = time()

        # by using -1 the worst case scenario is evaluated
        #contains(sorted, -1)
        binary_search_contains(sorted, -1)


        done = time()

        print n, (done-now)*1000
        n *= 2


if __name__ == "__main__":
    performance()
