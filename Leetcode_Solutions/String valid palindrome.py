'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
 it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            while i<j and not s[i].isalnum(): i+=1
            while i<j and not s[j].isalnum(): j-=1

            if s[i].lower()!=s[j].lower(): return False
            i+=1
            j-=1
        return True
    
#----------------------------------------------#

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[i for i in s.lower() if i.isalnum()]
        return s==s[::-1]
    
#--------------------------------------------------#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(i for i in s if i.isalnum())
        s=s.lower()
        if s==s[::-1]: return True