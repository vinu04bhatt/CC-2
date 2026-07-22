class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = k
        right = k
        
        current_min = nums[k]
        max_score = current_min
        
        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] < nums[right + 1]:
                right += 1
            else:
                left -= 1
                
            current_min = min(current_min, nums[left], nums[right])
            current_score = current_min * (right - left + 1)
            max_score = max(max_score, current_score)
            
        return max_score
