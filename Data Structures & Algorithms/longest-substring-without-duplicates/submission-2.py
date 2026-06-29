class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 1:
            return 0
        
        left = 0
        max_count = 0

        seen = {}

        for right in range(len(s)):
        
            if s[right] not in seen:
                #add new char to seen
                seen[s[right]] = right
            else: #dupe
                #move left if new char is in window
                if left <= seen[s[right]]:
                    left = seen[s[right]] + 1
                #update old index to new index
                seen[s[right]] = right

            max_count = max(max_count, right - left +1)

        return max_count

