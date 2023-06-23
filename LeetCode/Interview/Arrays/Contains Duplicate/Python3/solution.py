class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Convert the list to a set to remove duplicates
        # If the length of the set is not equal to the length of the original list,
        # it means there were duplicates in the list
        return len(set(nums)) != len(nums)
