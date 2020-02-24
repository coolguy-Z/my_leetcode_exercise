class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = []
        for i in range(len(nums)):
            if nums[i] == 0:
                l.append(i)
        for j in range(len(l)):
            nums.remove(0)
            nums.append(0)
        return nums