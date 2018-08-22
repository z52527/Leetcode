class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 or len(s) == 1:
            return s
        p = [true for i in range(2*len(s))]
        st = 0
        mx = 1
        for length in range(1, len(s)+1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if p[i+j]:
                    if s[i] == s[j]:
                        st = i
                        mx = max(mx, length)
                    else :
                        p[i+j] = False
        return s[st:st+mx]