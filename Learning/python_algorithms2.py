# This program is about simple selection sort
# Time complexity is O(n^2)

# For all unsorted elements, we compare them from the very beginning to the end.
# Remember the index of smallest element and exchange this element to the first
# in iteration.

class SQList:
    def __init__(self, lis=None):
        self.r = lis
    
    # define a method to exchange elements in order to easily use later on
    def swap(self, i, j):
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp
        
    # simple selection sort
    # Time complexity is O(n^2)
    def select_sort(self):
        lis = self.r
        length = len(self.r)
        for i in range(length):
            minimum = i
            for j in range(i+1, length):
                if lis[minimum] > lis[j]:
                    minimum = j
            if i != minimum:
                self.swap(i, minimum)

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0])
    sqlist.select_sort()
    print(sqlist)
    
"""
 0 1 2 3 4 5 6 7 8 9
"""    
      