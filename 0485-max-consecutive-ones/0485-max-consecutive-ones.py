class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        ma=0
        co=0
        while left<=right:
            if nums[left]==0:
                if co>ma:
                    ma=co
                co=0
            else:
                co+=1
            left+=1
        if co>ma:
            ma=co
        return ma
            
