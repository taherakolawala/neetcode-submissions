from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        windowSize = 0
        left = 0
        best = 0
        for right in range(len(s)):
            window[s[right]] += 1
            windowSize += 1
            if windowSize - max(window.values()) <= k:
                best = max(best, windowSize)
            while windowSize - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
                windowSize -= 1
        return best