class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing_nums = []
        for i in nums:
            if i in existing_nums:
                return True
            existing_nums.append(i)
        return False