import math
class Solution(object):
    def missingNumber(self, nums):
        isZeroFound = False
        soma = 0

        expectedSum = 0
        for i in nums:
            if i == 0:
                isZeroFound = True
            soma += i


        if not isZeroFound:
            return 0

        n = len(nums);
        expectedSum = (n*(n + 1))/2
        return expectedSum - soma

        """
        :type nums: List[int]
        :rtype: int
        """

sol = Solution();

x = Solution.missingNumber(sol,[2,0]);
print x
