import java.util.HashMap;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> hmap = new HashMap<Integer, Integer>();

        // Count the occurrences of each element in the nums array
        for (int i : nums) {
            // Get the current count of the element from the HashMap
            // If the element is not present, default count to 0
            int count = hmap.getOrDefault(i, 0);
            
            // Increment the count by 1 and update the HashMap
            hmap.put(i, count + 1);
        }

        // Iterate over the nums array again to check for duplicate elements
        for (int i : nums) {
            int count = 0;
            
            // Get the count of the current element from the HashMap
            count = hmap.get(i);
            
            // If the count is greater than 1, it means the element is a duplicate
            // Return true to indicate the presence of duplicates
            if (count > 1) {
                return true;
            }
        }
        
        // No duplicates found, return false
        return false;
    }
}
