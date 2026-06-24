"""
INTERVIEW ROUTINE

1. UNDERSTAND
   - Restate in own words. Input/output types? Constraints? Edge cases?

            - input is a list heights[] from 0 to 100
            - output is area (base * height)


                wall doesnt count so maybe l = 1 and r = n - 2

                have to keep track of all walls


            - [0,2,0,3,1,0,1,3,2,1]
                 ^             ^

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

   l = 0, r = len(heights) - 1
   l_max = 0
   r_max = 0

   max_water = 0

   while l < r:

      if l_max < r_max:
         l_max = max(l_max, heights[l])
         max_water += l_max - height[l]
         l += 1
         continue
      else:
         r_max = max(r_max, heights[r])
         max_water += r_max - height[r]
         r -= 1
         continue



      

         




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
    def trap(self, height: List[int]) -> int:

      if len(height) < 1:
         return 0

      l = 0
      r = len(height) - 1
      l_max = height[0]
      r_max = height[len(height) - 1]
         
      max_water = 0

      while l < r:

         if l_max < r_max:
            l += 1
            l_max = max(l_max, height[l])
            max_water += l_max - height[l]
            continue
         else:
            r -= 1
            r_max = max(r_max, height[r])
            max_water += r_max - height[r]
            continue

      return max_water



      
        