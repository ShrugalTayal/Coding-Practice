class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Initialize an empty list to store the intersection elements
        ans = []
        
        # Iterate over each unique element in nums1
        for i in set(nums1):
            try:
                # Find the minimum count of the current element in both nums1 and nums2
                count = min(nums1.count(i), nums2.count(i))
                
                # Extend the ans list with the current element repeated count times
                ans.extend([i] * count)
            except:
                # Handle any exception that may occur and continue the loop
                continue
        
        # Return the final list of intersection elements
        return ans
