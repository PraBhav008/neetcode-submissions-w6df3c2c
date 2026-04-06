class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if not s or not t:
            return ""

        counter_t = Counter(t)
        window = {}

        have = 0
        need = len(counter_t)

        res = ""
        res_len = float("inf")

        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in counter_t and window[char] == counter_t[char]:
                have += 1

            while have == need:
                # update result
                if (right - left + 1) < res_len:
                    res = s[left:right + 1]
                    res_len = right - left + 1

                # shrink
                window[s[left]] -= 1
                if s[left] in counter_t and window[s[left]] < counter_t[s[left]]:
                    have -= 1

                left += 1

        return res