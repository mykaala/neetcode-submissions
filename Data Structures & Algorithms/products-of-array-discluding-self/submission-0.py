class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [1,2,4,6]
        Output: [48,24,12,8]


        left[] -> 
        left[0] = 1

        left[i] = left[i-1] * nums[i-1]

        right[] ->
        right[n-1] = 1

        right[i] = right[i+1] * nums[i+1]

        answer[i] = left[i] * right[i]
        """

        left = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            left[i] = left[i-1] * nums[i-1]

        right = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                continue
            right[i] = right[i+1] * nums[i+1]

        answer = [1] * len(nums)
        for i in range(len(answer)):
            answer[i] = left[i] * right[i]

        return answer

            

            


