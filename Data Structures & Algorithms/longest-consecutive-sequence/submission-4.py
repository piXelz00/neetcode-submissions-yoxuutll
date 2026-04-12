class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        sor_list = sorted(nums)
        print(sor_list)
        max_chain = 1
        new_set = {}
        maxlen = []

        for i in range(len(sor_list)-1):

            if sor_list[i] != sor_list[i+1]:
                if sor_list[i] == sor_list[i+1]-1:                   
                    max_chain +=1 
                else:
                    maxlen.append(max_chain)
                    max_chain = 1
        maxlen.append(max_chain)    
        return max(maxlen) 

        

        