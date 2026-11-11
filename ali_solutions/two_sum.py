def twoSum(self, nums: list[int], target: int) -> list[int]:
    user_hash_table = {}
    for i in range(len(nums)):
        if (target - nums[i]) in user_hash_table:
            return [i, user_hash_table[(target - nums[i])]]
        user_hash_table[nums[i]] = i
