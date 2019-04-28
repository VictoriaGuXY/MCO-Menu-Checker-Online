# This program is about Quick Sort
# an advanced version of Bubble Sort
# Time complexity is O(nlog(n))

# Version 2

def quick_sort(nums):
    # wrapping for user to use easily
    def qsort(lst, begin, end):
        if begin >= end:
            return
        i = begin
        key = lst[begin]
        for j in range(begin+1, end+1):
            if lst[j] < key:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[begin], lst[i] = lst[i], lst[begin]
        qsort(lst, begin, i-1)
        qsort(lst,i+1,end)
    qsort(nums, 0, len(nums)-1)
    