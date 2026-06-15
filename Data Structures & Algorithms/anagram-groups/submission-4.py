class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        seen = {}

        for str in strs:
            count = [0] * 26 #counter list
            

            for c in str:
                ascii_val = ord(c) - ord('a')
                count[ascii_val] += 1

            key = tuple(count)
            
            if key not in seen:
                seen[key] = [str]
            else:
                seen[key].append(str)

        return list(seen.values())
            

        
            

