class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return self.s(s) == self.t(t) 
        







    def s(self,s:str) -> Dict:
        dict_s = {}
        for i in s:
            if i in dict_s:
                dict_s[i] = dict_s[i] + 1
            else:
                dict_s[i] = 0
        return dict_s


    def t(self,t:str) -> Dict:
        dict_t = {}
        for i in t:
            if i in dict_t:
                dict_t[i] = dict_t[i] + 1
            else:
                dict_t[i] = 0
        return dict_t



        



        return dict_s == dict_t 


        
        


        

