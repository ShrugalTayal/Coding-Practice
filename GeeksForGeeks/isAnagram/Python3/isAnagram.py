#User function Template for python3
class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        """
        d = {}
        for i in set(b):
            d[i] = b.count(i)
        
        count = 0
    
        for i in a:
            try:
                if a.count(i) == d[i]:
                    count = count + 1
            except:
                pass
            
        if count == len(a) and len(a) == len(b):
            return True
        else:
            return False
        """
        la = list(a)
        la.sort()
        
        lb = list(b)
        lb.sort()
        
        if la == lb:
            return True
        else:
            return False
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends
