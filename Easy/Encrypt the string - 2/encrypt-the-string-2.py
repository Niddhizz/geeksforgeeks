#User function Template for python3

class Solution:
    def encryptString(self, S):
        # code here
        c=0
        temp=[]
        result=''
        for i in range(len(S)):
            if i<len(S)-1 and S[i]==S[i+1]:
                c+=1
            else:
                temp.append(str(hex(c+1))[2:]+S[i])
                c=0
        for j in range(len(temp)-1,-1,-1):
            result+=temp[j]
        return result    

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.encryptString(S))
# } Driver Code Ends