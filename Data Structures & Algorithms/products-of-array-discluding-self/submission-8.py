class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        max_mul ,zro = self.max_(nums)
        mul_list = []

        if zro == 0:
            for i in range(0,len(nums)):
                if nums[i] != 0:
                    mul_num = max_mul//nums[i]
                    mul_list.append(mul_num)
            return mul_list    
        else:
            if zro > 1:
                print("got it")
                return  [0 for i in nums]
            elif zro ==1:
                zero_mul = []
                for i in range(0,len(nums)):
                    if nums[i]==0:
                        zero_mul.append(max_mul)
                    else:
                        zero_mul.append(0)
                return zero_mul


    def max_(self,nums:List[int]):
            mul=1
            zro_counter = 0
            for i in nums:
                if i !=0:
                    mul*=i 
                else:
                    zro_counter +=1
            return mul,zro_counter