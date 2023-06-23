**Intersection of Two Arrays II**
**Problem Description:**

You are given two integer arrays `nums1` and `nums2`, where `nums1` is an input array and `nums2` is a subset of `nums1`. You need to find the intersection of `nums1` and `nums2` and return the result as an array.

The intersection of two arrays contains elements that are common to both arrays, and the order of the elements in the result should match the order in which they appear in `nums1`.

**Example:**

```plaintext
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

**Constraints:**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

**Approach:**

To find the intersection of two arrays, you can use a hash map to store the counts of each element in `nums1`. Then, iterate through `nums2` and check if each element exists in the hash map. If it does, decrease the count and add the element to the result array.

**Pseudocode:**

1. Initialize an empty hash map `countMap` to store the counts of elements in `nums1`.
2. Iterate through each element `num` in `nums1`:
     - Increment the count of `num` in `countMap`.
3. Initialize an empty result array `result`.
4. Iterate through each element `num` in `nums2`:
     - If `num` exists in `countMap` and its count is greater than 0:
         - Append `num` to `result`.
         - Decrease the count of `num` in `countMap`.
5. Return the `result` array.
