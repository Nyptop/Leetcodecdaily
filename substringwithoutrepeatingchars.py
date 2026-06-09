class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 1
        longest = 1
        if len(s) == 0:
            return 0
        if len(s) == 2 and (s[l] != s[r]):
            return 2

        while True:
            longest = max(longest, r - l)
            if r == len(s):
                return longest
            if s[r] not in s[l:r]:
                r += 1
            else: # repeating character
                l += 1
            
            if l == r:
                r += 1