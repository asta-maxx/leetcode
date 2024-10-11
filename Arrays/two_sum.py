from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store number and its index
        num_map = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is present in the dictionary
            if complement in num_map:
                return [num_map[complement], i]
            
            # Add the number and its index to the dictionary
            num_map[num] = i
