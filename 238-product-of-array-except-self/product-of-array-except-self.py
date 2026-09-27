class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        l=[1]*n
        a=1
        for i in range(n):
            l[i]=a
            a*=nums[i]
        b=1
        for i in range(n-1,-1,-1):
            l[i]*=b
            b*=nums[i]
        return l