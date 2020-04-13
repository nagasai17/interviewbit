class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):
	    
	    head = A.next if A and A.next else A
	    
	    while A and A.next:
	        C = A.next.next                    # 3rd Node
	        D = C.next if C and C.next else C  # 4th Node if existing
	        A.next.next, A.next, A = A, D, C
	        
	    return head
