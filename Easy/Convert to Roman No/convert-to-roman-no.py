#User function template for Python 3

class Solution:
    def convertRoman(self, n):
        #Code here
        s=''
        l=[[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']]
        while n>0:
            for i in l:
                if (n>=i[0]):
                    n=n-i[0]
                    s=s+i[1]
                    break
        return s        
                

#{ 
 # Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ob = Solution()
        print(ob.convertRoman(n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends