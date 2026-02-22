class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x,n):
            if n==0:
                return 1
            if x==0:
                return 0
            res=rec(x,n//2)
            res=res*res
            if n%2==1:
                return res*x
            else:
                return res
        su=rec(x,abs(n))
        if n<0:
            su=1/su
        return su