import re

class Solution(object):
    def reverse(self, x):
        maxInteger = (1<<31) - 1
        minInteger = (1<<31) * -1
        negativeFlag = False

        if( x == 0):
            return 0

        if x < 0:
            negativeFlag = True


        
        x = str(x)
        if negativeFlag:
            x = x[1:len(x)]

        x = x[::-1]
        x = re.compile('^0+').sub('',x)

        if negativeFlag:
            x = '-' + x
        

        x = int(x)

        if( x > maxInteger or x < minInteger):
            return 0

        return x;

        """
        :type x: int
        :rtype: int
        """
s = Solution()
print(s.reverse(-1<<32))

