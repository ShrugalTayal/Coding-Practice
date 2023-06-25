class Solution {
    public int strStr(String haystack, String needle) {
        // Check if the length of needle and haystack is 1 and they are equal
        if (needle.length() == 1 && haystack.length() == 1 && haystack.equalsIgnoreCase(needle)) {
            return 0;
        } else {
            // Iterate through haystack with sliding window of length needle
            for (int i = 0; i <= (haystack.length() - needle.length()); i++) {
                // Extract substring of haystack with length needle
                String temp = haystack.substring(i, i + needle.length());
                // Check if the extracted substring is equal to needle ignoring case
                if (temp.equalsIgnoreCase(needle)) {
                    return i; // Return the starting index of the substring
                }
            }
            return -1; // Return -1 if needle is not found in haystack
        }
    }
}
