"""
INTERVIEW ROUTINE

1. UNDERSTAND
   - Restate in own words. Input/output types? Constraints? Edge cases?

        - Given a list of heights [1,7,2,5,4,7,3,6]
                                     ^           ^

        - determine max area of water (base * height)
            - base = right - left
            - height = min(height[left], height[right])



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
                                    [1,7,2,5,4,7,3,6]
                                        ^          ^

    l = 0
    r = len(heights) - 1

    max_area = -1

    while l < r:

        height = min(heights[left], heights[right])
        base = r - l
        curr_area = height * base
        
        if curr_area > max_area:
            max_area = curr_area

        if heights[l] <= heights[r]:
            l += 1
            continue
        
        if heights[l] > heights[r]:
            r -= 1
            continue

    return max_area


   # step 2
   # step 3

6. CODE IT
   - Talk through each line. Good variable names. Flag edge cases.

7. DRY RUN YOUR CODE
   - Trace actual code with real values. Don't just eyeball it.

8. COMPLEXITY (confirm)
   - Time: dominant operation?
        O(n) because worst case is one pointer stays and the other traverses through whole thing.
   - Space: extra structures created?
        O(1) because were only keeping track of a static max_area, curr area, and pointers that does not grow in size after initialization only mutated
"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_area = -1

        while l < r:

            height = min(heights[l], heights[r])
            base = r - l
            curr_area = height * base
            
            if curr_area > max_area:
                max_area = curr_area

            if heights[l] <= heights[r]:
                l += 1
                continue
            
            if heights[l] > heights[r]:
                r -= 1
                continue

        return max_area
        
        