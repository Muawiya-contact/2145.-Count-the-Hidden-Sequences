# 🧠 LeetCode Problem 2145: Count the Hidden Sequences

> **Difficulty**: Medium  
> **Topic**: Arrays, Prefix Sum  
> **Platform**: LeetCode  
> **Solved by**: [Muawiya - Coding Moves](https://www.youtube.com/@Coding_Moves)

---

## 🚀 Problem Statement

You are given a 0-indexed array of integers `differences`, which describes the difference between consecutive elements of a hidden sequence.  
You are also given two integers `lower` and `upper`, representing the inclusive bounds that **every element** in the hidden sequence must lie within.

Your goal is to determine **how many possible hidden sequences** can be constructed that satisfy:
- Each difference matches the one given.
- All elements are within the `[lower, upper]` range.

---

## 🧩 Example

### ✅ Example 1:
```text
Input:  differences = [1, -3, 4], lower = 1, upper = 6  
Output: 2  
Explanation:
Valid sequences:
  - [3, 4, 1, 5]
  - [4, 5, 2, 6]
```
# 🧠 Solution Strategy
Let the hidden sequence be [x, x+diff1, x+diff1+diff2, ...]
+ To ensure all values stay in [lower, upper], we calculate the prefix sum of differences to track how much the value drifts from x.

# Key Observations:
+ Let curr_sum be the cumulative sum of differences.

+ Track:

  - min_sum = minimum prefix sum

  - max_sum = maximum prefix sum

+To ensure all values are in bounds:
```
lower <= x + min_sum
upper >= x + max_sum
```
+ Solve for x:
```
x ∈ [lower - min_sum, upper - max_sum]
```
So, the number of valid values for x is:
```
max(0, (upper - max_sum) - (lower - min_sum) + 1)
```
# ✅ Python Code (Efficient – O(n) Time)
```
class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        curr = 0
        min_sum = 0
        max_sum = 0

        for diff in differences:
            curr += diff
            min_sum = min(min_sum, curr)
            max_sum = max(max_sum, curr)

        low_x = lower - min_sum
        high_x = upper - max_sum

        return max(0, high_x - low_x + 1)
```
# 📈 Time & Space Complexity
+ Time Complexity: O(n)

+ Space Complexity: O(1)

# 🎥 Watch It on YouTube
📺 Coding tutorial and explanation by Muawiya from <a href="https://www.youtube.com@Coding_Moves">Coding Moves</a>
Subscribe for more algorithm explanations, AI projects, and coding challenges!
