class Solution:
    def trap(self, height: List[int]) -> int:
        i = len(height)
        cnt = 0
        for p in range(1, i):
            lft = max(height[:p])
            rt = max(height[p:])
            point = height[p]
            roof = min(max(lft, point), max(rt, point))
            perdrop = roof - height[p]
            cnt += perdrop
        return cnt