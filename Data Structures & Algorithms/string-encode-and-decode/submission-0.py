class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        split_them = ""

        for _ascii in strs:
            for char in _ascii:
                encoded_str += str(ord(char)) + "#"
            encoded_str += "|"


        return encoded_str




    def decode(self, s: str) -> List[str]:

        first_split = self.split(s,'|')

        words_list = [] 
        for i in first_split:
            word = self.split(i,'#')
            words_list.append(word)
        
        return self.word_decoder(words_list)
        




    def split(self,strs,char) -> List[str]:
        
        breaking_point =  "" 
        split_em = []

        for i in strs:
            if  i == char:
                split_em.append(breaking_point)
                breaking_point =  ""
            else:
                breaking_point+=i
        return split_em



    def word_decoder(self,words):
        str_adder = ""
        decoded_list = []
        for i in words:
            for j in i:
                 words_char = chr(int(j))
                 str_adder+=words_char
            decoded_list.append(str_adder)
            str_adder = ""
        return decoded_list


