class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lengthOfArr = len(nums)
        resultArr = [1] * lengthOfArr
        

        #prefix products.
        prefix = 1
        for i in range(lengthOfArr):
            resultArr[i] = prefix
            prefix *= nums[i]

        #suffix products.
        suffix = 1
        for i in range(lengthOfArr-1, -1, -1):
            resultArr[i] *= suffix
            suffix *= nums[i]

        return resultArr