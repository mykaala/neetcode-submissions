class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        """
        Input: nums = [0,3,2,5,4,6,1,1] 
        7
        """

        seen = set(nums)
        max_count = 0
  
        for n in seen:
            if (n-1) not in seen:
                count = 1
                while n+1 in seen:
                    count += 1
                    n += 1

                max_count = max(count, max_count)
            

        return max_count



            