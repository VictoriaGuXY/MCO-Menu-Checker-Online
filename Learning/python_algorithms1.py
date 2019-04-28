# This program is about Bubble Sort
# Time complexity is O(n^2)

# simplest: bubble_sort_simple
# Bubble Sort: bubble_sort
# Advanced version: bubble_sort_advance

class SQList:
    def __init__(self, lis=None):
        self.r = lis
        
    # define a method to exchange elements in order to easily use later on
    def swap(self, i, j):
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp
        
    # define an easy exchange order
    # time complexity = O(n^2)
    def bubble_sort_simple(self):
        lis = self.r
        length = len(self.r)
        for i in range(length):
            for j in range(i+1, length):
                if lis[i] > lis[j]:
                    self.swap(i, j)
                    
    # time complexity = O(n^2)
    def bubble_sort(self):
        lis = self.r
        length = len(self.r)
        for i in range(length):
            j = length-2
            while j >= i:
                if lis[j] > lis[j+1]:
                    self.swap(j, j+1)
                j -= 1
    
    # advanced bubble_sort
    # time complexity = O(n^2)
    # set a flag, when nothing happens during an iteration, it indicates that 
    # elements after that have been sorted already.
    def bubble_sort_advance(self):
        lis = self.r
        length = len(self.r)
        flag = True
        i = 0
        while i < length and flag:
            flag = False
            j = length - 2
            while j >= i:
                if lis[j] > lis[j + 1]:
                    self.swap(j, j + 1)
                    flag = True
                j -= 1
            i += 1

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([4,1,7,3,8,5,9,2,6])
    # sqlist.bubble_sort_simple()
    # sqlist.bubble_sort()
    sqlist.bubble_sort_advance()
    print(sqlist)
    