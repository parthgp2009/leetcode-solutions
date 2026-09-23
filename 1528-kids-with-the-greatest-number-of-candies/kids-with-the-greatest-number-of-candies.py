class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        n=max(candies)
        l=[]
        for i in candies:
            l.append(i+extraCandies>=n)
        return l