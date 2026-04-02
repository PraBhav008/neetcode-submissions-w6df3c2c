class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter


        dictOfArr = Counter(nums).most_common(k)
        FrequentElementsArr = []

        for items in dictOfArr:
            FrequentElementsArr.append(items[0])
            

        return FrequentElementsArr
            