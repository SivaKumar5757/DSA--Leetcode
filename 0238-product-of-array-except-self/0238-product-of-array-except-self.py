class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr=1
        z=nums.count(0)
        if z>1:
            return [0]*len(nums)
        for i in nums:
            if i!=0:
                pr*=i
        for i in range(len(nums)):
            if z==1:
                if nums[i]==0:
                    nums[i]=pr
                else:
                    nums[i]=0
            else:
                nums[i]=pr//nums[i]
        return nums
        