class Solution(object):
    def addStrings(self, num1, num2):
        if(num1 == None and num2 == None):
            return '0'
            
        num1Array = list(num1)
        num2Array = list(num2)


        size = len(num1Array) if len(num1Array) > len(num2Array) else len(num2Array)
        smallest = len(num1Array) if len(num1Array) < len(num2Array) else len(num2Array)
        
        answer = ''
        carryOn = 0

        for i in range(1,size + 1):
            a = num1Array[len(num1Array) - i] if i <= len(num1Array) else 0 
            b = num2Array[len(num2Array) - i] if i <= len(num2Array) else 0

            
            print(a)
            print(b)

            digit = (int(a) + int(b) + carryOn) % 10
            carryOn = (int(a) + int(b) + carryOn) // 10

            answer = str(digit) + answer

        if(carryOn):
            answer = '1' + answer


        return answer

            
x = Solution()
print(x.addStrings('9','1'))
            
            




        
"""
:type num1: str
:type num2: str
:rtype: str
"""
       
