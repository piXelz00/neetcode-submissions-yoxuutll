class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sorted=sorted(nums)
        for i in range(0,len(nums_sorted)-1):
            if nums_sorted[i] ==  nums_sorted[i+1]:
                return True
        return False        
