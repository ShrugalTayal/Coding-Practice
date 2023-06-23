import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        
        // Iterate through each element in the array
        for (int i = 0; i < nums.length; i++) {
            // Iterate through the remaining elements to find a pair that sums to the target
            for (int j = i + 1; j < nums.length; j++) {
                // Check if the current pair sums to the target
                if (target == nums[i] + nums[j]) {
                    // Store the indices of the pair in the result array
                    result[0] = i;
                    result[1] = j;
                    return result; // Return the result array
                }
            }
        }
        
        return result; // Return the default result array if no pair is found
    }
}
