class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        str1=""
        for i in range(len(s)-1,-1,-1):
            if s[i] in "aeiouAEIOU":
                l.append(s[i])
        for i in s:
            if i in "aeiouAEIOU":
                str1+=l[0]
                l.pop(0)
            else:
                str1+=i
        return str1