#User function Template for python3

class Solution:

    def getSubstringWithEqual012(self, Str):
        # code here
        dic={}
        dic[(0,0)]=1
        res=0
        count0=0
        count1=0
        count2=0
        for i in range(len(Str)):
            if Str[i]=='0':
                count0+=1
            elif Str[i]=='1':
                count1+=1
            elif Str[i]=='2':
                count2+=1
            
            if (count1-count0,count2-count1) in dic:
                res+=dic[(count1-count0,count2-count1)]
                dic[(count1-count0,count2-count1)]+=1
            else:
                dic[(count1-count0,count2-count1)]=1
        return res        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.getSubstringWithEqual012(Str))

# } Driver Code Ends