class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for i in strs:
            a = sorted(i)
            a = ''.join(a)

            if a not in temp:
                temp[a] = []

            temp[a].append(i)
        return list(temp.values())

            