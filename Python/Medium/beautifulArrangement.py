
class Solution(object):
    def countArrangement(self, N):
        if (N == 0):
            return 0
        startingList = range(1, N + 1)
        return self.trySubArrangement(N, startingList, 1);


    def trySubArrangement(self, N, listPossible, pos):
        soma = 0
        if len(listPossible) == 0:
            return 1
        else:
            for x in listPossible:
                if(pos % x == 0 or x % pos == 0):
                    listToPass = listPossible[:]
                    listToPass.remove(x)
                    soma += self.trySubArrangement(N, listToPass, pos + 1)
            return soma
                        
s = Solution()
print(s.countArrangement(13))




            #recursive go trhough every possible subtree and find if is
            #possible with that arrangement
