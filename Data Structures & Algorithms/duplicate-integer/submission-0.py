class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = set()

        for i in range(len(nums)):
            if nums[i] in h:
                return True
            else:
                h.add(nums[i])
        return False