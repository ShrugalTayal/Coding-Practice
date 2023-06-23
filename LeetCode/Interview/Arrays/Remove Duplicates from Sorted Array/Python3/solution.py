class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Create a reference list with unique elements by converting 'nums' to a set
        ref = list(set(nums))
        
        # Sort the reference list in ascending order
        ref.sort()
        
        # Iterate over the length of the reference list
        for i in range(len(ref)):
            # Update 'nums' with the values from the sorted reference list
            nums[i] = ref[i]
        
        # Return the length of the modified 'nums' list
        return len(ref)
