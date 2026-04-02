class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        startOfSequence = -1
        lenOfLongestS = 0
        setOfNums = set(nums)

        for num in setOfNums:
            if num - 1 not in setOfNums:
                maxLen = 1
                current = num
                while current + 1 in setOfNums:
                    current += 1
                    maxLen += 1

                lenOfLongestS = max(lenOfLongestS, maxLen)
            
            

        return lenOfLongestS