class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ln1=len(nums1)
        ln2=len(nums2)
        le1=0
        le2=0
        med=(ln1+ln2)
        prev=0
        curr=0
        for i in range((med//2)+1):
            prev=curr
            if le1<ln1 and (le2>=ln2 or nums1[le1]<=nums2[le2]):
                curr=nums1[le1]
                le1+=1
            else:
                curr=nums2[le2]
                le2+=1
        if med%2==0:
            return (curr+prev)/2
        else:
            return curr
            



            
