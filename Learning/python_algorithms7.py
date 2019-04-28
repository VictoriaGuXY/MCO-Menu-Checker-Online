# This program is about Merging Sort using Divide and Conquer algorithm.
# Combine small sorted lists to get a large sorted list.

# Version 2
def merge(lfrom, lto, low, mid, high):
    # compare two lists which need to be combined
    # small in lto and lfrom index+1 
    # get new element and do comparison again
    # when finish comparison for lfrom, the elements in lfo are sorted
    i, j, k = low, mid, low
    while i < mid and j < high:
        if lfrom[i] <= lfrom[j]:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:
        lto[k] = lfrom[j]
        j += 1
        k += 1


def merge_pass(lfrom, lto, llen, slen):
    # deal with all lists need to be combined
    # we need length of each small list and total length of the large list
    i = 0
    while i+2*slen < llen:
        merge(lfrom, lto, i, i+slen, i+2*slen)
        i += 2*slen
    if i+slen < llen:
        merge(lfrom, lto, i, i+slen, llen)
    else:
        for j in range(i, llen):
            lto[j] = lfrom[j]

def merge_sort(lst):
    slen, llen = 1, len(lst)
    templist = [None]*llen
    while slen < llen:
        merge_pass(lst, templist, llen, slen)
        slen *= 2
        merge_pass(templist, lst, llen, slen)
        slen *= 2
        