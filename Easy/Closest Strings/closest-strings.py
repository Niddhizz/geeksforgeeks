#User function Template for python3

class Solution:
	def shortestDistance(self, s, word1, word2):
		# code here
		pos1=None
		pos2=None
		mn=float('inf')
        for i in range(len(s)):
            if s[i]==word1:
                pos1=i
            if s[i]==word2:
                pos2=i
            if pos1!=None and pos2!=None:
                mn=min(abs(pos1-pos2),mn)
        return mn    
                
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		s = list(map(str,input().split()))
		word1 = input()
		word2 = input()
		ob = Solution()
		ans = ob.shortestDistance(s, word1, word2)
		print(ans)

# } Driver Code Ends