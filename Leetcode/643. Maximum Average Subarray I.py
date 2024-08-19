class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k>=len(nums):
            return sum(nums)/float(k)
        array = nums[:k]
        summ = sum(array)
        max_sum = summ
        for i in range(1, len(nums)-k+1):
            prev, last = nums[i-1], nums[k+i-1]
            summ = summ+last-prev
            max_sum = max(max_sum ,summ)
        print(max_sum)
        return max_sum/float(k)
            

        