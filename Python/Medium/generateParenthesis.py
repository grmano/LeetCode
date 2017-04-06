class Solution(object):
    def generateParenthesis(self, n):
        returnList = []
        
        self.genParRec(n, 1, "(", returnList)
        
        return returnList
        """
        :type n: int
        :rtype: List[str]
        """

    def genParRec(self, n, notMatchedParen, string, returnList):

        if (notMatchedParen > n or len(string) > n * 2): #or notMatchedParen - ((n * 2) > len(string))):
            return

        if (n * 2 == len(string) and notMatchedParen == 0):
            returnList.append(string)
            return

        if (notMatchedParen != 0):
            self.genParRec(n, notMatchedParen + 1, string + "(", returnList)
            self.genParRec(n, notMatchedParen - 1, string + ")", returnList)
        else:
            self.genParRec(n, notMatchedParen + 1, string + "(", returnList)

        return
            
s = Solution()
print(s.generateParenthesis(3))
            
