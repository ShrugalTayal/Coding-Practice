class Solution {
    public int removeDuplicates(int[] nums) {
        // Check if the array is empty
        if (nums.length == 0) {
            return 0;
        } else {
            // Initialize a pointer to keep track of the unique elements
            int pointer = 0;
            
            // Iterate over the array starting from the second element
            for (int i = 1; i < nums.length; i++) {
                // If the current element is equal to the previous unique element, skip it
                if (nums[i] == nums[pointer]) {
                    continue;
                }
                // If the current element is different from the previous unique element
                else if (nums[i] != nums[pointer]) {
                    // Move the pointer to the next position
                    pointer = pointer + 1;
                    // Update the pointer position with the current unique element
                    nums[pointer] = nums[i];
                }
            }
            // Return the length of the modified array (pointer + 1)
            return pointer + 1;
        }
    }
}
