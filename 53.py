class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp[i]means the maximum subarray ending with A[i];
        """
        n = len(nums)
        dp = []
        dp.append(nums[0])
        m = dp[0]
        t = 0
        for i in range(1, n):
            if dp[i-1] > 0:
                t = dp[i-1]
            else:
                t = 0
            dp.append(t + nums[i])
            m = max(dp[i], m)
        return m
        