# This program is about Heap Sort
# Time complexity is O(n log(n))

class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def swap(self, i, j):
        # define a method to exchange elements in order to easily use later on        
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def heap_sort(self):
        length = len(self.r)
        i = int(length/2)
        # iteration start at the middle and end at 0
        while i >= 0:
            self.heap_adjust(i, length-1)
            i -= 1
        # reversely iterate the whole list
        j = length-1
        while j > 0:
            # exchange current node (start of list) which has index 0 to
            # index j
            self.swap(0, j)
            # rebuild
            self.heap_adjust(0, j-1)
            j -= 1

    def heap_adjust(self, s, m):
        lis = self.r
        temp = lis[s]
        i = 2*s
        while i <= m:
            if i < m and lis[i] < lis[i+1]:
                i += 1
            if temp >= lis[i]:
                break
            lis[s] = lis[i]
            s = i
            i *= 2
        lis[s] = temp

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    sqlist.heap_sort()
    print(sqlist)
    
"""
 0 1 2 3 4 5 6 7 8 9 22 123
"""
