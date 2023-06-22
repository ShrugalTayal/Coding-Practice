class Solution {
    // Function is to check whether two strings are anagram of each other or not.
    public static boolean isAnagram(String a, String b) {
        // Check if lengths of the strings are different
        if (a.length() != b.length()) {
            return false;
        }
        
        // Convert the strings to character arrays
        char[] arr_a = a.toCharArray();
        char[] arr_b = b.toCharArray();

        // Create a HashMap to store the character counts of string b
        HashMap<Character, Integer> hmap_b = new HashMap<>();
        
        // Count the occurrences of each character in string b and store in the HashMap
        for (int i = 0; i < arr_b.length; i++) {
            int count = hmap_b.getOrDefault(arr_b[i], 0);
            hmap_b.put(arr_b[i], count + 1);
        }
        
        // Check if the character counts in string a match the counts in the HashMap
        for (int i = 0; i < arr_a.length; i++) {
            int count = hmap_b.getOrDefault(arr_a[i], 0);
            if (count == 0) {
                // If a character in string a is not present in string b or its count is 0, return false
                return false;
            } else {
                hmap_b.put(arr_a[i], count - 1);
            }
        }
        
        return true;
    }
}
