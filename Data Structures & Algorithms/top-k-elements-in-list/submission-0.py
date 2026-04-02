class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter


        dictOfArr = Counter(nums).most_common()
        FrequentElementsArr = []

        for items in dictOfArr:
            if k:
                FrequentElementsArr.append(items[0])
                k -= 1
            

        return FrequentElementsArr
            