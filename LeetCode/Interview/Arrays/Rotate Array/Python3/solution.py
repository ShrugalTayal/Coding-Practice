class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # Normalize k to be within the range of 0 to n-1
        
        # Reverse the entire list
        nums.reverse()
        
        # Reverse the first k elements
        nums[0:k] = nums[0:k][::-1]
        
        # Reverse the remaining elements
        nums[k:] = nums[k:][::-1]
