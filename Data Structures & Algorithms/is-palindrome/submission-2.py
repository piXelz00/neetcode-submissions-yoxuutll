class Solution:
    def isPalindrome(self, s: str) -> bool:
        


        left,right = 0,len(s)-1

        while left<right:
            if  not (48<=ord(s[left])<=57 or  65<=ord(s[left])<=90 or 97<=  ord(s[left])<= 122) :
                left +=1
            elif not (48<=ord(s[right])<=57 or  65<=ord(s[right])<=90 or 97<=  ord(s[right])<= 122) :
                right-=1
            else: 
                if s[left].lower() !=s[right].lower():
                    return False
                left +=1
                right-=1

        return True        




class Solution2:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer forward if it's not a letter/number
            if not s[left].isalnum():
                left += 1
            # Move right pointer backward if it's not a letter/number
            elif not s[right].isalnum():
                right -= 1
            # Both are alphanumeric, so compare them
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
                
        return True
        