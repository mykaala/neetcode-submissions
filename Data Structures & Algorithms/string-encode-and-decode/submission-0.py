class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            cnt = len(s)
            res += str(cnt)
            res += "#"
            res += s

        return res


    def decode(self, s: str) -> List[str]:

        res = []
        i=0
        while i < len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1

            count = int(count)
            res.append(s[i+1:i+count+1])
            i += count+1

        return res
                
                


"""
INTERVIEW ROUTINE

1. UNDERSTAND
   - Restate in own words. Input/output types? Constraints? Edge cases?

2. DRY RUN EXAMPLE
   - Trace given example by hand. Make one edge case.

   Input: strs = ["Hello","World"]

    encoded -> "Hello/World" must use some kind of delimiter, but cant

   Output: ["Hello","World"]



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