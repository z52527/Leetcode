class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        ans = 0
        l = 0
        for i, c in enumerate(s):
            if c in dic:
                l = max(dic[c], l)
            ans = max(ans, i - l + 1)
            dic[c] = i + 1
#果然这样写还是不利于理解
#此处l为左指针，i为右指针， 每次向右滑动一次，如果新的字符已经出现过，则更新窗口左指针，取最大值的原因则是防止在两个相同字符中间出现重复字符
#例如abba 在最后一个a的时候更新 dic[a] = 1 dic[b] = 3 l = max(1, 2) 
#dic[c] = i + 1是为了将指针指向重复的下一个
        return ans