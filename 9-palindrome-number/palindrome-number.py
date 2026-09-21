class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=0
        a=x
        while x>0:
            r=x%10
            n=(n*10)+r
            x//=10
        if n==a:
            return True
        else:
            return False