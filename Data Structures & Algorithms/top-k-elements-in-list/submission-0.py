class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_hash = self.nums_hashmap(nums)

        top_k = [ i for i in self.top_k(nums_hash,k)]
        return top_k




        


    def nums_hashmap(self,nums: List[int]):

        map = {}
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i]+=1
        return map     


    def top_k(self,num_hash,k):

        k_list = {}
        while len(k_list)!=k:
            max_num = 0
            max_key = 0
            for i in num_hash:
                
                if num_hash[i]>max_num and i not in k_list:
                    max_num = num_hash[i]
                    max_key = i
            k_list[max_key] = max_num
        return k_list



