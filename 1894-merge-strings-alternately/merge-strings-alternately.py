class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final=""
        n=max(len(word1),len(word2))
        for i in range(n):
            if i<len(word1):
                final+=word1[i]
            if i<len(word2):
                final+=word2[i]
        return final