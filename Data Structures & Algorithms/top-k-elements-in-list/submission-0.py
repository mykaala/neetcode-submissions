class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        nums = [1,2,2,3,3,3], k = 2 
        
        "top 2 most frequent" -> 3 and 2

        output: [2,3]

        use Counter()

        sort Counter by values

        """

        seen = Counter()

        for n in nums:
            seen[n] += 1

        res = sorted(seen.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in res[:k]]