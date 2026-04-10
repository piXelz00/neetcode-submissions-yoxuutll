class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        set_nums = set(nums)
        tw_sum = []
        second = None
        for i in range(0,len(nums)):
            counter = 0
            element = target - nums[i]

            if element == nums[i]:
                
                counter = self.counter(0,i,nums)
                print(i)
                print(counter)
                
                

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






        


                



                
                
        

                



             
        
            
            

