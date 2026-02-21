class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        le=len(s)
        l=0
        c=0
        hm=set()
        m=0
        for i in s:
            c+=1
            while i in hm:
                hm.remove(s[l])
                l+=1
                c-=1
            hm.add(i)
            m=max(c,m)
        return m


        