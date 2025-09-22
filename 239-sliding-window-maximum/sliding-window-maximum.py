from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        dq = deque()

        for right in range(len(nums)):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            if dq[0] <= right - k:
                dq.popleft()

            if right >= k - 1:
                res.append(nums[dq[0]])

        return res