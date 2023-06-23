class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0  # Initialize a pointer to track the position to place non-zero elements
        
        if 0 not in nums:  # If there are no zeros in the list, print the list and return
            print(nums)
        else:
            for i in range(1, len(nums)):
                if nums[i] != 0 and nums[pointer] == 0:
                    # If the current element is non-zero and the element at the pointer is zero,
                    # swap the two elements and increment the pointer
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer = pointer + 1
                
                if nums[pointer] != 0:
                    # If the element at the pointer is non-zero, increment the pointer
                    pointer = pointer + 1
            
            print(nums)
