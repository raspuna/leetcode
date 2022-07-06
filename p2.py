#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def addTwonumbers(self, l1, l2):
        sum = ListNode()
        pointer1 = l1
        pointer2 = l2
        pointer3 = sum
        while True:
            #print(pointer1.val, pointer2.val)
            if pointer1:
                v1 = pointer1.val
                pointer1 = pointer1.next
            else:
                v1 = 0
            if pointer2: 
                v2 = pointer2.val
                pointer2 = pointer2.next
            else:
                v2 = 0
            
            val = v1 + v2 + pointer3.val
            exceed = val // 10
            remainder = val % 10
            pointer3.val = remainder
            if exceed or pointer1 or pointer2 : 
                newNode = ListNode(exceed)
                pointer3.next = newNode
                pointer3 = newNode
            else:
                break
    
        return sum
    
s = Solution()
l11 = ListNode(2)
l12 = ListNode(4)
l13 = ListNode(3)
l11.next = l12
l12.next = l13

l21=ListNode(5)
l22 = ListNode(6)
l23= ListNode(4)
l21.next = l22
l22.next = l23
print(s.addTwonumbers(l11, l21))
