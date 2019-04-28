# This program is about Shell Sort
# Time complexity is O(n^(3/2))

# It is an advanced version of Straight Insertion Sort
# The idea is dividing a list into sublists and we do Straight Insertion Sort on
# each sublist.
# Finally, do Straight Insertion Sort to the original list.

class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def shell_sort(self):
        # Shell Sort
        lis = self.r
        length = len(lis)
        increment = len(lis)
        
        while increment > 1:
            increment = int(increment/3)+1
            for i in range(increment+1, length):
                if lis[i] < lis[i - increment]:
                    temp = lis[i]
                    j = i - increment
                    while j >= 0 and temp < lis[j]:
                        lis[j+increment] = lis[j]
                        j -= increment
                    lis[j+increment] = temp

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0,123,22])
    sqlist.shell_sort()
    print(sqlist)
    
"""
 0 1 2 3 4 5 6 7 8 9 22 123
"""
