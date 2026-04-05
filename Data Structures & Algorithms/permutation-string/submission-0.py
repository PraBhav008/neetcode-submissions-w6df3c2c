class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        counter_s1 = Counter(s1)
        dictForMatch = {}
        lenOfS1 = len(s1)

        for right in range(len(s2)):
            dictForMatch[s2[right]] = dictForMatch.get(s2[right], 0) + 1

            if right - left + 1 > lenOfS1:
                dictForMatch[s2[left]] -= 1

                if dictForMatch[s2[left]] == 0:
                    del dictForMatch[s2[left]]

                left += 1
                
            if right - left + 1 == lenOfS1 and counter_s1 == dictForMatch:
                return True

        return False