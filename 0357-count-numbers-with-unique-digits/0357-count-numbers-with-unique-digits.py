class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def rec (le,li):
            if le==n:
                return 0
            c=0
            for i in range(0,10):
                if i == 0 and len(li) == 0:
                    continue
                if i not in li:
                    li.append(i)
                    c+=1
                    c+=rec(le+1,li)
                    li.pop()
            return c
        return rec(0,[])+1
