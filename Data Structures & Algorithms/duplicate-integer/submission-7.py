class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        a = set()
        for i in nums:
            if i in a:
                return True

            a.add(i)
        return False
    