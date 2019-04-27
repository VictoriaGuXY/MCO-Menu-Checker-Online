from collections import Counter

# If we want to count number of a specific element appears in a string, list or 
# tuple, use collections.Counter.

# most_common method from collections.Counter can be used to do this.

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)

# find three words that appear the most frequently
top_three = word_counts.most_common(3)

print(top_three)

"""
[('eyes', 8), ('the', 5), ('look', 4)]
"""
