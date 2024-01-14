#User function Template for python3

class Solution:
    def ReFormatString(self,S, K):
        #code here
        res=''
        j=0
        for i in range(len(S)-1,-1,-1):
            if S[i]!='-':
                if j==k:
                    res+='-'
                    j=0
                if ord(S[i])>=97 and ord(S[i])<=122:
                    res+=chr(ord(S[i])-32)
                else:
                    res+=S[i]
                j+=1
        res=res[::-1]
        return res

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
        k=int(input())
        obj = Solution()
        print(obj.ReFormatString(s, k))
# } Driver Code Ends