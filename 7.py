class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if x < 0:
            flag = True
            
        if flag:
            n = int("-" + str(x)[1:][::-1])
        else :
            n = int(str(x)[::-1])
        if n < -2**31 or n > 2**31 - 1:
            return 0
        return n
