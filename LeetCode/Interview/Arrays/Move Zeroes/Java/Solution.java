import java.util.Arrays;

class Solution {
    public void moveZeroes(int[] nums) {
        int pointer = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != 0 && nums[pointer] == 0) {
                // Swap non-zero element with zero element
                int temp = nums[i];
                nums[i] = nums[pointer];
                nums[pointer] = temp;
                pointer++;
            } else if (nums[pointer] != 0) {
                pointer++;
            }
        }

        System.out.println(Arrays.toString(nums));
    }
}
