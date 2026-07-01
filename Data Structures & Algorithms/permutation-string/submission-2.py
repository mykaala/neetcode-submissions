class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter()

        for i in range(len(s1)):
            window[s2[i]] += 1

        if window == need:
            return True

        left = 0

        for right in range(len(s1), len(s2), 1):
            
            window[s2[right]] += 1
            window[s2[left]] -= 1
            left += 1

            if window == need:
                return True

            


            
        return False






