from typing import List
class Solution:
    def longCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first_strs = strs[0]
        last_strs = strs[-1]
        s = ""
        for i in range(min(len(first_strs), len(last_strs))):
            if first_strs[i] == last_strs[i]:
                s += first_strs[i]
            else:
                break
        return s
        


# s = "latif"

# print(strs[0][1])
so = Solution()

strs = ["flower", "flow", "flight"]
print(so.longCommonPrefix(strs))