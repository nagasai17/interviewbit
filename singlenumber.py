class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        return 2*sum(set(A))-sum(A)
