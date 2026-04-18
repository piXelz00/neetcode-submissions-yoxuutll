class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        sanitized_s=[]
        for i in s:
            if  (48<=ord(i)<=57 or  65<=ord(i)<=90 or 97<=  ord(i)<= 122) :
                sanitized_s.append(i.lower())

        
        

        left,right = 0,len(sanitized_s)-1

        while left<right:

            if sanitized_s[left] !=sanitized_s[right]:
                return False

            left +=1
            right-=1

        return True        

        