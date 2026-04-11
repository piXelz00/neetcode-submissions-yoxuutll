class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        multiple = []
        for i in range(0,len(nums)):
            mul = 1 
            for j  in range(0,len(nums)):
                if j!=i:
                    mul*=nums[j]        
            multiple.append(mul)
        return multiple
        