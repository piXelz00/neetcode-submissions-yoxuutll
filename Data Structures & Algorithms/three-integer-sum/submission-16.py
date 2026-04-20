class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ns = sorted(nums)
        print(ns)
        three_sum = []
        

        for i in  range(0,len(ns)-2):
            
            left,right = i+1,len(ns)-1
            two_sum = -ns[i]
            while left<right:
                if ns[left]+ns[right] == two_sum:
                    
                    if [ns[left],ns[right],ns[i]] not in three_sum:
                        three_sum.append([ns[left],ns[right],ns[i]])
                    left+=1
                    right-=1
                elif two_sum < ns[left]+ns[right]:
                    right-=1
                else:
                    left+=1
            
        return three_sum


        


        