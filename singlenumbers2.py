class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        from collections import Counter
        array=Counter(A)
        for i,j in array.items():
            if j==1:
                return i
