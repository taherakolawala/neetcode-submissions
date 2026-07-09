class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        char_counts = {}
        window_size = 0
        best = 0
        for right in range(len(s)):
            char_counts[s[right]] = char_counts.get(s[right], 0) + 1
            window_size += 1
            if (window_size - max(char_counts.values()) <= k):
                best = max(best, window_size)
            print(window_size, " ", max(char_counts.values()), " best:", best, " ", s[left:right+1])
            while window_size - max(char_counts.values()) > k:
                print(s[left:right+1])
                char_counts[s[left]] -= 1
                left += 1
                window_size -= 1
        return best


