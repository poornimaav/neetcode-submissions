class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        for i in nums:
            if i not in temp:
                temp[i] = 0

            temp[i] +=1

        sorted_temp = (sorted(temp, key=lambda x: temp[x], reverse=True))
        print(sorted_temp)
        return sorted_temp[:k]

