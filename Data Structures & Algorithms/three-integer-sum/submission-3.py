class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        #   [-4,-1,-1,0,1,2]

        for i in range(0, len(nums)):

            l = i+1
            r = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l<r:
                if nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                    continue
                if nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                    continue

                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1]: #duplicate check
                        l = l+1
        return res

        
