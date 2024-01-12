#User function Template for python3

class Solution:
    def findIndex(self,str):
        # Your code goes here 
        stack=[]
        d={'(':')'}
        c=0
        for i in str:
            if i in d:
                stack.append(i)
            else:
                if len(stack)!=0:
                    c=c+1
                    stack.pop()
                else:
                    c=c+1
        return c         


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        str = input()
        ob=Solution()
        print(ob.findIndex(str))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends