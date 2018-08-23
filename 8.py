def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        True
    except (TypeError, ValueError):
        pass
 
    return False

class Solution:

 
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        l = -1
        r = -1
        for i, x in enumerate(str):
            if x == ' ':
                if r != -1:
                    break
                continue
            if x != ' ' and l == -1 :
                l = i
                r = i
                if x == "-" or is_number(x):
                    t = 0
                else :
                    return 0
                    break
                continue
            if is_number(x) and l != -1:
                r = i
            else:
                 break
            
        try:
            n = int(str[l:r+1])
        except ValueError:
            return 0
        if n < -2**31:
            n = -2**31
        elif n > 2**31:
            n = 2**31
        return n

print(Solution().myAtoi("    -88827   5655  U"))
                
            
            

        