class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unq = []
        for i in nums:
            if i in unq:
                return True

            unq.append(i)
        return False
