class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for i in s:
            chars[i] = chars.get(i, 0)+ 1

        for j in t:

            if j not in chars:
                return False

            chars[j] -=1

            if chars[j] < 0:
                return False

            

        return True
            



        