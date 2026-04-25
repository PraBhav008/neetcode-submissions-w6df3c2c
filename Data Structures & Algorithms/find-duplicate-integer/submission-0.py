class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicateVal = 0
        for i in range(len(nums)):
            count = 0
            duplicateVal = nums[i]
            for j in range(i, len(nums)):
                if duplicateVal == nums[j]:
                    count += 1
            
            if count > 1:
                return duplicateVal