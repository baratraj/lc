from typing import List
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            target_num = target - nums[i]
            if target_num in nums:
                return [i, nums.index(target_num)]


def test_two_sum():
    # Create an instance of Solution class
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9),  # should return [0, 1]
        ([3, 2, 4], 6),       # should return [1, 2]
        ([3, 3], 6)           # should return [0, 1]
    ]
    
    # Run test cases
    for nums, target in test_cases:
        result = solution.twoSum(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {result}")
        print("-" * 30)

if __name__ == "__main__":
    test_two_sum()

