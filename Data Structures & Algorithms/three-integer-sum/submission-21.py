class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ns = sorted(nums)
        three_sum = []



        for i in  range(0,len(ns)-2):


            if ns[i]>0:
                    break 

            if i>0 and  ns[i] == ns[i-1]:
                continue
   

            left,right = i+1,len(ns)-1
            two_sum = -ns[i]
            
            while left<right:
                if ns[left]+ns[right] == two_sum:
                        three_sum.append([ns[left],ns[right],ns[i]])
                        while left<right and ns[left]==ns[left+1]:
                            left+=1
                        while left<right and ns[right]==ns[right-1]:
                            right-=1

                        left+=1
                        right-=1

                elif two_sum < ns[left]+ns[right]:
                    right-=1
                else:
                    left+=1
            
        return three_sum


        


        