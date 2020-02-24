class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        oneindex, twoindex = 0, 0
        for i in range(1, len(nums)):
            twoindex += 1
            if nums[oneindex] != nums[twoindex]:
                nums[oneindex + 1] = nums[twoindex]
                oneindex += 1
        return oneindex + 1