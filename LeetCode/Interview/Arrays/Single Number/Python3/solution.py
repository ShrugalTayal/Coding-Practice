class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Iterate over each unique element in the set of nums
        for ele in set(nums):
            # Check if the count of the element is equal to 1
            if nums.count(ele) == 1:
                # If found, return the element
                return ele
