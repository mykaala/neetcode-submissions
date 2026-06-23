"""
INTERVIEW ROUTINE

1. UNDERSTAND
   - Restate in own words. Input/output types? Constraints? Edge cases?

    - ignores everything other than alphabet (cap and lc) and numbers: isalnum()
    - returns boolean:
        - check if false
        - otherwise return True

    


2. DRY RUN EXAMPLE
   - Trace given example by hand. Make one edge case.


    Input: s = "Was it a car or a cat I saw?"
                "wasitacar oracatisaw" 19 // 2 = 9 could use stack

    two pointers

    Input: s = "Was it a car or a cat I saw?"
                "wasitacaroracatisaw"
                    ^           ^

                 while l < r:


                    l += 1
                    r -= 1



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
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1
        s = s.lower()


        #    "Was it a car or a cat I saw?"
        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
                
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True



















        