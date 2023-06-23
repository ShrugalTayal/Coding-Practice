class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through each element in the array
        for i in range(len(nums)):
            try:
                # Check if the difference between target and nums[i] exists in the array
                if (target - nums[i]) in nums and nums.index(target - nums[i]) != i:
                    # If found, return the indices of nums[i] and the complement as a list
                    return [i, nums.index(target - nums[i])]
            except:
                pass
