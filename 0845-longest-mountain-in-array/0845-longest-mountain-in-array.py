class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ln=len(arr)
        inr=[0]*ln
        dcr=[0]*ln
        for i in range(1,ln):
            if arr[i-1]<arr[i]:
                inr[i]=inr[i-1]+1
        for i in range(ln-2,0,-1):
            if arr[i+1]<arr[i]:
                dcr[i]=dcr[i+1]+1
        # print(inr)
        # print(dcr)
        ma=0
        for i in range(ln):
            if inr[i]>0 and dcr[i]>0:
                ma=max(ma,inr[i]+dcr[i]+1)
        return ma