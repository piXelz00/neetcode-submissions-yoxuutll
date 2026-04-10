class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        for i , num in enumerate(nums):
            num2 = target - num
            if num2 in hash_map:
                return [hash_map[num2],i]
            hash_map[num] = i


                







        


                



                
                
        

                



             
        
            
            

