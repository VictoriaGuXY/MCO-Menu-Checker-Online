# This program is about Quick Sort
# an advanced version of Bubble Sort
# Time complexity is O(nlog(n))

# Version 1
class SQList:
    def __init__(self, lis=None):
        self.r = lis
    
    # define a method to exchange elements
    def swap(self, i, j):
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def quick_sort(self):
        self.qsort(0, len(self.r)-1)

    def qsort(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            self.qsort(low, pivot-1)
            self.qsort(pivot+1, high)

    def partition(self, low, high):
        # param low: left index
        # param high: right index
        # return: index of pivot
        lis = self.r
        pivot_key = lis[low]
        while low < high:
            while low < high and lis[high] >= pivot_key:
                high -= 1
            self.swap(low, high)
            while low < high and lis[low] <= pivot_key:
                low += 1
            self.swap(low, high)
        return low

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    sqlist.quick_sort()
    print(sqlist)

"""
 0 1 2 3 4 5 6 7 8 9 22 123
"""
