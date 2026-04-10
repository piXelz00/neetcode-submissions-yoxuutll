class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        for i , num in enumerate(nums):
            num2 = target - num
            if num2 in hash_map:
                return [hash_map[num2],i]
            hash_map[num] = i


                

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        set_nums = set(nums)
        tw_sum = []
        second = None
        for i in range(0,len(nums)):
            counter = 0
            element = target - nums[i]
            if element == nums[i]:                
                counter = self.counter(0,i,nums)
                
            if second is None:
                    if element in set_nums :
                            if counter != 1:
                                second = element 
                                tw_sum.append(i)        
            else:
                        if  second == nums[i]:
                            tw_sum.append(i)
        return tw_sum


    def counter(self,counter,n,nums):
        counter = 0
        for i in nums:
            if i == nums[n]:
                counter+=1
        return counter  






        


                



                
                
        

                



             
        
            
            

