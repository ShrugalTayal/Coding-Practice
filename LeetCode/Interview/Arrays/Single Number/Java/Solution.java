class Solution {
    public int singleNumber(int[] nums) {
        // Create a HashMap to store the count of each element
        HashMap<Integer, Integer> hmap = new HashMap<Integer, Integer>();
        
        // Count the occurrences of each element in nums and store them in the HashMap
        for (int i : nums) {
            int count = hmap.getOrDefault(i, 0);
            hmap.put(i, count + 1);
        }
        
        // Variable to store the single number
        int ele = -1;
        
        // Iterate over nums to find the element with a count of 1
        for (int i : nums) {
            int count = hmap.get(i);
            if (count == 1) {
                ele = i;
            }
        }
        
        // Return the single number
        return ele;
    }
}
