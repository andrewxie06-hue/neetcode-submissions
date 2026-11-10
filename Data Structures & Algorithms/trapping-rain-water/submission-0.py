class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) -1
        maxleft = height[left]
        maxright = height[right]
        while left < right:
            if maxleft < maxright:
                left += 1
                maxleft = max(maxleft, height[left])
                water += maxleft- height[left]
            else:
                right -= 1
                maxright = max(maxright, height[right])
                water += maxright- height[right]
            
          

        return water



