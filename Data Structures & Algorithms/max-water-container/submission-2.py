class Solution:
    def maxArea(self, heights: List[int]) -> int:

        
        maxArea = 0
         
        for i ,value in enumerate(heights):
            left,right = i,len(heights)-1
            while left<right:
                area_cal = (right-left) * min(heights[left],heights[right])
                if area_cal >maxArea:
                    maxArea=area_cal
                right-=1
        return maxArea  
            
        