class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        le=0
        ri=len(nums)-1
        def binsea(le,ri,nums,ff):
            ans=-1
            while le<=ri:
                mid=(le+ri)//2
                if nums[mid]<target:
                    le=mid+1
                elif nums[mid]>target:
                    ri=mid-1
                else:
                    ans=mid
                    if ff:
                        ri=mid-1
                    else:
                        le=mid+1
            return ans
        return [binsea(le,ri,nums,True),binsea(le,ri,nums,False)]



        