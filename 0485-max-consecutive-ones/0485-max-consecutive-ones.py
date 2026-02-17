class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        co=0
        ma=0
        for i in nums:
            if i==0:
                if ma<co:
                    ma=co
                co=0
            else:
                co+=1
        return max(ma,co)
            
            
