class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2147483648 and divisor==-1 :
            return 2147483647

        neg=(dividend<0)^(divisor<0)
        dividend,divisor=abs(dividend),abs(divisor)
        q=0
        while divisor <= dividend:
            mul=1
            temp=divisor
            while dividend>=(temp<<1):
                temp<<=1
                mul<<=1
            q+=mul
            dividend-=temp
        return q if not neg else -q