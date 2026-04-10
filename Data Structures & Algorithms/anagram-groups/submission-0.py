class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            ana_dict = {}
            ana_list = []

            master_list = []

            for i in range(0,len(strs)):
                cw = strs[i]
                word_hash = self.word_into_hash_map(cw)
                if word_hash in ana_list:
                    hash_index= ana_list.index(word_hash)
                    ana_dict[hash_index].append(cw)
                else:
                    ana_list.append(word_hash)
                    hash_index= ana_list.index(word_hash)
                    ana_dict[hash_index] = [cw]
                    
            
            for i in ana_dict:
                master_list.append(ana_dict[i])

            return master_list    
        
        



    def word_into_hash_map(self,word):

        dict_hash = {}

        for i in range(0,len(word)):

            if word[i] in dict_hash:
                dict_hash[word[i]] = dict_hash[word[i]]+1
            else:
                dict_hash[word[i]] = 1


        return dict_hash   
            


        

