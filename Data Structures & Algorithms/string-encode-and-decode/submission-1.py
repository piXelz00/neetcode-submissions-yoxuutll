class Solution:
    def encode(self, strs: List[str]) -> str:

        encoded_str = ""
        WORD_DELIMITER = "|"
        CHAR_DELIMITER = "#"

        for word in strs:
            for char in word:
                encoded_str += str(ord(char)) + CHAR_DELIMITER
            encoded_str += WORD_DELIMITER

        return encoded_str

    def decode(self, s: str) -> List[str]:

        WORD_DELIMITER = "|"
        CHAR_DELIMITER = "#"

        encoded_words = self.split_by_delimiter(s, WORD_DELIMITER)
        encoded_chars  = self.split_words_into_char_codes(encoded_words, CHAR_DELIMITER)

        return self.char_codes_to_words(encoded_chars)

    def split_words_into_char_codes(self, encoded_words, char_delimiter):
        char_codes_per_word = []
        for word in encoded_words:
            char_codes = self.split_by_delimiter(word, char_delimiter)
            char_codes_per_word.append(char_codes)
        return char_codes_per_word

    def split_by_delimiter(self, text, delimiter) -> List[str]:
        current_token = ""
        tokens = []
        for char in text:
            if char == delimiter:
                tokens.append(current_token)
                current_token = ""
            else:
                current_token += char
        return tokens

    def char_codes_to_words(self, char_codes_per_word):
        decoded_words = []
        for char_codes in char_codes_per_word:
            word = ""
            for code in char_codes:
                if code:                    
                    word += chr(int(code))
            decoded_words.append(word)
        return decoded_words