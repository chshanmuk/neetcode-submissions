class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        word_count = {}
        for i in s:
            word_count[i]=word_count.get(i,0)+1
        for i in t:
            word_count[i]=word_count.get(i,0)-1
        for i in word_count:
            if word_count[i]!=0:
                return False
        return True

