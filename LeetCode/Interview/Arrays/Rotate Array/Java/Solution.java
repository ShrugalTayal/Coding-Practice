import java.util.Arrays;

class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length; // Normalize k to be within the range of 0 to nums.length - 1

        int[] rotated = new int[nums.length]; // Create a new array to store the rotated elements
        System.arraycopy(nums, 0, rotated, k, nums.length - k); // Copy the first nums.length - k elements to the rotated array
        System.arraycopy(nums, nums.length - k, rotated, 0, k); // Copy the last k elements to the rotated array

        System.out.println(Arrays.toString(rotated)); // Print the rotated array

        for (int i = 0; i < nums.length; i++) {
            nums[i] = rotated[i]; // Update the original array with the rotated elements
        }

        System.out.println(Arrays.toString(nums)); // Print the modified original array
    }
}
