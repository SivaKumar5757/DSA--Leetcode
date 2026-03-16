class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        li=matrix
        left=0
        right=len(li[0])-1
        bottom=len(li)-1
        top=0
        res=[]
        while left<=right and top<=bottom:
            j=left
            while j<right+1 and top<=bottom:
                res.append(li[top][j])
                j+=1
            top+=1
            j=top
            while j<bottom+1 and left<=right:
                res.append(li[j][right])
                j+=1
            right-=1
            j=right
            while j>left-1 and top<=bottom:
                res.append(li[bottom][j])
                j-=1
            bottom-=1
            j=bottom
            while j>top-1 and left<=right:
                res.append(li[j][left])
                j-=1
            left+=1
        return res
