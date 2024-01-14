#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,s1,s2):
         n=len(s1)
         m=len(s2)
         d={}
         
         if n!=m:
             return False
         if n==1:
             return True
         for i in range(n):
             if s1[i] not in d:
                 if s2[i] in d.values():
                     return False
                 d[s1[i]]=s2[i]
             elif d[s1[i]]!=s2[i]:
                 return False
         return True         

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends