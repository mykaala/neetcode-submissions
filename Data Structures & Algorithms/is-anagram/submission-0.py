class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Input: s = "racecar", t = "carrace"
        Output: true


        need to keep track of:
        1. letters
        2. freq of each letter
        -> count()

        chars = count()

        s_char = count(s)
        t_char = count(t)

        return s_char == t_char

        T(n) = O(n)
        S(n) = O(n)
        """
        s_char = Counter(s)
        t_char = Counter(t)

        return s_char == t_char