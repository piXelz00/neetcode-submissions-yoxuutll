class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_arr = []
        for n in nums:
            if n not in  temp_arr:
                temp_arr.append(n)
            else:
                return True
        return False        
