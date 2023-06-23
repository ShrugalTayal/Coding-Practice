import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        // Create HashMaps to store the count of elements in nums1 and nums2
        HashMap<Integer, Integer> hmap1 = new HashMap<>();
        HashMap<Integer, Integer> hmap2 = new HashMap<>();

        // Count the occurrences of elements in nums1
        for (int i : nums1) {
            int count = hmap1.getOrDefault(i, 0);
            hmap1.put(i, count + 1);
        }

        // Count the occurrences of elements in nums2
        for (int i : nums2) {
            int count = hmap2.getOrDefault(i, 0);
            hmap2.put(i, count + 1);
        }

        // Create a temporary array to store the intersection elements
        int[] temp = new int[Math.min(nums1.length, nums2.length)];
        Arrays.fill(temp, -1);  // Initialize the temporary array with -1
        int index = 0;

        // Find the intersection of elements between nums1 and nums2
        for (int i : nums1) {
            int count1 = hmap1.get(i);
            int count2 = hmap2.getOrDefault(i, 0);

            // Set the counts to 0 to mark that the element has been used
            hmap1.put(i, 0);
            hmap2.put(i, 0);

            // Find the minimum count of the element occurrence
            int min = Math.min(count1, count2);

            // Add the element to the temporary array min times
            for (int j = 0; j < min; j++) {
                temp[index] = i;
                index++;
            }
        }

        // Count the number of -1s in the temporary array
        int count = 0;
        for (int i : temp) {
            if (i == -1) {
                count++;
            }
        }

        // Create the final array with non-negative elements from the temporary array
        int[] ans = new int[temp.length - count];
        int ansIndex = 0;
        for (int i : temp) {
            if (i != -1) {
                ans[ansIndex] = i;
                ansIndex++;
            }
        }

        return ans;
    }
}
