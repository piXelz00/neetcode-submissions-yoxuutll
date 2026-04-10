class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = [] # This is our "guest list"
        
        for n in nums:
            if n in seen:
                return True
            seen.append(n)
            
        return False 
