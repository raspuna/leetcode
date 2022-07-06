class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def equal(self, a, b):
        p1 = a
        p2 = b
        while True:
            if p1.val != p2.val:
                return False
            else:
                p1 = p1.next
                p2 = p2.next
            if not p1 :
                if p2:
                    return False
                else:
                    return True
            if not p2:
                if p1:
                    return False
                else:
                    return True



class Solution:
    def newSum(self, sum, val):
        if sum:
            sum.next = ListNode(val) 
            return sum
        else:
            return ListNode(val)

    def mergeTwoLists(self, list1, list2):
        list3 = None
        p1 = list1
        p2 = list2
        sum = list3
        while True:
            if (not p1) and (not p2):
                break
            elif not p1:
                if not list3:
                    return p2
                else:
                    sum.next = p2
                    break
            elif not p2:
                if not list3:
                    return p1
                else:
                    sum.next = p1
                    break
            else:
                if p1.val <= p2.val:
                    sum = self.newSum(list3, p1.val)
                    p1 = p1.next
                else:
                    list3 = self.newSum(list3, p2.val)
                    p2 = p2.next
                

        return list3

        

def test(a, b, c):
    s = Solution()
    l = s.mergeTwoLists(toListNode(a), toListNode(b))
    print(l.equal(toListNode(c)))
def toListNode(a_list):
    head = []
    p = None
    for i in a_list:
        l = ListNode(i)
        if not head :
            head = l
            p = l
        l.next = p
        p = l
    return head

test([1,2,4], [1,3,4], [1,1,2,3,4,4])
test([], [], [])
test([], [0], [0])