class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums is []:
            return 0

        nums =  set(nums)
        max_len = 0
        for num in nums: 
            if num-1 not in nums:
                count_length = 1
                while num+count_length in nums:
                    count_length +=1 
                max_len = max(max_len,count_length)

        return max_len        








                





        

        