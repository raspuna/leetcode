
public class P22 {
    public ListNode addList(ListNode a, ListNode b){
        if (a == null) {
            return b;
        } else if (b == null) {
            return a;
        } else {
            ListNode p = a;
            while(p.next != null) {
                p = p.next;
            }
            p.next = b;
            return a;
        }
    }
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode mergedList = null;
        ListNode pointer1 = list1;
        ListNode pointer2 = list2;
        ListNode mergedPointer = mergedList;
        
        while(true) {
            if (pointer1 == null) {
                if (pointer2 == null) {
                    break;
                } else {
                    mergedPointer = addList(mergedPointer, pointer2);
                    if (mergedList == null) {
                        return mergedPointer;
                    } else {
                        return mergedList;
                    }
                }
            } else if (pointer2 == null){
                mergedPointer = addList(mergedPointer, pointer1);
                if (mergedList == null) {
                    return mergedPointer;
                } else {
                    return mergedList;
                }
            } else {
                System.out.println(pointer1.val + " ? " + pointer2.val);
                if (pointer1.val <= pointer2.val) {
                    if (mergedPointer == null) {
                        mergedList = new ListNode(pointer1.val);
                        mergedPointer = mergedList;
                    } else {
                        mergedPointer.next = new ListNode(pointer1.val);
                        mergedPointer = mergedPointer.next;
                    }
                    pointer1 = pointer1.next;
                } else {
                    if (mergedPointer == null) {
                        mergedList = new ListNode(pointer2.val);
                        mergedPointer = mergedList;
                    } else {
                        mergedPointer.next = new ListNode(pointer2.val);
                        mergedPointer = mergedPointer.next;
                    }
                    pointer2 =pointer2.next;
                }
                printList(mergedList);
            }
        }
        return mergedList;
    }
    public ListNode buildList(int[] a) {
        if ((a == null) || (a.length == 0)) {
            printList(null, "build");
            return null;
        }
        ListNode l = new ListNode(a[0]);
        ListNode p = l;
        for (int i = 1; i < a.length; i++) {
            p.next = new ListNode(a[i]);
            p = p.next;
        }
        printList(l, "build");
        return l;
    }
    public void printList(ListNode aNode, String msg) {
        System.out.print(msg + ": ");
        printList(aNode);
    }
    public void printList(ListNode aNode){
        System.out.print("[");
        while(aNode != null) {
            System.out.print(aNode.val+ " -> ");
            aNode = aNode.next;
        }
        System.out.println("]");
    }    
    public static void main(String[] args) {
        P22 myP = new P22();
        int[] a = {1,2,4};
        int[] b = {1,3,4};
        ListNode l1 = myP.buildList(a);
        ListNode l2 = myP.buildList(b);
        ListNode l3 = myP.mergeTwoLists(l1, l2);
        myP.printList(l3);

        int[] c = {};
        int[] d = {0};
        l1 = myP.buildList(c);
        l2 = myP.buildList(d);
        l3 = myP.mergeTwoLists(l1, l2);
        myP.printList(l3);

        int[] e = {1};
        int[] f = {};
        l1 = myP.buildList(e);
        l2 = myP.buildList(f);
        l3 = myP.mergeTwoLists(l1, l2);
        myP.printList(l3);
    }
}
