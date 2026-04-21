class Solution:
    def maxArea(self, heights: List[int]) -> int:
            maxArea = 0         
            left,right = 0,len(heights)-1
            while left<right:
                required_min = min(heights[left],heights[right])
                area_cal = (right-left) * required_min
            
                if area_cal>maxArea:
                    maxArea=area_cal    

                if heights[right]==required_min:
                    right-=1

                if heights[left]==required_min:
                    print(required_min)
                    left+=1

            return maxArea  
            
        