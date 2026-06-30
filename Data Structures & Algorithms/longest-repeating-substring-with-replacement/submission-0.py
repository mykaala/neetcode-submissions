class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        left = 0
        seen = {}
        most_freq = 0
        longest = 0

        for right in range(len(s)):

            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1

            most_freq = max(most_freq, seen[s[right]])

            if (right - left + 1) - most_freq > k: #window breaks -> slide left
                #reduce count of the excluded character
                seen[s[left]] -= 1
                #slide left
                left += 1

            longest = max(longest, right - left + 1)

        return longest
            


            
