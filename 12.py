class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4]
        sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV"] 
        ans = ""
        for i in range(len(val)):
            p, m = divmod(num, val[i])
            if p > 0:
                ans += sym[i] * p
                num = m;
            if num == 0:
                return ans
        if num != 0:
            ans += num * "I"
        return ans
    

