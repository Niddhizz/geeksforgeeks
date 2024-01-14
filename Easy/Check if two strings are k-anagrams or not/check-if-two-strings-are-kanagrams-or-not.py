#User function template for Python 3
from collections import Counter
class Solution:
    def areKAnagrams(self, s1, s2, k):
        # code here
        n1=len(s1)
        n2=len(s2)
        if n1!=n2:
            return 0
            
        c1,c2=Counter(s1),Counter(s2)
        for i in range(len(s1)):
            if c2[s1[i]]<=0:
                k-=1
            elif c2[s1[i]]>0:
                c2[s1[i]]-=1
        return k>=0        

#{ 
 # Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        k = int(input())
        ob = Solution()
        if ob.areKAnagrams(arr[0], arr[1], k):
            print(1)
        else:
            print(0)
# } Driver Code Ends