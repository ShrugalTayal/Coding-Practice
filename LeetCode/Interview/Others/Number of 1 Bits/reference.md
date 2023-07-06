---

## Number of 1 Bits

**Problem Description:**

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

LeetCode Link: [Number of 1 Bits](https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/)

**Example 1:**

Input: `n = 00000000000000000000000000001011`
- The input binary represents the unsigned integer `11`.

Output: `3`
- The binary representation of `11` has three '1' bits.

**Example 2:**

Input: `n = 00000000000000000000000010000000`
- The input binary represents the unsigned integer `128`.

Output: `1`
- The binary representation of `128` has only one '1' bit.

**Example 3:**

Input: `n = 11111111111111111111111111111101`
- The input binary represents the unsigned integer `4294967293`.

Output: `31`
- The binary representation of `4294967293` has thirty-one '1' bits.

**Constraints:**

- The input must be a binary string of length `32`.

---

The problem "Number of 1 Bits" requires counting the number of '1' bits in a given 32-bit unsigned integer. The input is a binary string representing the unsigned integer, and the task is to count the number of '1' bits and return the count.
