# 27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k
    
# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[k-1]:
                nums[k] = nums[i]
                k+=1
        return k
    
# 80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=2
        
        for i in range(2,len(nums)):
            if nums[i]!=nums[k-2]:
                nums[k] = nums[i]
                k+=1
        return k
    
# 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k] = nums[i]
                k+=1
        for i in range(k,len(nums)):
            nums[i] = 0
