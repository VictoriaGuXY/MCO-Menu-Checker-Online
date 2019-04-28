# This program is about Merging Sort using Divide and Conquer algorithm.
# Combine small sorted lists to get a large sorted list.

# Version 1
class SQList:
    def __init__(self, lis=None):
        self.r = lis
    
    # define a method to exchange elements
    def swap(self, i, j):
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def merge_sort(self):
        self.msort(self.r, self.r, 0, len(self.r)-1)

    def msort(self, list_sr, list_tr, s, t):
        temp = [None for i in range(0, len(list_sr))]
        if s == t:
            list_tr[s] = list_sr[s]
        else:
            m = int((s+t)/2)
            self.msort(list_sr, temp, s,  m)
            self.msort(list_sr, temp, m+1, t)
            self.merge(temp, list_tr, s, m, t)

    def merge(self, list_sr, list_tr, i, m,  n):
        j = m+1
        k = i
        while i <= m and j <= n:
            if list_sr[i] < list_sr[j]:
                list_tr[k] = list_sr[i]
                i += 1
            else:
                list_tr[k] = list_sr[j]
                j += 1

            k += 1
        if i <= m:
            for l in range(0, m-i+1):
                list_tr[k+l] = list_sr[i+l]
        if j <= n:
            for l in range(0, n-j+1):
                list_tr[k+l] = list_sr[j+l]

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 12, 77, 34, 23])
    sqlist.merge_sort()
    print(sqlist)

"""
 0 1 2 3 4 5 6 7 8 9 12 23 34 77
"""
