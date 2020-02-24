class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        L = len(nums)
        if L > k:
            new = []
            for i in range(L - k):
                new.append(nums.pop(0))
            nums.extend(new)
        if L == k:
            nums
        if L < k:
            new = []
            for i in range(k % L) :
                new = nums.pop()
                nums.insert(0, new)