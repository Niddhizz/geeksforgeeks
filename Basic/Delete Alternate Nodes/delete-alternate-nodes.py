#User function Template for python3

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None'''

class Solution: 
    
    
    def deleteAlt(self, head):
        
        #add code here
        if head.next==None:
            return head
        elif head.next.next==None:
            return head
        else:
            curr=head
            while curr!=None and curr.next!=None:
                nextnode=curr.next
                curr.next=curr.next.next
                nextnode=None
                curr=curr.next
            return head    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        
        n = int(input())
        arr = list(map(int, input().strip().split()))
        #head = createList(arr, n)
        head = Node(arr[0])
        temp = head
        for i in range(1,len(arr)):
            temp.next = Node(arr[i])
            temp = temp.next

        
        ob = Solution()
        ob.deleteAlt(head)
        
        while head is not None:
            print(head.data,end = " ")
            head = head.next
        print()   
        
# } Driver Code Ends