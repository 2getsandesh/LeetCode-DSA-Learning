'''Given an integer n, return an array ans 
of length n + 1 such that for each i (0 <= i <= n),
 ans[i] is the number of 1's in the binary representation of i.'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        
        for i in range(0,n+1):
            c = bin(i).count("1")
            ans.append(c)
            
        return ans
    
#====================================================#
    
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)

        for i in range(1,n+1):
            if i%2==0:
                ans[i] = ans[i>>1]
            else:
                ans[i] = ans[i>>1]+1
        return ans