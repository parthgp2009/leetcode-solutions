class Solution:
    def reverseVowels(self, s: str) -> str:
        a=set("aeiouAEIOU")
        l=list(s)
        left,right=0,len(s)-1
        while left<right:
            if l[left] not in a:
                left+=1
            elif l[right] not in a:
                right-=1
            else:
                l[left],l[right]=l[right],l[left]
                left+=1
                right-=1
        return("".join(l))