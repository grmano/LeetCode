# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def swapPairs(self, head):
        if( head == None or 
            head.next == None):
            return head

        ret = head.next

        temp = None
        while(head != None and
            head.next != None):
            if(temp and head.next):
                temp.next = head.next

            temp = head
            head = temp.next
            temp.next = head.next
            head.next = temp

            head = temp.next

        return ret

            

a = ListNode(1)
b = Solution()
b.swapPairs(a)
