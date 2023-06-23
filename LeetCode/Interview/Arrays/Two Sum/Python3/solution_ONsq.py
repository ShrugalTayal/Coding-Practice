class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through each element in the array
        for i in range(len(nums)):
            # Iterate through the remaining elements after i
            for j in range(i+1, len(nums)):
                # Check if the sum of nums[i] and nums[j] equals the target
                if nums[i] + nums[j] == target:
                    # If found, return the indices as a list
                    return [i, j]
