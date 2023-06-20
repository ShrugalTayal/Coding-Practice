from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Iterate over the elements of nums2 and assign them to the end of nums1
        # using negative indices
        for i in range(-1, -1 - n, -1):
            nums1[i] = nums2[i]

        # Sort the modified nums1 array
        nums1.sort()

        # No need to return nums1 explicitly (in-place modification)
