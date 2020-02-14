##https://leetcode.com/problems/shortest-way-to-form-string/
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        cnt = 1
        i, j = 0, 0
        while j < len(target):
            tracker = target[j]
            pos = source.find(target[j], i)
            if pos == -1:
                if i == 0:
                    return -1
                cnt += 1
                i = 0
            else:
                i = pos + 1
                j += 1
        return cnt

d = Solution().shortestWay
print(d("xyz","xzyxz"))
