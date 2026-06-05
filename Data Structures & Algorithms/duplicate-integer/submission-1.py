class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        """
        nums = [1, 2, 3, 3] -> true
        nums = [1, 2, 3, 4] -> false


        seen = {1, }

        """

        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False