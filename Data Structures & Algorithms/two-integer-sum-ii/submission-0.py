"""
INTERVIEW ROUTINE

1. UNDERSTAND
   - Restate in own words. Input/output types? Constraints? Edge cases?

2. DRY RUN EXAMPLE
   - Trace given example by hand. Make one edge case.

3. PATTERN
   - Count something? → Counter/hashmap
   - Fast lookup? → hashset/hashmap
   - Need order? → sort/heap
   - Sorted input? → binary search/two pointers
   - Running window? → sliding window
   - Explore paths? → BFS/DFS

4. APPROACH + COMPLEXITY (before coding)
   - "I'll use X because Y"
   - Brute force first, then optimize
   - Rough T(n) and space guess

5. PSEUDOCODE
   # step 1
   # step 2
   # step 3

6. CODE IT
   - Talk through each line. Good variable names. Flag edge cases.

7. DRY RUN YOUR CODE
   - Trace actual code with real values. Don't just eyeball it.

8. COMPLEXITY (confirm)
   - Time: dominant operation?
   - Space: extra structures created?
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
                continue
            elif numbers[l] + numbers[r] > target:
                r -= 1
                continue

            return [l+1, r+1]

        return []
            















         