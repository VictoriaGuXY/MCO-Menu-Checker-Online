# This program is about Straight Insertion Sort
# Time complexity is O(n^2)
# Best situation is O(n)

# straightly insert into a sorted list
# then we will get a new list with length + 1

class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def insert_sort(self):
        lis = self.r
        length = len(self.r)
        
        # start from index 1
        for i in range(1, length):
            if lis[i] < lis[i-1]:
                temp = lis[i]
                j = i-1
                while lis[j] > temp and j >= 0:
                    lis[j+1] = lis[j]
                    j -= 1
                lis[j+1] = temp

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0])
    sqlist.insert_sort()
    print(sqlist)
    
"""
 0 1 2 3 4 5 6 7 8 9
"""
